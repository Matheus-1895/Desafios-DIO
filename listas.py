carros = ["celta","gol", "kwid"]

for carros in carros:
    print(carros)


frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3] )

letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:] )# ["t", "h", "o", "n"]
print(lista[:2] )# ["p", "y"]
print(lista[1:3] )# ["y", "t"]
print(lista[0:3:2] )# ["p", "t"]
print(lista[::] )# ["p", "y", "t", "h", "o", "n"]
print(lista[::-1] )# ["n", "o", "h", "t", "y", "p"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


lista2 = []
lista2.append(1) # APPEND ADICIONA COISAS A LISTA
lista2.append("Python")
lista2.append([40, 30, 20])
print(lista2) 

linguagens = ["python", "js", "c"]
print(linguagens) # ["python", "js", "c"]
linguagens.extend(["java", "csharp"]) # ADICIONA MAIS DE UMA COISA A LISTA DE UMA VEZ SÓ
print(linguagens) # ["python", "js", "c", "java", "csharp"]

lista = [1, "Python", [40, 30, 20]]
print(lista) # [1, "Python", [40, 30, 20]]
lista.clear() # LIMPA A LISTA
print(lista) # []


lista3 = [1, "Python", [40, 30, 20]]
lista3.copy() # COPIA A LISTA 
print(lista3) # [1, "Python", [40, 30, 20]]


cores = ["vermelho", "azul", "verde", "azul"]
cores.count("vermelho") # DIZ QUANTAS VEZES CADA OBJETO APARECE NA LISTA
cores.count("azul")
cores.count("verde")

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.index("java") # DIZ QUAL A POSICAO QUE APARECE O OBJETO PELA PRIMEIRA VEZ QUE O OBJETO ESTA
linguagens.index("python") # 0

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.pop() # csharp REMOVE O ULTIMO ELEMENTO DA LISTA. A NÃO SER QUE PASSE O INDICE CORRETO DE QUAL QUER TIRAR
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c") # PARECIDO COM "POP" , POREM PASSAMOS O NOME CORRETO DO OBJETO UE SERA RETIRADO
print(linguagens) # ["python", "js", "java", "csharp"]


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse() # TA REVERSE NA LISTA 
print(linguagens) # ["csharp", "java", "c", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"] ORDENA DE ORDEM ALFABETICA OU ORDEM CRESCENTE
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"] ORDENA PELO TAMANHO DA PALAVRA
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"] 

linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens)) # 5 VE O TAMNHA DO LISTA 

linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]