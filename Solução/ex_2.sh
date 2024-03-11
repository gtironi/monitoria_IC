head -qn1 ../Dados/machado/*/*.txt | sed -E 's/(,|.)htm//g' | cut -d' ' -f2- | sort -bdf > resposta_ex_2.txt

#head -qn1 ../Dados/machado/*/*.txt: pega a primeira linha de todos os arquivos de todas as pastas dentro de machado
    #-q: parametro para não mostrar o cabeçalho
    #n1: parametro para pegar apenas a primeira linha

#sed -E 's/(,|.)htm//g': retira .htm e ,htm do final das linhas
    # -E: habilita o uso de Expressão regular estendidas
    # s/: indica que é para substituir
    # (,|.)htm: expressão regular a ser substituida
    # //: indica que deve substituir por nada (remover)
    # g: substituir todas, não só a primeira
    # 's/o que substituir/pelo que substituir/g'

# cut -d' ' -f2-: seleciona tudo depois do primeiro espaço em branco
    # -d' ': indica que o delimitador é ' '
    # -f2-: indica que deve manter o segundo campo (depois do espaço)

# sort -bdf: ordena as linhas
    # -b: ignora espaços em branco
    # d: considere apenas caracteres alfanuméricos e espaços
    # f: ignore diferenças entre letras maiúsculas e minúsculas
    