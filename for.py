notas = []  # Lista para armazenar as notas

# Loop para coletar 5 notas
for i in range(5):
    nota = float(input("Escreva sua nota: "))  # Coletar a nota e convertê-la para float
    notas.append(nota)  # Adicionar a nota à lista

# Calcular a média das notas
media = sum(notas) / len(notas)

# Exibir a média das notas
print(f"Essa é a média das suas notas: {media}")

for numero in range(0,51,5):
    print(numero)