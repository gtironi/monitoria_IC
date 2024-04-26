[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/L0wh9Moz)
# Minerando Textos no Terminal
Atividade prática do curso de Introdução à Computação.

Usando sed e outras ferramentas do terminal, o aluno deve manipular e minerar arquivos de texto, além de se familiarizar com o uso de regex e paths.

## Descrição
Seu objetivo é resolver todas as tarefas usando apenas recursos do terminal, Bash no Linux e GitBash no Windows. 

Coloque cada solução em um **script shell separado**, que já está criado (vazio) na pasta 'Solução' com os nomes `ex_1.sh`, `ex_2.sh`, etc.

Cada um destes scripts, quando executado, deve escrever a resposta em um arquivo chamado `resposta_ex_1`, `resposta_ex_2`, e assim por diante. 

## Exercícios
Na pasta *Dados* está a obra completa de Machado de Assis na forma de vários arquivos de texto, distribuídos em vários sub-diretórios.

1. Quantas palavras tem a obra completa?
   - Dica: Experimente concatenar todos os arquivos em um só para facilitar a contagem.
2. Liste os títulos de todas as obras (todas as pastas), em ordem alfabética.
3. Agora, liste somente os contos (seus títulos) em ordem cronológica de publicação. O resultado deve ser algo como:

```
Conto, Contos Fluminenses, 1870
Conto, Historias da Meia-Noite, 1873
...
```
4. Utilizando o conto `macn001.txt` , liste as palavras distintas que aparecem nele em ordem crescente de frequência, precedidas do número de ocorrências de cada uma. 
   - Dica 1: Para facilitar comece colocando cada palavra em uma linha separada:
   ```bash
   $ echo "gato sapato" | sed 's/ /\n/g'
   ```
   No código acima, a expressão regular `s/ /\n/g` substitui todos os espaços por quebras de linha (`\n`).
   - Dica 2: Quando tratamos texto, o computador vê qualquer alteração na string como uma palavra completamente diferente, como é o caso das letras maiúsculas e minúsculas, ou palavras acompanhadas de pontuação. Utilize os comandos `tr` e `sed` para **uniformizar** o texto.
   - Dica 3: Utilize os comandos `sort` e `uniq`.
   
O resultado deve ser algo como:
```
6 romance
6 rompeu
6 rosto
...
```
5. Repita o que foi feito no exercício anterior, mas agora para todas as obras. Lembre-se das dicas dadas nas outras questões!
6. Usando o resultado do exercício anterior, liste apenas as palavras que aparecem mais de 1000 vezes. 
   - Dica: Considere a seguinte linha de código para o pipeline desse exercício: `grep -E "^ *[[:digit:]]{4}"`; 
 
[Dicas de grep](https://github.com/fccoelho/introcomp/blob/main/conte%C3%BAdo/Introdu%C3%A7%C3%A3o%20%C3%A0%20programa%C3%A7%C3%A3o/GREP.md).
   
## Entrega
Coloque os scripts com as suas soluções e os arquivos de resposta no diretório `Solução` deste repositório. ao final, não esqueça de fazer um commit e um push.
