tabuleiro = [['A','B','.','A','D','A','D','C','D','B','B','A','A','.','.','B','A','C','D','D','.','.','.','D','A','D','B','C','B','.'],
    ['D','A','D','A','B','B','.','B','C','C','D','.','A','B','A','.','D','C','.','B','C','A','A','B','C','D','.','B','A','D'],
    ['C','B','A','C','.','.','B','D','A','.','D','D','.','C','A','B','A','A','A','.','.','A','D','B','B','D','.','C','.','.'],
    ['B','.','D','.','C','C','C','B','.','.','C','D','C','D','A','B','.','.','C','A','.','B','C','C','B','.','C','B','.','A'],
    ['D','C','.','.','A','D','B','.','A','D','.','.','A','C','B','A','A','A','B','A','.','A','.','.','A','C','A','D','.','B'],
    ['B','B','.','.','A','B','A','.','C','C','C','B','A','C','.','.','.','.','A','.','.','C','A','.','B','.','.','.','D','C'],
    ['C','.','B','A','C','A','.','.','.','D','C','C','A','.','D','.','B','B','.','C','D','A','D','A','.','C','B','C','.','B'],
    ['D','.','.','B','A','B','C','D','.','.','.','D','B','C','A','.','.','A','.','.','C','.','D','C','A','C','.','D','C','C'],
    ['B','.','C','D','C','B','.','C','C','B','A','D','D','.','.','B','A','.','B','B','D','D','D','.','D','C','.','C','C','B'],
    ['C','.','C','B','C','.','.','.','D','.','D','A','.','A','.','B','C','A','B','A','B','.','.','C','A','C','C','D','.','B'],
    ['D','.','A','D','.','A','.','.','D','.','.','B','D','A','A','C','.','B','D','B','A','B','D','.','A','.','C','B','C','.'],
    ['B','.','.','B','.','C','.','B','A','D','D','A','A','.','B','A','C','B','D','.','C','.','A','D','.','A','D','D','D','.'],
    ['C','.','.','.','.','.','C','.','A','.','.','A','.','B','C','C','.','.','C','C','.','D','C','C','C','.','.','B','.','.'],
    ['.','.','.','.','.','D','D','.','.','C','D','D','B','.','C','D','A','B','.','.','C','.','.','.','.','.','A','D','C','C'],
    ['A','C','D','B','C','A','C','B','D','B','D','A','A','.','C','A','.','.','B','.','A','B','A','.','.','D','.','A','D','.'],
    ['.','C','.','.','B','.','D','.','B','D','C','C','.','D','.','B','D','A','D','.','D','D','C','A','.','.','A','C','A','.'],
    ['A','C','.','B','C','D','.','C','.','B','.','.','.','.','.','.','B','B','A','B','C','D','.','D','.','.','.','D','A','B'],
    ['A','B','A','.','D','.','B','C','.','C','D','A','B','.','C','.','.','.','D','.','C','.','D','.','C','.','.','.','.','.'],
    ['.','D','D','C','B','D','A','B','.','.','D','.','D','D','D','.','.','D','.','.','C','D','.','.','.','C','.','C','A','A'],
    ['.','C','.','.','.','.','B','.','.','B','C','D','B','B','.','B','A','.','A','D','D','B','.','D','B','D','.','.','B','C'],
    ['B','A','A','D','A','.','.','D','A','B','.','D','.','.','A','.','B','A','A','.','.','.','C','A','A','A','.','B','A','.'],
    ['.','D','B','D','C','D','C','.','B','A','.','.','C','B','A','.','.','B','.','.','D','C','D','.','B','C','C','B','B','A'],
    ['C','C','B','.','C','A','C','.','A','C','A','A','C','A','B','C','A','D','B','.','A','.','A','.','D','C','.','D','B','D'],
    ['D','B','C','B','.','B','.','B','C','.','.','.','.','C','A','D','A','A','.','D','C','B','D','A','.','.','C','D','D','.'],
    ['C','.','D','D','C','B','C','.','.','D','.','.','C','D','D','A','.','.','.','.','.','A','.','C','C','C','.','B','A','A'],
    ['B','B','.','B','.','.','.','.','D','D','A','A','.','B','A','A','.','D','B','.','.','.','C','.','B','A','B','B','C','B'],
    ['D','D','A','.','C','C','.','D','.','C','.','C','B','A','B','.','.','A','A','A','.','B','D','.','C','.','C','.','B','C'],
    ['B','D','A','A','A','.','B','.','C','A','.','C','D','B','.','C','B','.','B','A','C','B','A','A','B','D','B','C','.','B'],
    ['.','.','.','A','B','D','.','.','A','C','B','D','.','B','D','B','C','D','A','B','B','A','B','D','D','.','.','.','C','D'],
    ['B','.','.','D','D','B','D','.','D','B','D','B','A','D','C','A','A','A','D','.','D','D','.','C','D','.','.','B','C','A']]


alguem_venceu = False

for letra in ["A", "B", "C", "D"]:
    for linha in tabuleiro:
        for i in range(len(linha)-3):
            if linha[i] == linha[i+1] == linha[i+2] == linha[i+3] == letra:
                alguem_venceu = True

    num_coluna = len(tabuleiro[0])

    for j in range(num_coluna):
        coluna = []
        #construindo a coluna
        for linha in tabuleiro:
            coluna.append(linha[j])

        #verificando se tem 3 iguais
        for m in range(len(coluna)-3):
            if coluna[m] == coluna[m+1] == coluna[m+2] == linha[m+3] == letra:
                alguem_venceu = True

    print(f"Para a letra {letra} o resultado foi {alguem_venceu}")

    if alguem_venceu == True:
        print(f"O vencedor foi o jogador {letra}")
        break


print(alguem_venceu)


"""
todos_tem3 = False

for letra in ["A", "B", "C", "D"]:
    para_letra = False
    for linha in tabuleiro:
        for i in range(len(linha)-2):
            if linha[i] == linha[i+1] == linha[i+2] == letra:
                para_letra = True

    num_coluna = len(tabuleiro[0])

    for j in range(num_coluna):
        coluna = []
        #construindo a coluna
        for linha in tabuleiro:
            coluna.append(linha[j])
        
        #verificando se tem 3 iguais
        for m in range(len(coluna)-2):
            if coluna[m] == coluna[m+1] == coluna[m+2] == letra:
                para_letra = True

    print(f"Para a letra {letra} o resultado foi {para_letra}")

    if para_letra == False:
        break

    if (letra == "D" and para_letra == True):
        todos_tem3 = True


print(todos_tem3)
"""


"""
numero_de_jogadas = 0

for linha in tabuleiro:
    for elemento in linha:
        if elemento == "B":
            numero_de_jogadas += 1

print(numero_de_jogadas)
"""


'''
coluna4 = []
quantidade_de_vazios = 0

for linha in tabuleiro:
    if linha[3] == '.':
        quantidade_de_vazios += 1


print(quantidade_de_vazios)
'''

