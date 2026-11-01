matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
def mostrar_tabuleiro(tabuleiro):
    maior = max(len(str(c)) for linha in tabuleiro for c in linha)

    for linha in tabuleiro:
        for coluna in linha:
            print(f"[{str(coluna):^{maior}}]", end='')
        print()
somaPares = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor para a linha {l}, coluna {c}: '))
        if matriz[l][c] %2==0:
            somaPares += matriz[l][c]
print(f'A soma dos valores pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print('O maior valor da segunda linha é:', max(matriz[1]))
mostrar_tabuleiro(matriz)