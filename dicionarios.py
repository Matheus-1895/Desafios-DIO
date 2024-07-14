Times_estadios = {'Flamengo': 'Maracanã', 'Vasco' : 'São Januário', 'Botafogo' : 'Nilton Santos'}

estadio = Times_estadios['Flamengo']
print(estadio)
print(Times_estadios['Flamengo'])


for times in Times_estadios:
    print(times)

for times in Times_estadios:
    estadio = Times_estadios[times]
    print(estadio)

print(Times_estadios.values())
print(Times_estadios.keys())

#Times_estadios : ['Santos'] = 'Vila Belmiro'


for chave in Times_estadios:
    print(chave, Times_estadios[chave])

for chave, valor in Times_estadios.values():
    print(chave, valor)