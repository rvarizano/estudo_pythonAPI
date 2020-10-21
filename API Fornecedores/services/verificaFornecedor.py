import json
import requests

def verificaFornecedor(nome_fornecedor):
        url = "http://localhost:5000/medicamentos/fornecedor/{}".format(nome_fornecedor)
        retorno = json.loads(requests.get(url).text)
        return retorno['fornecedor']

