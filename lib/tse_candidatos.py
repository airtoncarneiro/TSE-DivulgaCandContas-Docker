from configparser import ConfigParser, ExtendedInterpolation
import json
import urllib3
import os


class TSE_Candidatos():
    def __init__(self, env):
        try:
            config = ConfigParser(interpolation=ExtendedInterpolation())
            config.sections()
            config.read('config.ini')
            # url = "{}/{}/".format(config["default"]["url_base"], \
            #     config[env]["endpoint"])
            url = config[env]["url"]
            input = config[env].get("folder_input")
            output = config[env]["folder_output"]
        except:
            raise Exception("Arquivo config.ini não encontrado ou mal configurado.")

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
        if input:
            self.input = "{}\\{}".format(os.getcwd(), input)
        self.output = "{}\\{}".format(os.getcwd(), output)
    
    
    # def load(self):
    #     with open('data.json', 'r') as fp:
    #         data = json.load(fp)


    def save(self):
        with open(self.output, 'w') as file:
            json.dump(self.r, file)

    
    
    def download(self, pool_manager:urllib3.PoolManager):
        r = pool_manager.request(method="GET", url=self.url, headers=self.headers)        
        match r.status:
            case 200:
                return json.loads(r.data.decode("utf-8"))
            case _:
                raise Exception("Erro:{}\nDescrição:{}")



class EleicaoOrdinaria(TSE_Candidatos):
    def download(self):
        http = urllib3.PoolManager()
        self.r = super().download(http)
