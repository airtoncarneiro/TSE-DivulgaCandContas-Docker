import os


TSE_API_ENVIROMENT = os.environ.get("TSE_API")
match TSE_API_ENVIROMENT:
    case 'eleicao_ordinaria':
        from lib.tse_candidatos import EleicaoOrdinaria
    case _:
        raise Exception("TSE_API enviroment variable not found!")

if __name__ == '__main__':
    tse = EleicaoOrdinaria(env=TSE_API_ENVIROMENT)
    tse.download()
    tse.save()
    print("Fim.")