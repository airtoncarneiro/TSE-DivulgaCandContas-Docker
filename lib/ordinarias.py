from lib.tse_candidatos import TSE_Candidatos
import urllib3


class TSE(TSE_Candidatos):
    def download(self):
        http = urllib3.PoolManager()
        self.r = super().download(url=self.url, pool_manager=http)
        super().save(full_file_name=self.output)
