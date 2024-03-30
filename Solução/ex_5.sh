#!/bin/bash

cat ../dados/machado/*/*.txt | sed 's/ /\n/g' | sed '/^$/d' | tr -d '[!"#$%&()*+,\./:;<=>?@[\]^_`{|}~]' | LC_ALL='C' sort -bdf  | uniq -i -c | LC_ALL='C' sort -rn -k 1 > resposta_ex_5.txt