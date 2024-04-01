#!/bin/bash

sed 's/ /\n/g' ../dados/machado/contos/macn001.txt | sed '/^[[:space:]]*$/d' | tr -d '[!"#$%&()*+,\./:;<=>?@[\]^_`{|}~]' | LC_ALL='C' sort -bdf  | uniq -i -c | LC_ALL='C' sort -rn -k 1 > resposta_ex_4.txt
