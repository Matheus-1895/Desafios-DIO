saldo = 0
limite_valor = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUE = 3

while True:

    opcao = int(input("""
----------MENU----------
    INSIRA SUA OPÇÃO:
[0] Sair
[1] Depositar
[2] Saque
[3] Extrato
"""))

    if opcao == 1:
        print("Você escolheu Depósito.")
        valor = float(input("Digite o valor do Depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito no valor de R${valor:.2f}\n"
            print("Depósito concluído com SUCESSO")
        else:
            print("Operação falhou. O valor do depósito deve ser maior que 0.")

    elif opcao == 2:
        if numero_saques >= LIMITE_SAQUE:
            print("Não é possível realizar o Saque:\nLIMITE DE SAQUES DIARIOS EXCEDIDOS(3)")
        else:
            print("Você escolheu Saque.")
            valor = float(input("Digite o valor do Saque: "))
            if valor > saldo:
                print("Não é possível realizar o Saque:\nO valor do Saque é maior que o Saldo atual da conta.")
            elif valor > limite_valor:
                print("Não é possível realizar o Saque:\nO valor do Saque é maior que o limite estipulado(R$ 500).")
            elif valor <= 0:
                print("Operação falhou. O valor do saque deve ser maior que zero.")
            else:
                saldo -= valor
                extrato += f"Saque no valor de R${valor:.2f}\n"
                numero_saques += 1
                print("Saque concluído com SUCESSO\n")
                print(f"Seu saldo atual é: {saldo:.2f}\n")

    elif opcao == 3:
        print("Você escolheu Extrato.\n")
        if not extrato:
            print("Não foram realizadas transações")
        else:
            print("EXTRATO".center(27))
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("OPERAÇÕES".center(29))
            print(extrato)
        
    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")   
