"""numeros = [5, 12, 8, 20, 3, 15]
for n in numeros:
    if n % 2 == 0:
        print(f'{n} é par')
        """
"""
numeros = [10, 20, 30, 40]
soma = 0
for n in numeros:
    soma += n
print(soma)
"""
"""
numeros = [17, 4, 23, 8, 4, 31, 55, 17, 0, 23, 10, 2]
maior = numeros[0]
menor = numeros[0]
soma_pares = 0
quantidade_impares = 0
quantidade_17 = 0
contador = 0
posicao23 = None
soma = 0
for n in numeros:
    #Maior e menor
    if n > maior:
        maior = n
    elif n < menor:
        msenor = n
    #Soma pares
    if n%2==0:
        soma_pares += n
    #quantidade Numeros impares
    else:
        quantidade_impares += 1
        if n == 17:
            quantidade_17 += 1
        elif n == 23 and posicao23 == None:
            posicao23 = contador
    contador += 1
    soma += n


print('O maior é:', maior)
print('O menor é:', menor)
print('A soma dos pares é:', soma_pares)
print('A quantidade de números impares é:', quantidade_impares)
print('A quantidade de 17 na lista é:', quantidade_17)
print('O indice do primeiro 23 é:', posicao23)
print('A média de todos os números é:', soma/len(numeros))
"""
"""
def maior(lista):
    num = lista[0]
    for n in lista:
        if n >= num:
            num = n
    return num
def menor(lista):
    num = lista[0]
    for n in lista:
        if n <= num:
            num = n
    return num
def media(lista):
    media = 0
    for n in lista:
        media+=n
    return media / len(lista)
def numerosAcimaDaMedia(lista, media):
    acimaDaMedia = 0
    for n in lista:
        if n > media:
            acimaDaMedia += 1
    return acimaDaMedia
def maiorNumeroPar(lista):
    listapares = []
    for n in lista:
        if n%2==0:
            listapares.append(n)
    maior = listapares[0]
    for n1 in listapares:
        if maior < n1:
            maior = n1
    return maior
def menorNumeroImpar(lista):
    listaImpares = []
    for n in lista:
        if n%2!=0:
            listaImpares.append(n)
    menor = listaImpares[0]
    for n1 in listaImpares:
        if n1 < menor:
            menor = n1
    return menor
def aparicoesMaiorNumero(lista):
    aparecimentoDoMaiorNumero = 0
    for n in lista:
        if n == maior(lista):
            aparecimentoDoMaiorNumero += 1
    return aparecimentoDoMaiorNumero

def primeiro_repetido_consecutivo(lista):
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            return lista[i]
    return None

numeros = [12, 7, 7, 3, 18, 21, 21, 21, 5, 9, 14, 14, 2, 30, 11,30]
print(f'O maior número é:{maior(numeros)}')
print(f'O menor número é:{menor(numeros)}')
print(f'A média de todos os números é:{media(numeros)}')
print(f'O número de pessoas acima da média:{numerosAcimaDaMedia(numeros,media(numeros))}')
print(f'O maior número entre os pares é:{maiorNumeroPar(numeros)}')
print(f'O menor número entre os impares é:{menorNumeroImpar(numeros)}')
print(f'O maior número aparece:{aparicoesMaiorNumero(numeros)}')
print(f'O primeiro número que se repete na lista é:{primeiro_repetido_consecutivo(numeros)}')

"""
"""
logs = ['log1', 'log2', 'log3']
def bufferDeslizante(lista,newLog=''):
    if len(lista) < 3:
        if newLog != '':
            lista.append(newLog)
    else:
        if newLog != '':
            del lista[0]
            lista.append(newLog)
    return lista
print(bufferDeslizante(logs))
print(bufferDeslizante(logs,'log4'))
def bufferDeslizante(lista,newLog=''):
    if newLog != '':
        if len(lista) < 3:
                lista.append(newLog)
        else:
                del lista[0]
                lista.append(newLog)
    return lista
"""
"""
from collections import deque

# Criamos um deque com tamanho máximo definido (maxlen=3)
# O próprio deque já gerencia o limite automaticamente!
logs = deque(['log1', 'log2', 'log3'], maxlen=3)

print(logs)  # deque(['log1', 'log2', 'log3'], maxlen=3)

# Adicionando um novo log. 
# Quando usamos append() em um deque com maxlen, ele automaticamente 
# descarta o elemento mais antigo do início se estiver cheio!
logs.append('log4')

print(logs)  # deque(['log2', 'log3', 'log4'], maxlen=3)
"""
notas_turma = [4.5, 7.0, 8.2, 5.0, 6.0, 9.5, 3.0]
"""
def processar_aprovados(notas):
    acima_da_media = []
    
    for n in notas:
        if n >= 6.0:
            acima_da_media.append(n)
            
    # Tratamento para evitar divisão por zero caso nenhum aluno seja aprovado
    if len(acima_da_media) == 0:
        return [], 0.0
        
    media = sum(acima_da_media) / len(acima_da_media)
    
    # Retornamos a lista e a média separadamente (em uma tupla)
    return acima_da_media, media

# Testando a função:
aprovados, media_turma = processar_aprovados(notas_turma)

print(f"Aprovados: {aprovados}")
print(f"Média dos aprovados: {media_turma:.2f}")
"""
"""
precos = [45.0, 120.5, 30.0, 15.0, 250.0, 89.9]
novosprecos = [n*0.9 for n in precos if n >= 50 ]
print(novosprecos)

matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
soma = 0
for linha in matriz:
    for coluna in linha:
        soma+=coluna
        print(coluna)
print(soma)
"""
pessoa = ['João', 17]
lista = [['Maria', 25], ['Pedro', 30]]
lista.append(pessoa[:])
print(lista)
print(pessoa)
del lista[2]
print(lista)
print(pessoa)