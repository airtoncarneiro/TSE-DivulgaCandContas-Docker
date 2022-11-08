import os
import logging


logging.basicConfig(format="%(asctime)s - %(process)d - %(levelname)s "\
                            "- %(message)s",
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])
logging.info("==== Inicio. =====")

TSE_API_ENVIROMENT = os.environ.get("TSE_API")
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
    tse = TSE(env=TSE_API_ENVIROMENT)
    tse.download()
    
    logging.info("==== Fim.     ====")
