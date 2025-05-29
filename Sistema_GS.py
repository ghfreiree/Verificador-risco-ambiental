def info_user():
    while True:
        atributos = ['Nome', 'Localização']
        lista = []
        print('\nPor favor, preencha as suas informações.')
        nome = input('Nome: ')
        lista.append(nome)
        bairro = input('Bairro: ')
        lista.append(bairro)
        cidade = input('Cidade: ')
        lista.append(f', {cidade}')
        lista.append('')
        print('')
        y = 3
        x = 0
        for i in atributos:
            print(f'{i}: {lista[x]}{lista[y]}')
            y-=1
            x+=1

        while True:
            confirmacao = input('\nEssas informações estão corretas? (Sim ou não): ')
            if confirmacao.lower() == 'sim':
                break
            elif confirmacao.lower() == 'não' or confirmacao.lower() == 'nao':
                print('\nVamos tentar novamente.')
                break
            else:
                print('\nResposta inválida. Por favor, responda com "Sim" ou "Não".')
        if confirmacao.lower() == 'sim':
            print('Informações salvas com sucesso!')
            break
    return lista

def relevo():
    print('''
Relevo
1 - Planície baixa (região baixa)
2 - Plano inclinado (descida/subida)
3 - Planalto (região alta)
''')
    while True:
        relevo = int(input('Digite o número correspondente ao seu tipo de relevo: '))
        if relevo in [1, 2, 3]:
            break
        else:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
    return relevo

def precipitacao():
    print('-------------------------------------------------------------------------')
    print('''
Precipitação
1 - Seca
2 - Regular
3 - Muita chuva
''')
    while True:
        precipitacao = input('Digite o número correspondente ao seu tipo de precipitação: ')
        if precipitacao in ['1', '2', '3']:
            break
        else:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
    print('-------------------------------------------------------------------------')
    return precipitacao

def temperatura():
    print('''
Temperatura
1 - Fria
2 - Temperada
3 - Quente
''')
    while True:
        temperatura = input('Digite o número correspondente à temperatura da sua região: ')
        if temperatura in ['1', '2', '3']:
            break
        else:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
    print('-------------------------------------------------------------------------')
    return temperatura

def arborizacao():
    print('''
Arborização
1 - Baixa
2 - Alta''')
    while True:
        arborizacao = input('Digite o número correspondente à arborização da sua região: ')
        if arborizacao in ['1', '2']:
            break
        else:
            print('Opção inválida. Por favor, escolha 1 ou 2.')
    print('-------------------------------------------------------------------------')
    return arborizacao

def verif_enchente(nivelamento, chuva):
    if nivelamento == '1':
        if chuva == '3':
            return 'Alto'
        elif chuva == '2':
            return 'Médio'
        elif chuva == '1':
            return 'Baixo'
    elif nivelamento == '2':
        return 'Muito baixo'
    elif nivelamento == '3':
        if chuva == '3':
            return 'Baixo'
        elif chuva == '2':
            return 'Baixo'
        elif chuva == '1':
            return 'Muito baixo'

def verif_deslizamento(nivelamento, chuva):
    if nivelamento == '1':
        if chuva == '3':
            return 'Alto'
        elif chuva == '2':
            return 'Médio'
        elif chuva == '1':
            return 'Baixo'

def verif_queimadas(arvores, calor, chuva):
    if arvores == '1':
        if calor == '3':
            if chuva == '1':
                return 'Alto'
            elif chuva == '2':
                return 'Baixa'
            elif chuva == '3':
                return 'Muito baixo'
        elif calor == '2':
            if chuva == '1':
                return 'Baixo'
            elif chuva == '2':
                return 'Muito baixo'
            elif chuva == '3':
                return 'Muito baixo'
        elif calor == '1':
            if chuva == '1':
                return 'Muito baixo'
            elif chuva == '2':
                return 'Muito baixo'
            elif chuva == '3':
                return 'Muito baixo'
    elif arvores == '2':
        if calor == '3':
            if chuva == '1':
                return 'Alta'
            elif chuva == '2':
                return 'Média'
            elif chuva == '3':
                return 'Baixo'
        elif calor == '2':
            if chuva == '1':
                return 'Baixo'
            elif chuva == '2':
                return 'Muito baixo'
            elif chuva == '3':
                return 'Muito baixo'
        elif calor == '1':
            if chuva == '1':
                return 'Muito baixo'
            elif chuva == '2':
                return 'Muito baixo'
            elif chuva == '3':
                return 'Muito baixo'

def enchente(risco_enchente):
    print(f'\nO risco de enchente é na sua região é {risco_enchente}')
    print('As enchentes são mais propensas a ocorrer em regiões de planície baixa, pois a água sempre tende a descer. Outro fator que contribui para o risco de enchente é a precipitação, pois quanto mais chuva, maior o risco de alagamento.')
    print('Recomendações: É importante manter os bueiros limpos, evitar jogar lixo nas ruas e plantar árvores para ajudar a absorver a água da chuva. Além disso, é importante ter um plano de emergência caso você more em uma região de alto risco de enchentes.')

def deslizamento(risco_deslizamento):
    print(f'\nO risco de deslizamento é na sua região é {risco_deslizamento}')
    print('Os deslizamentos ocorrem geralmente em regiões de plano inclinado quando se tem muita chuva. Isso acontece porque a água da chuva causa a saturação e erosão do solo. Caso o solo dessa região não seja estável, ele acaba desmontando e causa o deslizamento das contruções instaladas sobre ele.')
    print('Recomendações: Para evitar passar por deslizamentos, é importante evitar terrenos em regiões de solo instável e plano inclinado. ')

def queimadas(risco_queimadas):
    print(f'\nO risco de queimadas naturais na sua região é {risco_queimadas}')
    print('Queimadas naturais são raras e ocorrem em condições específicas, como em regiões muito secas e quentes, onde há uma boa quantidade de vegetação para a chama se espalhar. Elas podem ser causadas também por raios ou outras fontes de ignição natural que são mais raras ainda de acontecer.')

def main():
    print('*-Bem-vindo ao Sistema de Avaliação de Riscos Ambientais!-*')
    info = info_user()
    nome = info[0]
    bairro = info[1]
    cidade = info[2]
    
    print('-------------------------------------------------------------------------------------------------------------------------')
    print(f'\n{nome}, agora vamos fazer um pequeno questionário para avaliar os riscos ambientais de {bairro}{cidade}')
    nivelamento = relevo()
    chuva = precipitacao()
    calor = temperatura()
    arvores = arborizacao()
    print('\n-------------------------------------------------------------------------------------------------------------------------')

    risco_enchente = verif_enchente(nivelamento, chuva)
    risco_deslizamento = verif_deslizamento(nivelamento, chuva)
    risco_queimadas = verif_queimadas(arvores, calor, chuva)

    enchente(risco_enchente)
    deslizamento(risco_deslizamento)
    queimadas(risco_queimadas)

main()