lista = [[],[]]
for n in range(7):
    lista[0].append(int(input(f'Digite o {n+1}º valor: ')))
for i in lista[0]:
    if i % 2 == 0:
        lista[1].append(i)
        lista[0].remove(i)
print(sorted(lista[1]))
print(sorted(lista[0]))