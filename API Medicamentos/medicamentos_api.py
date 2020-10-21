from flask import Blueprint, jsonify, request
from services.medicamentos_service import listar as service_listar, \
    localiza as service_localiza, \
    localizaPorNome as service_localizaPorNome, \
    localizaPorFornecedor as service_localizaPorFornecedor, \
    novo as service_novo, \
    remover as service_remover, \
    atualiza as service_atualiza

medicamentos_app = Blueprint('medicamentos_app', __name__, template_folder='templates')

@medicamentos_app.route('/medicamentos', methods=['GET'])
def listar():
    med_lista = service_listar()
    if med_lista != None:
        return jsonify(list(map(lambda med: med.__dict__(), med_lista)))
    return 'Erro extraordinário definitivamente não esperado.', 404

@medicamentos_app.route('/medicamentos/<int:id_medicamento>', methods=['GET'])
def localiza(id_medicamento):
    medicamento = service_localiza(id_medicamento)
    if medicamento != None:
        return jsonify(medicamento.__dict__())
    return 'Nenhum medicamento cadastrado com essa ID.', 404

@medicamentos_app.route('/medicamentos/<nome>', methods=['GET'])
def localizaPorNome(nome):
    medicamento = service_localizaPorNome(nome)
    if medicamento != None:
        return jsonify(medicamento.__dict__())
    return 'Nenhum medicamento cadastrado com esse Nome.', 404

@medicamentos_app.route('/medicamentos/fornecedor/<fornecedor>', methods=['GET'])
def localizaPorFornecedor(fornecedor):
    medicamento = service_localizaPorFornecedor(fornecedor)
    if medicamento != None:
        return jsonify(medicamento.__dict__())
    return 'Nenhum medicamento cadastrado com esse Fornecedor.', 404

@medicamentos_app.route('/medicamentos', methods=['POST'])
def novo():
    novo_medicamento = request.get_json()
    med_lista = service_novo(novo_medicamento)
    if med_lista != None:
        return jsonify(list(map(lambda med: med.__dict__(), med_lista)))
    return 'Algum dado não foi inputado corretamente. Verifique sua inserção.', 404

@medicamentos_app.route('/medicamentos/<int:id_medicamento>', methods=['DELETE'])
def remover(id_medicamento):
    removido = service_remover(id_medicamento)
    if removido != None:
        return jsonify(removido.__dict__())
    return 'Nenhum medicamento cadastrado com essa ID.', 404

@medicamentos_app.route('/medicamentos', methods=['PUT'])
def atualiza():
    atualiza_medicamento = request.get_json()
    med_lista = service_atualiza(atualiza_medicamento)
    if med_lista != None:
        return jsonify(list(map(lambda med: med.__dict__(), med_lista)))
    return 'Algum dado não foi inputado corretamente. Verifique sua inserção.', 404
