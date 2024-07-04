frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

tupla = ("p", "y", "t", "h", "o", "n",)
tupla[2:]  # ("t", "h", "o", "n")
tupla[:2]  # ("p", "y")
tupla[1:3]  # ("y", "t")
tupla[0:3:2]  # ("p", "t")
tupla[::]  # ("p", "y", "t", "h", "o", "n")
tupla[::-1]  # ("n", "o", "h", "t", "y", "p")

carros = ("gol", "celta", "palio",)
for carro in carros:
    print(carro)


carros = ("gol", "celta", "palio",)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    print(carro)
