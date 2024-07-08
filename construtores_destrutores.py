class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


c1 = Cachorro("Chappie", "amarelo")
c2 = Cachorro("Thor", "branco" , False)
c3 = Cachorro('Scooby', 'Branco e Preto')
c1.falar()
print(c1)
print(c2)
print(c3)  # Imp    rimindo a segunda instância criada
