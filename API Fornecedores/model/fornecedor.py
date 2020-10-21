from services.viacep_service import ViaCep
from services.verificaFornecedor import verificaFornecedor

class Fornecedor():
    def __init__(self, id_fornecedor, nome, cep, logradouro, complemento, bairro, localidade, uf):
        self.id_fornecedor = id_fornecedor
        self.nome = nome
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf

    def atualizar(self, dados):
        try:
            if "id" and "nome" and "cep" in dados:
                id_fornecedor = dados["id"]
                nome = dados["nome"]
                cep = dados["cep"]
                viacep = ViaCep(cep)
                logradouro = viacep.buscar_logradouro()
                complemento = viacep.buscar_complemento()
                bairro = viacep.buscar_bairro()
                localidade = viacep.buscar_localidade()
                uf = viacep.buscar_uf()
                self.id_fornecedor, self.nome, self.cep, self.logradouro, self.complemento, self.bairro, self.localidade, self.uf = id_fornecedor, nome, cep, logradouro, complemento, bairro, localidade, uf
                if verificaFornecedor(nome) == True:
                    return self
            else:
                print("Nenhum produto cadastrado com esse fornecedor!")
                return None
        except Exception as e:
            print("Problema ao criar novo fornecedor!")
            print(e)
            return None

    def __dict__(self):
        d = dict()
        d['id'] = self.id_fornecedor
        d['nome'] = self.nome
        d['cep'] = self.cep
        d['logradouro'] = self.logradouro
        d['complemento'] = self.complemento
        d['bairro'] = self.bairro
        d['localidade'] = self.localidade
        d['uf'] = self.uf
        return d

    @staticmethod
    def cria(dados):
        try:
            if "id" and "nome" in dados:
                id_fornecedor = dados["id"]
                nome = dados["nome"]
                cep = dados["cep"]
                viacep = ViaCep(cep)
                logradouro = viacep.buscar_logradouro()
                complemento = viacep.buscar_complemento()
                bairro = viacep.buscar_bairro()
                localidade = viacep.buscar_localidade()
                uf = viacep.buscar_uf()
                verifica = verificaFornecedor(nome)
            if verifica == nome:
                return Fornecedor(id_fornecedor=id_fornecedor, nome=nome, cep=cep, logradouro=logradouro, complemento=complemento, bairro=bairro, localidade=localidade, uf=uf)
            else:
                print("Nenhum produto cadastrado com esse fornecedor!")
                return None
                
        except Exception as e:
            print("Problema ao criar novo fornecedor!")
            print(e)
            return None

    @staticmethod
    def cria_de_tupla(registro):
        try:
            id_fornecedor = registro[0]
            nome = registro[1]
            cep = registro[2]
            logradouro = registro[3]
            complemento = registro[4]
            bairro = registro[5]
            localidade = registro[6]
            uf = registro[7]
            return Fornecedor(id_fornecedor=id_fornecedor, nome=nome, cep=cep, logradouro=logradouro, complemento=complemento, bairro=bairro, localidade=localidade, uf=uf)
        except Exception as e:
            print("Problema ao criar novo fornecedor!")
            print(e)