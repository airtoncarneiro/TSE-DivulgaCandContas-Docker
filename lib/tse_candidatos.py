from configparser import ConfigParser, ExtendedInterpolation
import urllib3
import os
import json
from pathlib import Path
import re


class TSE_Candidatos():
    def __init__(self, env):
        try:
            config = ConfigParser(interpolation=ExtendedInterpolation())
            config.sections()
            config.read('config.ini')
            url = config[env]["url"]
            input_folder = config[env].get("input_folder")
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
            self.input = "{}\\{}".format(os.getcwd(), input_folder)
        self.output = "{}\\{}\\{}".format(os.getcwd(), output_folder, 
                                        output_file)

    def save(self, full_file_name:str):
        os.makedirs(os.path.dirname(full_file_name), exist_ok=True)
        with open(full_file_name, 'w') as file:
            json.dump(self.r, file)
    
    def read_from_file(self):
        folder = self.input
        files = Path(folder).glob('*.json')
        for file in files:
            with open(file, encoding='utf-8') as json_file:
                objs = json.load(json_file)
                for obj in objs:
                    yield obj
    
    def download(self, url:str, pool_manager:urllib3.PoolManager):
        r = pool_manager.request(method="GET",
                                url=url, 
                                headers=self.headers)
        match r.status:
            case 200:
                return json.loads(r.data.decode("utf-8"))
            case _:
                raise Exception("Erro:{}\nDescrição:{}".format(r.status, ''))
    
    def _replace_arguments(self, text:str, custom_dict:dict):
        pattern = "{\w*}"
        # Substitui os parâmetros da URL por seus respectivos valores
        for matched in re.findall(pattern, text):
            key = [matched[1:-1]][0]
            text = text.replace(matched, str(custom_dict.get(key, matched)))

        return text
