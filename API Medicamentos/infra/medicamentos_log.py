from datetime import datetime
class MedicamentoLog():
    def __init__(self, medicamento):
        self.original_data = medicamento.__dict__()
        self.ultima_atualizacao = medicamento.__dict__()
        self.start_time = datetime.now()

    def atualiza(self, medicamento):
        self.ultima_atualizacao = medicamento.__dict__()

    def finaliza_e_imprime(self):
        print(f'Mudanças iniciaram em {self.start_time}')
        print(f'Valor original:')
        print(self.original_data)
        print(f'Valor final:')
        print(self.ultima_atualizacao)
        print(f'Mudanças finalizaram em {datetime.now()}')
