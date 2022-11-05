from lib.tse_candidatos import TSE_Candidatos
import urllib3


class TSE(TSE_Candidatos):
    def download(self):
        TIPOS = {"11":"Prefeito",
                "12":"Vice-Prefeito",
                "13":"Vereador"}

        http = urllib3.PoolManager()
        for municipios_UF_file in super().read_from_file():
            print(municipios_UF_file)
            for tipo in TIPOS:
                print(tipo)