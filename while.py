opcao = -1

while opcao != 0 or opcao < 3:
    opcao = int(input("[1] sacar \n[2] Extrato\n[0] Sair\n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Extrato retirado")
    elif opcao > 2:
        print("Opcao invalida, vsfd")
else:
    print("Tchau, até logo")