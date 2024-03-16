# Monitoria IC

Bem-vindo ao nosso repositório de monitoria para a disciplina de Introdução à Computação!

Este espaço foi criado com o intuito de auxiliar os alunos da disciplina de Introdução à Computação, fornecendo recursos úteis, como arquivos e comandos relevantes, que podem ajudar no aprendizado e na prática dos conceitos abordados durante o curso.

Aqui, você encontrará uma variedade de materiais, desde documentos de apoio até exemplos práticos de uso de comandos de terminal e programas de computador. Nosso objetivo é proporcionar uma experiência de aprendizado enriquecedora e acessível para todos os alunos.

Fique à vontade para explorar os recursos disponíveis e utilize este repositório como uma ferramenta complementar aos seus estudos. Além disso, estamos abertos a sugestões e contribuições da comunidade acadêmica para tornar este espaço ainda mais útil e diversificado.

Assinado: ChatGPT

## mv - mover arquivo

```bash
mv [opções] origem destino
```

Para renomear o arquivo `teste.txt` para `teste2.txt`, digite:

```bash
mv teste.txt teste2.txt
```

Para mover o arquivo para o diretório pai, digite:
```bash
mv arquivo1 ../
```

## cp - copia arquivo

```bash
cp [opções] origem destino
```

Para criar uma cópia do arquivo `teste.txt` com o nome `teste_bak.txt`, digite:

```bash
cp teste.txt teste_bak.txt
```

## cat - junta arquivos

```bash
cat [OPÇÃO] [ARQUIVO]
```

Para mostrar todos os arquivos `.txt`, utilize:

```bash
cat *.txt
```

Para criar um novo arquivo com a junção dos arquivos existentes, utilize:

```bash
cat *.txt > junto.txt
```

## echo - escreve

Para escrever em um arquivo, utilize:

```bash
echo "Bem-vindo ao meu script de boas-vindas!" > escrita.txt
```

## wc - conta linhas, palavras e caracteres de arquivos

- `-c`: Conta o número de caracteres de um ou mais arquivos;
- `-l`: Conta o número de linhas de um ou mais arquivos;
- `-w`: Conta as palavras de um ou mais arquivos.


```bash
wc [opções] [arquivo]
```

Para contar o número de palavras no arquivo `junto.txt`, utilize:

```bash
wc -w junto.txt
```

## sed - ferramenta de processamento de texto

```bash
sed [opções] 'comando' arquivo(s)
```

Para substituir todas as ocorrências da palavra `palavra` por `substituicao` no arquivo `arquivo.txt`, utilize:

```bash
sed 's/palavra/substituicao/g' arquivo.txt
```

## grep - encontrar padrões em arquivos de texto

```bash
grep [opções] expressão arquivo
```

Parâmetros importantes:

- `-i`: Ignora a diferença entre letras maiúsculas e minúsculas.
- `-v`: Mostra todas as linhas do arquivo, exceto as que contêm a expressão.
- `-c`: Conta quantas ocorrências existem.

Para encontrar arquivos `.txt` no diretório atual, utilize:

```bash
ls | grep ".txt"
```

Para encontrar endereços de e-mail no arquivo `test-file`, utilize (EXPRESSÃO REGULAR INCORRETA):

```bash
grep -E '^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{2,}' email.txt
```

(EXPRESSÃO REGULAR CORRETA)

```bash
grep -E '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' email.txt
```

- `^`: Este símbolo indica que a correspondência deve começar no início da cadeia.
- `[a-zA-Z0-9._%+-]+`: Isso corresponde a um ou mais caracteres alfanuméricos, como `.`, `_`, `%`, `+`, ou `-`. Isso permite caracteres comuns em endereços de e-mail.
- `@`: Corresponde ao símbolo `@`.
- `[a-zA-Z0-9.-]+`: Isso corresponde a um ou mais caracteres alfanuméricos, como `.`, ou `-`. Isso permite o uso de subdomínios.
- `\.[a-zA-Z]{2,}`: Isso corresponde a um ponto seguido de dois ou mais caracteres alfabéticos. Isso garante que a parte do domínio tenha pelo menos duas letras, como `.com`, `.org`, `.edu`, etc.
- `$`: Este símbolo indica que a correspondência deve terminar no final da cadeia.

## chmod - tornar o arquivo executável

```bash
chmod +x arquivo
```
