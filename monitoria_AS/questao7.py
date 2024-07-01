#with open("pedidos_produtos.csv", "r") as csv:

arquivo = open("pedidos_produtos.csv")
csv = arquivo.read()

lista_baguncada = csv.split("\n")

lista_baguncada_certa = lista_baguncada[1:len(lista_baguncada)-1]

matriz_pedidos = []

for pedido in lista_baguncada_certa:
    lista_pedido = pedido.split(",")
    matriz_pedidos.append(lista_pedido)

coluna_categoria = []

for linha in matriz_pedidos:
    coluna_categoria.append(linha[2])

coluna_categoria_set = set(coluna_categoria)
contagem_maior = 0
contagem_total = 0

for categoria in coluna_categoria_set:
    contagem_da_categoria = 0
    for linha in matriz_pedidos:
        if linha[2] == categoria:
            contagem_da_categoria += 1

    contagem_total += contagem_da_categoria
    if contagem_da_categoria > contagem_maior:
        maior_categoria = categoria
        contagem_maior = contagem_da_categoria

    print(f"A categoria {categoria} teve {contagem_da_categoria} pedidos")

print(maior_categoria)

"""
arquivo = open("pedidos_produtos.csv")
csv = arquivo.read()

lista_baguncada = csv.split("\n")

lista_baguncada_certa = lista_baguncada[1:len(lista_baguncada)-1]

matriz_pedidos = []

for pedido in lista_baguncada_certa:
    lista_pedido = pedido.split(",")
    matriz_pedidos.append(lista_pedido)

coluna_categoria = []

for linha in matriz_pedidos:
    coluna_categoria.append(linha[2])

coluna_categoria_set = set(coluna_categoria)
soma_maior = 0

for categoria in coluna_categoria_set:
    soma_da_categoria = 0
    for linha in matriz_pedidos:
        if linha[2] == categoria:
            soma_da_categoria += int(linha[3])

    if soma_da_categoria > soma_maior:
        maior_categoria = categoria
        soma_maior = soma_da_categoria

    print(f"A categoria {categoria} vendeu {soma_da_categoria}")

print(maior_categoria)
"""

"""
arquivo = open("pedidos_produtos.csv")
csv = arquivo.read()

lista_baguncada = csv.split("\n")

lista_baguncada_certa = lista_baguncada[1:len(lista_baguncada)-1]

matriz_pedidos = []

for pedido in lista_baguncada_certa:
    lista_pedido = pedido.split(",")
    matriz_pedidos.append(lista_pedido)

soma_valor = 0

for linha in matriz_pedidos:
    soma_valor += int(linha[3])
    

print(soma_valor)
"""

"""
arquivo = open("pedidos_produtos.csv")
csv = arquivo.read()

lista_baguncada = csv.split("\n")

lista_baguncada_certa = lista_baguncada[1:len(lista_baguncada)-1]

matriz_pedidos = []

for pedido in lista_baguncada_certa:
    lista_pedido = pedido.split(",")
    matriz_pedidos.append(lista_pedido)

coluna_pedidosid = []

for linha in matriz_pedidos:
    coluna_pedidosid.append(linha[1])

coluna_pedidosid_set = set(coluna_pedidosid)

print(len(coluna_pedidosid_set))
"""

"""
arquivo = open("pedidos_produtos.csv")
csv = arquivo.read()

#lista_baguncada = csv.strip("\n")

lista_baguncada = csv.split("\n")

lista_baguncada_certa = lista_baguncada[1:len(lista_baguncada)-1]

print(len(lista_baguncada_certa))
"""