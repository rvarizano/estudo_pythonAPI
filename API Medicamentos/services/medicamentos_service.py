from model.medicamento import Medicamento
from infra.medicamentos_dao import listar as listar_dao, novo as novo_dao, delete as remover_dao, atualiza as atualiza_dao

def listar():
    return listar_dao()

def localiza(id_medicamento):
    for Medicamento in listar_dao():
        if Medicamento.id_medicamento == id_medicamento:
            return Medicamento
    return None

def localizaPorNome(nome):
    for Medicamento in listar_dao():
        if Medicamento.nome == nome:
            return Medicamento
    return None

def localizaPorFornecedor(fornecedor):
    for Medicamento in listar_dao():
        if Medicamento.fornecedor == fornecedor:
            return Medicamento
    return None

def novo(medicamento_data):
    medicamento = Medicamento.cria(medicamento_data)
    if medicamento != None:
        novo_dao(medicamento.__dict__())
        return listar_dao()
    return None

def remover(id_medicamento):
    medicamento = localiza(id_medicamento)
    if medicamento != None:
        remover_dao(medicamento.id_medicamento)
        return listar_dao()
    return None

def atualiza(medicamento_data):
    medicamento = Medicamento.cria(medicamento_data)
    if localiza(medicamento.id_medicamento) != None:
        if medicamento != None:
            atualiza_dao(medicamento.__dict__())
            return listar_dao()
    return None