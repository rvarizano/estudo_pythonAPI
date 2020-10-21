import sqlite3
from model.medicamento import Medicamento

def listar():
    medicamentos = []
    con = sqlite3.connect('banco_dados_medicamentos')
    cur = con.cursor()    
    cur.execute("select id_medicamento, nome, indicacao, descricao,\
    formulacao, apresentacao, modo_uso, posologia, fornecedor\
         from medicamentos")
    
    medicamentos = [Medicamento.cria_de_tupla(linha) for linha in cur.fetchall()]

    con.close()
    return medicamentos

def novo(medicamento_dicionario):
    con = sqlite3.connect('banco_dados_medicamentos')
    cur = con.cursor()    
    cur.execute("insert into medicamentos\
    (nome, indicacao, descricao,\
    formulacao, apresentacao, modo_uso, posologia, fornecedor)\
    values(:nome, :indicacao, :descricao,\
    :formulacao, :apresentacao, :modo_uso, :posologia, :fornecedor)", medicamento_dicionario)
    con.commit()
    con.close()


def delete(id_medicamento):
    con = sqlite3.connect('banco_dados_medicamentos')
    cur = con.cursor()
    cur.execute("delete from medicamentos where id_medicamento = ? ", (id_medicamento,))
    con.commit()
    con.close()

def atualiza(medicamento_data):
    con = sqlite3.connect('banco_dados_medicamentos')
    cur = con.cursor()
    print(medicamento_data)
    cur.execute("update medicamentos set\
    nome = :nome,\
    indicacao = :indicacao,\
    descricao = :descricao,\
    formulacao = :formulacao,\
    apresentacao = :apresentacao,\
    modo_uso = :modo_uso,\
    posologia = :posologia,\
    fornecedor = :fornecedor\
    where id_medicamento = :id ", medicamento_data)
    con.commit()
    con.close()
