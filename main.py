import os

# TSE API enviroment variable
TSE_API_ENVIROMENT = os.environ.get("TSE_API")
match TSE_API_ENVIROMENT:
    case 'eleicao_ordinaria':
        from lib.eleicao_ordinaria import Eleicao_Ordinaria
    case _:
        raise Exception("TSE_API enviroment variable not found!")


if __name__ == "__main__":
    tse = Eleicao_Ordinaria()
    tse.download()
    print(1)
