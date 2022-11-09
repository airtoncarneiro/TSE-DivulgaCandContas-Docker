import os
import logging
from time import sleep


logging.basicConfig(format="%(asctime)s - %(process)d - %(levelname)s "\
                            "- %(message)s",
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])
logging.info("==== Inicio. =====")

TSE_API_ENVIROMENT = os.environ.get("TSE_API")
TSE_API_ENVIROMENT="ordinarias"
match TSE_API_ENVIROMENT:
    case "ordinarias":
        from lib.ordinarias import TSE
    case "municipios":
        from lib.municipios import TSE
    case "candidatos":
        from lib.candidatos import TSE
    case "candidato":
        from lib.candidato import TSE
    case _:
        msg = "TSE_API enviroment variable not found!"
        logging.error(msg)
        raise TypeError(msg)

if __name__ == '__main__':
    qtdExecucoes = 1
    while qtdExecucoes < 6:
        logging.info("Execucao #{}".format(qtdExecucoes))
        
        tse = TSE(env=TSE_API_ENVIROMENT)
        tse.download()
        
        sleep(60 * 5)
        qtdExecucoes += 1
                
    logging.info("==== Fim.     ====")
