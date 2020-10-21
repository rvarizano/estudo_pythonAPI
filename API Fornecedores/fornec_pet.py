from flask import Flask
from fornecedores_api import fornecedores_app
import sqlite3

con = sqlite3.connect('banco_dados_fornecedores')
cur = con.cursor()
criar = cur.execute("create table if not exists fornecedores ( \
        id_fornecedor integer primary key autoincrement,\
        nome varchar(100),\
        cep varchar(8),\
        logradouro varchar(200),\
        complemento varchar(50),\
        bairro varchar(150),\
        localidade varchar(250),\
        uf varchar(5) )")
con.commit()
con.close()

app = Flask(__name__)
app.register_blueprint(fornecedores_app)

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
