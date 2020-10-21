from flask import Blueprint, jsonify, request
from services.fornecedores_service import listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    remover as service_remover, \
    atualiza as service_atualiza

fornecedores_app = Blueprint('fornecedores_app', __name__, template_folder='templates')

@fornecedores_app.route('/fornecedores', methods=['GET'])
def listar():
    fornec_list = service_listar()
    if fornec_list != None:
        return jsonify(list(map(lambda fornec: fornec.__dict__(), fornec_list)))
    return 'Erro extraordinário definitivamente não esperado.', 404

@fornecedores_app.route('/fornecedores/<int:id_fornecedor>', methods=['GET'])
def localiza(id_fornecedor):
    fornecedor = service_localiza(id_fornecedor)
    if fornecedor != None:
        return jsonify(fornecedor.__dict__())
    return 'Nenhum fornecedor cadastrado com essa ID.', 404

@fornecedores_app.route('/fornecedores', methods=['POST'])
def novo():
    novo_fornecedor = request.get_json()
    fornec_list = service_novo(novo_fornecedor)
    if fornec_list != None:
        return jsonify(list(map(lambda fornec: fornec.__dict__(), fornec_list)))
    return 'Algum dado não foi inputado corretamente. Verifique sua inserção.', 404

@fornecedores_app.route('/fornecedores/<int:id_fornecedor>', methods=['DELETE'])
def remover(id_fornecedor):
    removido = service_remover(id_fornecedor)
    if removido != None:
        return jsonify(removido.__dict__())
    return 'Nenhum fornecedor cadastrado com essa ID.', 404

@fornecedores_app.route('/fornecedores', methods=['PUT'])
def atualiza():
    atualiza_fornecedor = request.get_json()
    fornec_list = service_atualiza(atualiza_fornecedor)
    if fornec_list != None:
        return jsonify(list(map(lambda fornec: fornec.__dict__(), fornec_list)))
    return 'Algum dado não foi inputado corretamente. Verifique sua inserção.', 404
