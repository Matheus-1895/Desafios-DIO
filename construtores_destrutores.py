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


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

def __str__():
    return f"{self.__clas__.__name__}: {''.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


c = Cachorro("Chappie", "amarelo")
c.falar()
print(c)

print("Ola mundo")

