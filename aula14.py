'''n = 1
while n != 0: Flag: é um ponto deparada
    n = int(input('Digite um valor: '))
print('FIM')'''

'''n = 1
r = 'S'
while n != 0: Flag: com outra condicinal
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('FIM')'''

n= 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')