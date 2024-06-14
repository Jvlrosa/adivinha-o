import random

while True:
    numero = int(input('SE ACERTAR O NUMRO Q ESTOU PENSANDO VC GANHA, DIGITE SEU NUMERO AQUI: '))

    lista = ['0', '1', '2', '3', '4', '5']

    escolha_aleatoria = random.choice(lista)

    if str(numero) == escolha_aleatoria:
        print(f'PARABÉNS 👏👏👏. SUA ESCOLHA - {numero}, ESCOLHA DA MÁQUINA - {escolha_aleatoria}')
    else:
        print(f'INFELIZMENTE VOCÊ PERDEU 😔😔😔. SUA ESCOLHA - {numero}, ESCOLHA DA MÁQUINA - {escolha_aleatoria}')

    continuar = input('DESEJA TENTAR NOVAMENTE [S/N]: ').lower()
    if continuar != 's':
        break