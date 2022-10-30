from lib.tse_candidatos import TSE_Candidatos
import urllib3



class TSE(TSE_Candidatos):
    def read_from_file(self):
        return super().read_from_file()

    def download(self):
        http = urllib3.PoolManager()
        self.r = super().download(http)
