import json
import os
import re
from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path

import urllib3


class TSE_Candidatos():
    """Classe (pai) responsável pelas tratativas e ações que cada API no TSE
       deve fazer.
    """
    def __init__(self, env:str)->None:
        """Inicialização da classe.

        Args:
            env (str): Variável de ambiente.
            Valores possíveis:
              * ordinarias
              * municipios
              * candidatos
              * candidato

        Raises:
            Exception: Se a variável de ambiente não for válida
              ou algumas variáveis no arquivo config.ini não
              localizadas.
        """
        try:
            config = ConfigParser(interpolation=ExtendedInterpolation())
            config.sections()
            config.read('config.ini')
            url = config[env]["url"]
            input_folder = config[env].get("input_folder")
            input_file = config[env].get("input_file")
            output_folder = config[env]["output_folder"]
            output_file = config[env].get("output_file")
        except:
            raise Exception("Arquivo config.ini não encontrado ou mal "\
                "configurado.")

        self.url = url
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;"\
                "q=0.9,image/avif,image/webp,image/apng,*/*;"\
                "q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"pt,en-US;q=0.9,en;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2"\
                " (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2"
        }
        if input_folder:
            self.input_folder = os.path.join(os.getcwd(), os.path.normpath(input_folder))
            self.input_file = input_file
        self.output = os.path.join(os.getcwd(), output_folder, os.path.normpath(output_file))

    def save(self, full_file_name:str)->None:
        """Salva o arquivo.

        Args:
            full_file_name (str): Nome do arquivo incluindo o full path.
        """
        os.makedirs(os.path.dirname(full_file_name), exist_ok=True)
        with open(full_file_name, 'w', encoding='utf8') as file:
            json.dump(self.r, file, ensure_ascii=False)
    
    def read_from_file(self)->dict:
        """Lê os arquivos.

        Returns:
            dict: Retorna um dicionário.

        Yields:
            Iterator[dict]: Como pode haver vários arquivos e, cada um deles,
                pode ter uma lista de dicionários, retornar cada um com Yield.
        """
        files = Path(self.input_folder).rglob(self.input_file)
        for file in files:
            custom_dict = self._makeADictFromPath(str(file))
            with open(file, encoding='utf-8') as json_file:
                objs = json.load(json_file)
                # Como a iteração deve ser na lista vindo do JSON
                # e, algumas vezes, a lista não é o único objeto
                # do arquivo, garantir retornar sempre uma lista
                if type(objs) == list:
                    for obj in objs:
                        for key, value in custom_dict.items():
                            obj[key] = value
                        yield obj
                else:
                    for _, value in objs.items():
                        if type(value) == list:
                            for obj in value:
                                if "candidatos" in objs and \
                                not("codCand") in obj:
                                   obj["codCand"] = obj["id"]
                                for key, value in custom_dict.items():
                                    obj[key] = value
                                yield obj
    
    def download(self, url:str, pool_manager:urllib3.PoolManager)->dict:
        """Realiza o método GET na API do TSE.

        Args:
            url (str): URL da chamada.
            pool_manager (urllib3.PoolManager): Gerenciador da conexão.

        Raises:
            Exception: Caso 'status code' != 200.

        Returns:
            dict: Resposta ao GET.
        """
        r = pool_manager.request(method="GET",
                                url=url, 
                                headers=self.headers)
        match r.status:
            case 200:
                return json.loads(r.data.decode("utf-8"))
            case _:
                raise Exception("Erro:{}\nDescrição:{}".format(r.status, ''))
    
    def _replace_arguments(self, text:str, custom_dict:dict)->str:
        """Faz a correspondência entre os parâmetros passados e suas
           respecivas chaves/valores, substituindo-os.

        Args:
            text (str): Texto com chaves e valores a serem substituídos.
            custom_dict (dict): Dicionário com as chaves e valores para
                referência de pesquisa e substituição.

        Returns:
            str: Texto com as chaves e valores substituídos.
        """
        pattern = "{\w*}"
        custom_text = text
        # Substitui os parâmetros da URL por seus respectivos valores
        for matched in re.findall(pattern, custom_text):
            key = [matched[1:-1]][0]
            custom_text = custom_text.replace(matched, str(custom_dict.get(key, matched)))

        return custom_text
    
    def _makeADictFromPath(self, path:str)->dict:
        """Do PATH substitui as chaves/valores. Cada chave/valor do path fará
           parte do dicionário.
           Ex.: ../output/ano=2020/  -> dict = {'ano':2020}

        Args:
            path (str): Path do arquivo.

        Returns:
            dict: Path com as chaves/valores substituídos.
        """
        customDict = dict()
        for key_value in path.split('\\'):
            if '=' in key_value:
                key, value = key_value.split('=')
                customDict[key] = value
        return customDict
