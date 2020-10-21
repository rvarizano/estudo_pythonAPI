from model.fornecedor import Fornecedor
from infra.fornecedores_dao import listar as listar_dao, novo as novo_dao, delete as remover_dao, atualiza as atualiza_dao

def listar():
    return listar_dao()

def localiza(id_fornecedor):
    for Fornecedor in listar_dao():
        if Fornecedor.id_fornecedor == id_fornecedor:
            return Fornecedor
    return None

def novo(fornecedor_data):
    fornecedor = Fornecedor.cria(fornecedor_data)
    if fornecedor != None:
        novo_dao(fornecedor.__dict__())
        return listar_dao()
    else:
        return None

def remover(id_fornecedor):
    fornecedor = localiza(id_fornecedor)
    if fornecedor != None:
        remover_dao(fornecedor.id_fornecedor)
        return listar_dao()
    return None

def atualiza(fornecedor_data):
    fornecedor = Fornecedor.cria(fornecedor_data)
    if localiza(fornecedor.id_fornecedor) != None:
        if fornecedor != None:
            atualiza_dao(fornecedor.__dict__())
            return listar_dao()
    else:
        return None
