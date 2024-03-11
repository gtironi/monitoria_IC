head -qn1 ../Dados/machado/contos/*.txt | sed -E 's/(,|.)htm//g' | sed -E 's/,([0-9]{4})/, \1/g' | awk '{print $NF $0}' | LC_ALL=C sort -n | cut -d' ' -f2- > resposta_ex_3.txt

#head -qn1 ../Dados/machado/contos/*.txt: pega a primeira linha de todos os arquivos dentro da pasta contos
    #-q: parametro para não mostrar o cabeçalho
    #n1: parametro para pegar apenas a primeira linha

#sed -E 's/(,|.)htm//g': retira .htm e ,htm do final das linhas
    # -E: habilita o uso de Expressão regular estendidas
    # s/: indica que é para substituir
    # (,|.)htm: expressão regular a ser substituida
    # //: indica que deve substituir por nada (remover)
    # g: substituir todas, não só a primeira
    # 's/o que substituir/pelo que substituir/g'

#sed -E 's/,([0-9]{4})/, \1/g': substitui ,1983 por , 1983
    # -E: habilita o uso de Expressão regular estendidas
    # s/: indica que é para substituir
    # ,([0-9]{4}): expressão regular a ser substituida ,(4 digitos)
    # /, \1/: indica que deve substituir por , seguida por espaço e seguido pela ocorrencia a ser substituida
    # g: substituir todas, não só a primeira
    # 's/o que substituir/pelo que substituir/g'

# awk '{print $NF $0}': coloca a data no começo da linha para possibilitar o sort
    # $NF: ultima palavra da linha
    # $0: toda a linha

# LC_ALL=C sort -n: faz o sort de acordo com a data que está no começo
    # LC_ALL=C: muda a variável LC_ALL para C. 
    # -n: especifica que a ordenação deve ser numérica (considera todos os numeros seguidos)

# cut -d' ' -f2-: retira a data do começo
    # -d' ': indica que o delimitador é ' '
    # -f2-: indica que deve manter o segundo campo (depois do espaço)
