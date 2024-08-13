nomes = []
i = 1

while i <= 5 :
    nome = str(input("Digite um nome:"))
    nomes.append(nome)
    i += 1

print(nomes)

#///////////////////////////////////////

n = int(input("Digite um numero"))

numero = 0

while numero <= n:
    print(numero)
    numero += 1

#///////////////////////////////////////

opcao = -1

while opcao != 0 and opcao < 3:
    opcao = int(input("[1] sacar \n[2] Extrato\n[0] Sair\n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Extrato retirado")
    elif opcao > 2:
        print("Opcao invalida, vsfd")
else:
    print("Tchau, até logo")

#///////////////////////////////////////

continuar = 's'

while continuar.lower() == 's':

    num1 = float(input('Digite um numero:'))
    num2 = float(input('Digite outro numero:'))
    resultado = num1 + num2
    print(f'O resoltado de {num1} + {num2} = {resultado}')

    continuar = (input('Deseja fazer uma operaçao?[S ou N]'))

#///////////////////////////////////////

funcionarios = []

while True:
    nome = input("Digite o nome da pessoa (ou digite '0' para terminar): ")
    
    if nome == "0":
        break
    
    funcionarios.append(nome)


print(funcionarios)
