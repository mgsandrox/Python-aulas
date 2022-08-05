nome =  str(input('Qual o seu  nome? ')).strip().upper()
if nome == 'ALESSANDRO':
    print('Que nome gênial!!!')
elif nome == 'FELIPE' or nome =='HELBER' or nome == 'JACKSON':
    print('Que nome horrivel da molestia!')
elif nome == 'EMILY':
    print('Que nome lindo meu amor! \033[1;31m<3\033[m')
elif nome == 'BRUNA' or nome == 'MARTA' or nome == 'GEOVANA':
    print('É um nome legal!')
else:
    print(f'Muda esse nome {nome}! kkkkkk')