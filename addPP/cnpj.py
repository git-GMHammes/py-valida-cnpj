import re
#
REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = limpaCNPJ(cnpj)
    print(f'\n\t re.sub(r"[^0-9]", "", cnpj) {cnpj}\n')
    if invalSequencia(cnpj):
        print(f'\n\t Você não pode digitar uma sequência!!')
        return False
    novoCNPJ = calculaCNPJ(cnpj=cnpj, digito=1)
    print(f'Novo CNPJ: {novoCNPJ}')
    novoCNPJ = calculaCNPJ(cnpj=novoCNPJ, digito=2)
    print(f'Novo CNPJ: {novoCNPJ}')
    if novoCNPJ == cnpj:
        print(f'\n\t {novoCNPJ} == {cnpj} Válido')
    else:
        print(f'\n\t {novoCNPJ} == {cnpj} Inválido')


def calculaCNPJ(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]  # Começa da posição 1 da lista
        novoCNPJ = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novoCNPJ = cnpj
    else:
        return None
    #
    total = 0
    for indice, regressivo in enumerate(regressivos):
        # print(f'{indice, cnpj[indice], regressivo}')
        # int() para converter em inteiro
        total += int(cnpj[indice]) * regressivo
        print(f'\t total += cnpj[indice] * regressivo')
        print(
            f'\t {total} += {cnpj[indice]} * {regressivo} = {regressivo * int(cnpj[indice])}')
    print(f'\n total: {total}\n')
    digito = 11 - (total % 11)
    print(f'digito: {digito}')
    digito = digito if digito <= 9 else 0
    print(f'digito: {digito}')
    return f'{novoCNPJ}{digito}'


def invalSequencia(cnpj):  # invalida sequência
    sequencia = cnpj[0] * len(cnpj)
    print(f'\n\t cnpj[0] * len(cnpj) {sequencia}\n')
    if sequencia == cnpj:
        return True
    else:
        return False


def limpaCNPJ(cnpj):
    # expressão regular que retorna apenas numeros
    return re.sub(r'[^0-9]', '', cnpj)
