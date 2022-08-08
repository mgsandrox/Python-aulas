for c in range(0, 6): # Laço de repetição normal
    print(c)
print('FIM')

for c in range(0, 7, 2):# Acrescentando mais 1 numero a contagem do laço vai pulando o numero inserido
    print(c)
print("FIM")

n = int(input('Digite um valor: '))# Utiliza uma variavel para inserir o valor que o laço ira fazer a contagem
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))# Inclusão de um laço com variaveis
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):# É adicionado o " +1 " para chegar a um resultado que deseja, pois por padrão iria de 0 a 9 não de 0 a 10
    print(c)
print('FIM')

for c in  range(0, 4):
    n = int(input('Digite um valor: '))# Uma variavel dento de um laço, que irá se repetir até o fim do laço
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))# Usando um laço para somar com variaveis
    s += n
print(f'O somatorio de todos os valores foi {s}')