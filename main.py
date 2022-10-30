import os


TSE_API_ENVIROMENT = os.environ.get("TSE_API")
#TSE_API_ENVIROMENT = 'municipios'
match TSE_API_ENVIROMENT:
    case 'ordinarias':
        from lib.ordinarias import TSE
    case 'municipios':
        from lib.municipios import TSE
    case _:
        raise Exception("TSE_API enviroment variable not found!")

if __name__ == '__main__':
    tse = TSE(env=TSE_API_ENVIROMENT)
    #tse.read_from_file()
    tse.download()
    tse.save()
    print("Fim.")