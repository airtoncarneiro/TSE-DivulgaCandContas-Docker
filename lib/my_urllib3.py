from asyncio import exceptions
from http.client import HTTPResponse
import json
import urllib3

class My_Urllib3():
    def __init__(self, url:str) -> urllib3.PoolManager:
        """Inicializa a biblioteca para realizar o download das informacoes
        do site do TSE

        Returns:
            urllib3.PoolManager: Instancia para fazer as requisicoes
        """
        self.url = url
        self.http = urllib3.PoolManager()
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;"\
                "q=0.9,image/avif,image/webp,image/apng,*/*;"\
                "q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"pt,en-US;q=0.9,en;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2"\
                " (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2"
        }

    def my_request(self)->urllib3.response.HTTPResponse:
        r = self.http.request(method="GET", url=self.url, headers=self.headers)        
        match r.status:
            case 200:
                return json.loads(r.data.decode("utf-8"))
            case _:
                raise Exception("Erro:{}\nDescrição:{}")
        
        return None