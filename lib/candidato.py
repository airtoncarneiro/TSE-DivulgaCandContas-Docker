from lib.tse_candidatos import TSE_Candidatos
import urllib3
import logging
import os


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
        http = urllib3.PoolManager()
        for candidatos_file in super().read_from_file():
            tmp_params = "ano={}, codigo={}, id={}, codCand={}"\
                    .format(candidatos_file["ano"],
                            candidatos_file["codigo"],
                            candidatos_file["id"],
                            candidatos_file["codCand"]
                            )
            file = self._replace_arguments(text=self.output,
                custom_dict=candidatos_file)
            if os.path.exists(file):
                logging.info("Já existe candidato: {}".format(tmp_params))
            else:
                logging.info("Obter info de candidato: {}".format(tmp_params))
                
                url = self._replace_arguments(text=self.url,
                    custom_dict=candidatos_file)
                self.r = super().download(url=url, pool_manager=http)

                super().save(full_file_name=file)
