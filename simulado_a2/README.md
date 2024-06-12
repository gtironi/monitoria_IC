### 1 - Questão de leitura de arquivo

**Descrição:**

Escreva um programa em Python que leia um arquivo de texto e conte o número total de palavras contidas nele. O programa deve considerar as palavras independentemente de diferenças entre maiúsculas e minúsculas e deve ignorar pontuações.

**Requisitos:**
- O programa deve solicitar ao usuário o nome do arquivo.
- Deve remover pontuações e transformar todas as palavras para letras minúsculas.
- Deve contar e exibir o número total de palavras.

**Exemplo de Entrada:**
```
Nome do arquivo: exemplo.txt
```
**Exemplo de Saída:**
```
Número total de palavras: 42 palavras
```

### 2 - Verificação de matriz identidade

**Descrição:**

Escreva um programa em Python que receba uma matriz quadrada de ordem `n` e determine se ela é uma matriz de identidade. Uma matriz de identidade é uma matriz quadrada em que todos os elementos da diagonal principal são 1 e todos os outros elementos são 0.

**Requisitos:**
- O programa deve solicitar ao usuário o tamanho `n` da matriz.
- O programa deve solicitar ao usuário os elementos da matriz.
- O programa deve verificar se a matriz é uma matriz de identidade e imprimir o resultado.

**Exemplo de Entrada:**
```
Tamanho da matriz: 3
Matriz:
[[1 0 0],
[0 1 0],
[0 0 1]]
```
**Exemplo de Saída:**

```
A matriz é uma matriz de identidade.
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

### 4 - Complete o Código

A função abaixo deve reorganizar os elementos de uma lista em uma matriz com as dimensões dadas. Por exemplo, dada a lista  $L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$, a chamada $v2m(L, 5, 2)$ retorna a matriz:

$
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]] 
$

Já a chamada $v2m(L, 2, 5)$ retorna a matriz:

$
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]] 
$

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
    - B) `v[num_col*j + i]`
    - C) `v[num_lin*i + j]`
    - D) `v[num_lin*j + i]`

2. M.append(__________)
    - A) `v`
    - B) `linha`
    - C) `num_lin`
    - D) `num_col`