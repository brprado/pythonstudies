#VALIDAÇÃO DE GÊNERO/SEXO
print('-=-' * 6)
print('\033[33mVALIDAÇAÕ DE SEXO\033[m')
print('-=-' * 6)
sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
if sexo == 'M' or sexo == 'F':
    print('\033[32mOPÇÃO REGISTRADA COM SUCESSO!\033[m')
    exit()
if sexo != 'M' or sexo != 'F':
    while sexo != 'M' or sexo != 'F':
        sexo2 = str(input('\033[31mOPÇÃO INVÁLIDA\033[m. DIGITE [M ou F]: ')).strip().upper()[0]
        if sexo2 == 'M' or sexo2 == 'F':
            print('\033[32mOPÇÃO REGISTRADA COM SUCESSO!\033[m')
            exit()
