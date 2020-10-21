class Medicamento():
    def __init__(self, id_medicamento, nome, indicacao, descricao, formulacao, apresentacao, modo_uso, posologia, fornecedor):
        self.id_medicamento = id_medicamento
        self.nome = nome
        self.indicacao = indicacao
        self.descricao = descricao
        self.formulacao = formulacao
        self.apresentacao = apresentacao
        self.modo_uso = modo_uso
        self.posologia = posologia
        self.fornecedor = fornecedor

    def atualizar(self, dados):
        try:
            if "id" and "nome" in dados:
                id_medicamento = dados["id"]
                nome = dados["nome"]
                indicacao = dados["indicacao"]
                descricao = dados["descricao"]
                formulacao = dados["formulacao"]
                apresentacao = dados["apresentacao"]
                modo_uso = dados["modo_uso"]
                posologia = dados["posologia"]
                fornecedor = dados["fornecedor"]
                self.id_medicamento, self.nome, self.indicacao, self.descricao, self.formulacao, self.apresentacao, self.modo_uso, self.posologia, self.fornecedor = id_medicamento, nome, indicacao, descricao, formulacao, apresentacao, modo_uso, posologia, fornecedor
                return self
        except Exception as e:
            print("Problema ao criar novo medicamento!")
            print(e)
            return None

    def __dict__(self):
        d = dict()
        d['id'] = self.id_medicamento
        d['nome'] = self.nome
        d['indicacao'] = self.indicacao
        d['descricao'] = self.descricao
        d['formulacao'] = self.formulacao
        d['apresentacao'] = self.apresentacao
        d['modo_uso'] = self.modo_uso
        d['posologia'] = self.posologia
        d['fornecedor'] = self.fornecedor
        return d

    @staticmethod
    def cria(dados):
        try:
            if "id" and "nome" in dados:
                id_medicamento = dados["id"]
                nome = dados["nome"]
                indicacao = dados["indicacao"]
                descricao = dados["descricao"]
                formulacao = dados["formulacao"]
                apresentacao = dados["apresentacao"]
                modo_uso = dados["modo_uso"]
                posologia = dados["posologia"]
                fornecedor = dados["fornecedor"]            
            return Medicamento(id_medicamento=id_medicamento, nome=nome, indicacao=indicacao, descricao=descricao, formulacao=formulacao, apresentacao=apresentacao, modo_uso=modo_uso, posologia=posologia, fornecedor=fornecedor)
        except Exception as e:
            print("Problema ao criar novo medicamento!")
            print(e)
            return None

    @staticmethod
    def cria_de_tupla(registro):
        try:
            id_medicamento = registro[0]
            nome = registro[1]
            indicacao = registro[2]
            descricao = registro[3]
            formulacao = registro[4]
            apresentacao = registro[5]
            modo_uso = registro[6]
            posologia = registro[7]
            fornecedor = registro[8]
            return Medicamento(id_medicamento=id_medicamento, nome=nome, indicacao=indicacao, descricao=descricao, formulacao=formulacao, apresentacao=apresentacao, modo_uso=modo_uso, posologia=posologia, fornecedor=fornecedor)
        except Exception as e:
            print("Problema ao criar novo medicamento!")
            print(e)