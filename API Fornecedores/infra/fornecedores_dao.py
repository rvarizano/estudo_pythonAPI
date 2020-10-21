import sqlite3
from model.fornecedor import Fornecedor

def listar():
    fornecedores = []
    con = sqlite3.connect('banco_dados_fornecedores')
    cur = con.cursor()    
    cur.execute("select id_fornecedor, nome, cep, logradouro,\
    complemento, bairro, localidade, uf \
    from fornecedores")
    
    fornecedores = [Fornecedor.cria_de_tupla(linha) for linha in cur.fetchall()]

    con.close()
    return fornecedores

def novo(fornecedor_dicionario):
    con = sqlite3.connect('banco_dados_fornecedores')
    cur = con.cursor()    
    cur.execute("insert into fornecedores (nome, cep, logradouro,\
    complemento, bairro, localidade, uf)\
    values(:nome, :cep, :logradouro,\
    :complemento, :bairro, :localidade, :uf)", fornecedor_dicionario)
    con.commit()
    con.close()


def delete(id_fornecedor):
    con = sqlite3.connect('banco_dados_fornecedores')
    cur = con.cursor()
    cur.execute("delete from fornecedores where id_fornecedor = ? ", (id_fornecedor,))
    con.commit()
    con.close()

def atualiza(fornecedor_data):
    con = sqlite3.connect('banco_dados_fornecedores')
    cur = con.cursor()
    print(fornecedor_data)
    cur.execute("update fornecedores set nome = :nome,\
    cep = :cep,\
    logradouro = :logradouro,\
    complemento = :complemento,\
    bairro = :bairro,\
    localidade = :localidade,\
    uf = :uf\
    where id_fornecedor = :id ", fornecedor_data)
    con.commit()
    con.close()
