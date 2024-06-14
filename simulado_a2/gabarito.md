### Questão 1 - 
```
def contar_palavras(arquivo):
    pontuacoes = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '"', "'", '...']

    with open(arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()
    
    # Convertendo o texto em uma lista de caracteres
    lista_caracteres = list(texto)
    
    # Remover pontuações
    lista_caracteres_sem_pontuacao = [char for char in lista_caracteres if char not in pontuacoes]
    
    # Transformar a lista de volta em uma string
    texto_sem_pontuacao = ''.join(lista_caracteres_sem_pontuacao)
    
    # Transformar em minúsculas
    texto_sem_pontuacao = texto_sem_pontuacao.lower()
    
    # Dividir o texto em palavras
    palavras = texto_sem_pontuacao.split()
    
    # Contar o número total de palavras
    total_palavras = len(palavras)
    
    return total_palavras

nome_arquivo = input("Nome do arquivo: ")
total_palavras = contar_palavras(nome_arquivo)
print(f"Número total de palavras: {total_palavras}")
```

### Questão 2 - 
```
def verificar_vencedor(tabuleiro):
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2]:
            return 0 if linha[0] == 'X' else 1
    
    # Verifica colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]':
            return 0 if tabuleiro[0][i] == 'X' else 1
    
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return 0 if tabuleiro[0][0] == 'X' else 1
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return 0 if tabuleiro[0][2] == 'X' else 1
    
    return -1
```

### Questão 3 -
B)
```python
def soma_diagonal_secundaria(matriz):
    soma = 0
    n = len(matriz)
    for i in range(n):
        soma += matriz[i][n - i - 1]
    return soma
```


### Questão 4 -
1. A) `v[j*num_col + i]`

2. B) `linha`


### Questão 5 -
```
def fatorial(n):
    # Base da recursão: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * fatorial de (n - 1)
    else:
        return n * fatorial(n-1)
```
