from lib.tse_candidatos import TSE_Candidatos
import urllib3
import logging
import os


class TSE(TSE_Candidatos):
    """Classe herdada de TSE_Candidatos com sobreescrição do método de
       download.

    Args:
        TSE_Candidatos (_type_): Classe pai com métodos e operações em cima
        das APIs do TSE.
    """
    def download(self)->None:
        """Realiza a operação de GET no site do TSE e salve o resultado
           num arquivo sobreescrevendo o método pai.
        """
        TIPOS = {
                 "1": "Presidente",
                 "3": "Governador",
                 "5": "Senador",
                 "6": "Deputado Federal",
                 "7": "Deputado Estadual",
                 "11":"Prefeito",
                 "12":"Vice-Prefeito",
                 "13":"Vereador"
                 }

        http = urllib3.PoolManager()
        for municipios_UF_file in super().read_from_file():
            for tipo in TIPOS:
                if tipo != '11':
                    continue
                
                municipios_UF_file["tipo"] = tipo
                tmp_params = "ano={}, codigo={}, id={}, tipo={}"\
                    .format(municipios_UF_file["ano"],
                            municipios_UF_file["codigo"],
                            municipios_UF_file["id"],
                            municipios_UF_file["tipo"]
                            )
                file = self._replace_arguments(text=self.output,
                    custom_dict=municipios_UF_file)
                if os.path.exists(file):
                    logging.info("Já existe candidato: {}".format(tmp_params))
                else:
                    logging.info("Obter lista de candidatos: "\
                        "{}, UF={}, Cidade={}".format(tmp_params,
                        municipios_UF_file["uf"],
                        municipios_UF_file["nome"]))
                    
                    url = self._replace_arguments(text=self.url,
                        custom_dict=municipios_UF_file)
                    self.r = super().download(url=url, pool_manager=http)

                    super().save(full_file_name=file)
