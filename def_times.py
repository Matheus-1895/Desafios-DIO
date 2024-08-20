def adicionar_time(times, nome_time):
    times.append(nome_time)
    print(f'O time {nome_time} foi adicionado ao campeonato.')

times = []

while True:
    print('1. Adicionar times:')
    print('2. Ver times:')
    print('0. Sair')

    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        nome_time = input('Digite o nome de um time: ')
        adicionar_time(times, nome_time)
    elif escolha == '2':
        if times:
            print('Times no campeonato:')
            for time in times:
                print(f'- {time}')
        else:
            print('Nenhum time foi adicionado ainda.')
    elif escolha == '0':
        break
    else:
        print('Escolha inválida. Tente novamente.')



