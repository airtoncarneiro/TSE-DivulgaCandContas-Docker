from lib.my_urllib3 import My_Urllib3

class Eleicao_Ordinaria():
    def __init__(self):
        """Faz a requisicao a Eleicao Ordinaria.
        Passo 1 de ...
        """
        url = "https://divulgacandcontas.tse.jus.br/divulga/rest/v1/" \
            "eleicao/ordinarias/"
        self.my_urllib3 = My_Urllib3(url)


    def download(self):
        r = self.my_urllib3.my_request()
        print(1)