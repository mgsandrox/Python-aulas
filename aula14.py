

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

'''n= 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')'''

'''#Loop com uma lista
carros = ["HRV", "Gol", "Agro", "Poche", "Fusca"]
i = 0;
tam = len(carros)

while  i < tam:
    print(carros[i])
    i += 1
print("\nFim do loop")'''

#Loop com lista e um for, buscando a informação do usuario
import os

carros = []
carro = input("Informe um modelo de carro: ")

while  carro != "-1":
    carros.append(carro)
    carro = input('Informe outro modelo: ')

os.system('cls')
for x in carros:
    print(x)
print("\nFim do loop")