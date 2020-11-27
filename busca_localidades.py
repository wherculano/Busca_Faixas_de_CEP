import json
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


class BuscaLocalidades:
    SIGLAS = iter(['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB',
                   'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'])

    def __init__(self, browser, url_page):
        self.browser = browser
        self.url = url_page
        self.estados_dict = {}
        self.__count_id = 1

    def acessar_site(self):
        self.browser.get(self.url)
        sleep(2)

    def salvar_localidades(self):
        estados = self.browser.find_element_by_class_name("f1col")
        try:
            sigla_atual = next(self.SIGLAS)
            estados.send_keys(sigla_atual)
        except StopIteration:
            print('.:: Fim da Consulta ::.')
            exit()

        btn_buscar = self.browser.find_element_by_class_name("btn2,float-right")
        btn_buscar.click()
        sleep(2)
        tabela_localidade = navegador.find_elements_by_tag_name('tbody')

        result = tabela_localidade[1].text.split('\n')[1:]
        for i in range(len(result)):
            primeiro_hifen = result[i].find('-')
            faixa = result[i][primeiro_hifen - 5: primeiro_hifen + 16]
            localidade = result[i][:primeiro_hifen - 6]
            self.estados_dict[sigla_atual] = self.estados_dict.get(sigla_atual,
                                                                   {localidade: {'ID': self.__count_id,
                                                                                 'Faixa de CEP': faixa}})
            self.estados_dict[sigla_atual][localidade] = self.estados_dict[sigla_atual].get(localidade,
                                                                                            {'ID': self.__count_id,
                                                                                             'Faixa de CEP': faixa})
            self.__count_id += 1

            with open('dados.jsonl', 'w') as f:
                json.dump(self.estados_dict, f, ensure_ascii=False)

        navegador.back()
        self.salvar_localidades()


if __name__ == '__main__':
    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    options = ChromeOptions()
    options.add_argument("--headless")
    navegador = Chrome(options=options)
    buscacep = BuscaLocalidades(navegador, url)
    buscacep.acessar_site()
    buscacep.salvar_localidades()
