from flask import Flask
from medicamentos_api import medicamentos_app
import sqlite3

con = sqlite3.connect('banco_dados_medicamentos')
cur = con.cursor()
criar = cur.execute("create table if not exists medicamentos ( \
        id_medicamento integer primary key autoincrement,\
        nome varchar(100),\
        indicacao varchar(500),\
        descricao varchar(500),\
        formulacao varchar(250),\
        apresentacao varchar(250),\
        modo_uso varchar(250),\
        posologia varchar(250),\
        fornecedor varchar(250) )")
con.commit()
con.close()

app = Flask(__name__)
app.register_blueprint(medicamentos_app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)