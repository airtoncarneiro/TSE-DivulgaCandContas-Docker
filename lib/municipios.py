from lib.tse_candidatos import TSE_Candidatos
import urllib3


class TSE(TSE_Candidatos):
    def download(self):
        UFS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
                'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
                'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', ]

        http = urllib3.PoolManager()
        for eleicao in super().read_from_file():
            if eleicao['ano'] == 2020:
                print(eleicao['ano'])
                for uf in UFS:
                    eleicao['siglaUF'] = uf
                    url = self._replace_arguments(text=self.url,
                        custom_dict=eleicao)
                    self.r = super().download(url=url, pool_manager=http)

                    # se há eleições na UF
                    if self.r['municipios']:
                        file = self._replace_arguments(text=self.output,
                            custom_dict=eleicao)
                        super().save(full_file_name=file)
