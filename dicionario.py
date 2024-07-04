dados = {"nome": "Guilherme", "idade": 28}
dados = dict(nome="Guilherme", idade=28)
dados["telefone"] = "3333-1234" # ADICIONOU TELEFONE AO DICIONARIO {"nome": "Guilherme", "idade": 28,"telefone": "3333-1234"}


print(dados["nome"]) # "Guilherme"
print(dados["idade"])# 28
print(dados["telefone"]) # "3333-1234"

dados["nome"] = "Maria" #Alterou os dados do dicionario
dados["idade"] = 18
dados["telefone"] = "9988-1781"


print(dados["nome"]) # "MARIA"
print(dados["idade"])# 18
print(dados["telefone"]) # 9988-1781


contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos["giovanna@gmail.com"]["telefone"]) 

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)


contatos.clear() # LIMPAR tODO O DICIONARIO 
print(contatos)

contatos.fromkeys(["Cpf", ]) # {"Cpf": None}
contatos.fromkeys(["Cpf"], "vazio") # {"Cpf": "vazio"

