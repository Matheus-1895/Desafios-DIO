# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_mensal):
    # TODO: Crie uma Estrutura Condicional para verificar o consumo médio mensal 
    # TODO: Retorne o plano de internet adequado:
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif 10 < consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    elif consumo_mensal > 20:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."
    else:
        return "Consumo inválido. Por favor, insira um valor numérico válido."

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira o consumo médio mensal de dados em GB: "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

