### 1 - Questão de leitura de arquivo

**Descrição:**

Escreva um programa em Python que leia um arquivo de texto e conte o número total de palavras contidas nele. O programa deve considerar as palavras independentemente de diferenças entre maiúsculas e minúsculas e deve ignorar pontuações.

**Requisitos:**
- O programa deve solicitar ao usuário o nome do arquivo.
- Deve remover pontuações e transformar todas as palavras para letras minúsculas.
- Deve contar e exibir o número total de palavras.
- 

**Exemplo de Entrada:**
```
Nome do arquivo: exemplo.txt
```
**Exemplo de Saída:**
```
Número total de palavras: 42 palavras
```

### 2 - Jogo da Velha

Escreva uma função em Python que determine o resultado de um jogo da velha em uma matriz 3x3. A função deve retornar:

- `-1` se houve empate ou se ninguém venceu,
- `0` se o vencedor foi 'X',
- `1` se o vencedor foi 'O'.

A matriz será representada por uma lista de listas com os caracteres 'X', 'O', como o exemplo abaixo:

```
[[X O O],
[O X O],
[X O X]]
```

*Obs: A função sempre receberá um tabuleiro completo, isto é, não haverá espaços vazios na matriz.*

Complete o código abaixo:

```python
def verificar_vencedor(tabuleiro):
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2]:
            #complete aqui
    
    # Verifica colunas
    for i in range(3):
        if #complete aqui :
            #complete aqui
    
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        #complete aqui
    if #complete aqui :
        #complete aqui
    
    return #complete aqui
```

### 3 - Matriz - Soma dos elementos da diagonal secundária

Dada uma matriz quadrada $n \times n$, escreva uma função que calcula a soma dos elementos da diagonal secundária. A diagonal secundária é composta pelos elementos que vão da posição superior direita (0, n-1) até a posição inferior esquerda (n-1, 0).

Qual das seguintes funções Python calcula corretamente a soma dos elementos da diagonal secundária de uma matriz $n \times n$ representada por uma lista de listas?

A)
```python
def soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma
```

B)
```python
def soma_diagonal_secundaria(matriz):
    soma = 0
    n = len(matriz)
    for i in range(n):
        soma += matriz[i][n - i - 1]
    return soma
```

C)
```python
def soma_diagonal_secundaria(matriz):
    soma = 0
    n = len(matriz)
    for i in range(n):
        soma += matriz[n - i - 1][i]
    return soma
```

D)
```python
def soma_diagonal_secundaria(matriz):
    soma = 0
    n = len(matriz)
    for i in range(n):
        soma += matriz[n - i][i]
    return soma
```

E)
```python
def soma_diagonal_secundaria(matriz):
    soma = 0
    n = len(matriz)
    for i in range(1, n+1):
        soma += matriz[i][i]
    return soma
```

### 4 - Complete o Código

A função abaixo deve reorganizar os elementos de uma lista em uma matriz com as dimensões dadas. Por exemplo, dada a lista  $L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$, a chamada $v2m(L, 5, 2)$ retorna a matriz:

```
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]] 
```

Já a chamada $v2m(L, 2, 5)$ retorna a matriz:

```
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]] 
```

Complete as lacunas no código abaixo para que a função funcione corretamente.

```python
def v2m(v, num_lin, num_col):
    #Inicializa a matriz M como uma lista vazia
    M = []
    for j in range(num_lin):
        #Inicializa uma linha vazia
        linha = []
        for i in range(num_col):
            #Adiciona o elemento correto da lista v à linha
            linha.append(__________)
        #Adiciona a linha completa à matriz M
        M.append(__________)
    return M
```

Complete as lacunas com as opções corretas:

1. linha.append(__________)
    - A) `v[j*num_col + i]`
    - B) `v[num_col*i + j]`
    - C) `v[num_lin*i + j]`
    - D) `v[num_lin*j + i]`

2. M.append(__________)
    - A) `v`
    - B) `linha`
    - C) `num_lin`
    - D) `num_col`

### 5 - Fatorial
Escreva uma função recursiva em Python que calcule o fatorial de um número inteiro positivo. O fatorial de um número $n$ é o produto de todos os números inteiros positivos de 1 até $n$.

A função deve ser chamada fatorial e receber um inteiro positivo $n$ como argumento. A função deve retornar o fatorial de $n$.

Complete o código abaixo:

```python
def fatorial(n):
    #coloque seu código aqui
```
