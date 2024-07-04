def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome): # É OBRIGATORIO DIZER O NOME DA HORA DE IMPRIMIR 
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"): # PODE OU NAO DIZER O NOME DA HORA DE IMPRIMIR . SE NAO EXPECIFICA-LO, VAI IMPRIMIR 'ANONIMO'
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")


def calcular_total(numeros):
    return sum(numeros)
    
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34])) # 64
print(retorna_antecessor_e_sucessor(10)) # (9, 11)



def salvar_carro(marca, modelo, ano, placa):# salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC1234"})
# Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234



def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in
    kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta-Feira", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)




def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):  #OQUE VEM ANTES DA / É OBRIGADO A COLOCAR O PARAMETROS POR POSIÇÃO
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # inválido


def criar_carro(*, modelo, ano, placa, marca, motor, combustivel): #OQUE VEM DEPOIS DO * É OBRIGADO A COLOCAR O PARAMETROS POR NOME
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # inválido


def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel): #MISTURA DAS DUAS FUNÇÕES
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # inválido


def somar(a, b): # FUNÇÃO DEF PARA CALCULAR A SOMA DE A e B
    return a + b

def exibir_resultado(a, b, funcao): # FUNÇÃO DEF PARA MONTAR E DAR VALORES DE A e B
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # CHAMA A FUNÇÃO DEF PARA CALCULAR A SOMA