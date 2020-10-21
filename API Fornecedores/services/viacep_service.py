import json
import requests

class ViaCep:
    def __init__(self, cep):
        self.cep = cep

    def buscar_logradouro(self):
        url = "http://viacep.com.br/ws/{}/json".format(self.cep)
        retorno = json.loads(requests.get(url).text)
        return retorno["logradouro"]

    def buscar_complemento(self):
        url = "http://viacep.com.br/ws/{}/json".format(self.cep)
        retorno = json.loads(requests.get(url).text)
        return retorno['complemento']

    def buscar_bairro(self):
        url = "http://viacep.com.br/ws/{}/json".format(self.cep)
        retorno = json.loads(requests.get(url).text)
        return retorno['bairro']

    def buscar_localidade(self):
        url = "http://viacep.com.br/ws/{}/json".format(self.cep)
        retorno = json.loads(requests.get(url).text)
        return retorno['localidade']

    def buscar_uf(self):
        url = "http://viacep.com.br/ws/{}/json".format(self.cep)
        retorno = json.loads(requests.get(url).text)
        return retorno['uf']

