from lib.tse_candidatos import TSE_Candidatos
import urllib3


class TSE(TSE_Candidatos):
    def download(self):
        TIPOS = {"11":"Prefeito",
                 "12":"Vice-Prefeito",
                 "13":"Vereador"}

        http = urllib3.PoolManager()
        for municipios_UF_file in super().read_from_file():
            for tipo in TIPOS:
                municipios_UF_file['tipo'] = tipo
                url = self._replace_arguments(text=self.url,
                    custom_dict=municipios_UF_file)
                self.r = super().download(url=url, pool_manager=http)

                file = self._replace_arguments(text=self.output,
                    custom_dict=municipios_UF_file)
                super().save(full_file_name=file)
