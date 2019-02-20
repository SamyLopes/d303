class Carro:
    qtde_rodas: 4

    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def buzinar(self):
        print('Biiibiii')

    def acelerar(self):
        print('Vrooom Vrooom')

carro1 = Carro('vermelho', 'Ferrari', 'FF')
carro1.buzinar()
carro1.acelerar()