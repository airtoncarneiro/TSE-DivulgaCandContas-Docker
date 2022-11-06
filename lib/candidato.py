from lib.tse_candidatos import TSE_Candidatos
import urllib3


class TSE(TSE_Candidatos):
    def download(self):
        http = urllib3.PoolManager()
        for candidatos_file in super().read_from_file():
            url = self._replace_arguments(text=self.url,
                custom_dict=candidatos_file)
            self.r = super().download(url=url, pool_manager=http)

            file = self._replace_arguments(text=self.output,
                custom_dict=candidatos_file)
            super().save(full_file_name=file)
