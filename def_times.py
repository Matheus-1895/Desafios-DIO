def adicionar_time(times, nome_time):
    times.append(nome_time)
    print(f'O time {nome_time} foi adicionado ao campeonato.')

times = []

def ver_times(times):
    print('\nTimes do Campeonato:')
    for indice, time in enumerate(times, start=1):
        print(f'-{indice}. {time}')

while True:
    print('1. Adicionar times:')
    print('2. Ver times:')
    print('0. Sair')

    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        nome_time = input('Digite o nome de um time: ')
        adicionar_time(times, nome_time)
    elif escolha == '2':
        ver_times(times)
    elif escolha == '0':
        break
    else:
        print('Escolha inválida. Tente novamente.')



