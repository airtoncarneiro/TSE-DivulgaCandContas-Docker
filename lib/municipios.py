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
        UFS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
                "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
                "RS", "RO", "RR", "SC", "SP", "SE", "TO", ]

        http = urllib3.PoolManager()
        for ordinarias_file in super().read_from_file():
            for uf in UFS:
                ordinarias_file["siglaUF"] = uf
                
                tmp_params = "siglaUF={}, id={}".format(ordinarias_file["siglaUF"],
                                    ordinarias_file["id"]
                                    )
                file = self._replace_arguments(text=self.output,
                    custom_dict=ordinarias_file)
                if os.path.exists(file):
                    logging.info("Já existe municipios: {}".format(tmp_params))
                else:                
                    logging.info("Obter lista de municipios: siglaUF={}, id={}"\
                        .format(ordinarias_file["siglaUF"],
                                ordinarias_file["id"]
                                ))
                    
                    url = self._replace_arguments(text=self.url,
                        custom_dict=ordinarias_file)
                    self.r = super().download(url=url, pool_manager=http)

                    # se há eleições na UF
                    if self.r["municipios"]:
                        super().save(full_file_name=file)
