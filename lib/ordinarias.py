from lib.tse_candidatos import TSE_Candidatos
import urllib3
import logging


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
        logging.info("Obter lista das eleicoes ordinarias.")
        http = urllib3.PoolManager()
        self.r = super().download(url=self.url, pool_manager=http)
        super().save(full_file_name=self.output)
