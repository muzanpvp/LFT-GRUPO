# Análise Léxica da Linguagem Crystal💎

Este documento detalha a fase de **análise léxica** (ou tokenização) para um compilador da linguagem de programação Crystal. O analisador léxico é o primeiro estágio do processo de compilação, responsável por ler o código-fonte caractere por caractere e agrupá-los em sequências significativas chamadas **tokens**. Cada token representa uma unidade atômica da linguagem, como palavras-chave, identificadores, operadores, literais, entre outros.

## 1. Introdução à Análise Léxica

A análise léxica é uma etapa fundamental na interpretação do código-fonte, pois transforma uma sequência bruta de caracteres em uma sequência estruturada de tokens. Esta sequência de tokens serve como entrada para a próxima fase do compilador: a análise sintática.

### 1.1 Responsabilidades do Analisador Léxico

O analisador léxico possui as seguintes responsabilidades principais:

- **Identificação de Lexemas**: Agrupar caracteres que aparecem lado a lado formando uma sequência significativa chamada lexema. O lexema é a ocorrência real de um token no código-fonte.
- **Classificação de Tokens**: Atribuir a cada lexema identificado um tipo ou categoria, como `KEYWORD` (palavra-chave), `IDENTIFIER` (identificador), `INTEGER_LITERAL` (literal inteiro), etc.
- **Remoção de Elementos Não Essenciais**: Descartar caracteres que não influenciam a estrutura do programa, como espaços em branco (espaços, tabulações, quebras de linha) e comentários.
- **Relato de Erros Léxicos**: Detectar e sinalizar sequências de caracteres que não correspondem a nenhum padrão válido de token na linguagem Crystal, permitindo que erros sejam identificados logo no início da compilação.

 ## 2. Tokens da Linguagem Crystal

A linguagem Crystal define vários tipos de tokens, cada um com suas próprias regras de formação. As informações a seguir são baseadas diretamente na **[documentação oficial do Crystal (versão 1.16)](https://crystal-lang.org/reference/1.16/index.html)**.


### 2.1 Palavras Reservadas 

Esta seção apresenta as palavras-chave da linguagem Crystal, divididas por categorias funcionais para facilitar a compreensão do seu uso.


## Controle de Fluxo

Palavras usadas para controlar o fluxo da execução do programa, como condicionais, laços e retornos.

| Palavra-Chave | Palavra-Chave | Palavra-Chave | Palavra-Chave |
|---------------|---------------|---------------|---------------|
| `if`          | `else`        | `elsif`       | `unless`      |
| `case`        | `when`        | `while`       | `until`       |
| `for`         | `break`       | `next`        | `yield`       |
| `return`      | `do`          | `then`        |               |

---

## Declaração e Definição

Palavras utilizadas para declarar métodos, classes, módulos, macros, enums, e outras construções do programa.

| Palavra-Chave    | Palavra-Chave   | Palavra-Chave | Palavra-Chave |
|------------------|-----------------|---------------|---------------|
| `def`            | `class`         | `module`      | `struct`      |
| `enum`           | `union`         | `macro`       | `abstract`    |
| `alias`          | `include`       | `extends`     | `require`     | 
| `rescue`         | `ensure`        |               |               |

---

## Literais e Valores Especiais

Palavras que representam valores fixos, especiais ou referências ao contexto atual do programa.

| Palavra-Chave | Palavra-Chave | Palavra-Chave | Palavra-Chave    |
|---------------|---------------|---------------|------------------|
| `true`        | `false`       | `nil`         | `uninitialized`  |
| `self`        | `super`       |               |                  |

---

## Tipos, Operações e Metaprogramação

Palavras relacionadas a tipos, operações especiais e metaprogramação.

| Palavra-Chave          | Palavra-Chave           | Palavra-Chave           | Palavra-Chave         |
|------------------------|-------------------------|-------------------------|-----------------------|
| `as`                   | `typeof`                | `type`                  | `sizeof`     |
| `static_array_sizeof`  | `pointerof`             | `lib`                   | `out`                 |
| `private`              | `protected`             |                         |                       |

---

## Blocos e Outros

Palavras utilizadas para definição de blocos de código, seleções específicas e inserções inline.

| Palavra-Chave | Palavra-Chave | Palavra-Chave | Palavra-Chave |
|---------------|---------------|---------------|---------------|
| `begin`       | `end`         | `asm`         | `select`      |

---
> **Nota:** Palavras-chave são reservadas e não podem ser usadas para nomear variáveis, métodos, ou classes.


### 2.2 Identificadores 

Nomes definidos pelo programador para referenciar variáveis, métodos, classes, módulos, constantes, etc.

Regras:

- Devem começar com uma letra (a-z, A-Z) ou um sublinhado (_).
- Podem conter letras, dígitos (0-9) e sublinhados (_).
- São case-sensitive (distinguem maiúsculas de minúsculas).
- Variáveis Locais e Argumentos: começam com uma letra minúscula ou _.
- Constantes, Módulos e Classes: começam com uma letra maiúscula.
- Métodos: podem terminar convencionalmente com `!` (métodos que modificam o estado) ou `?` (métodos que retornam um booleano).
- Variáveis de Instância: começam com `@` (ex: `@nome_usuario`).
- Variáveis de Classe: começam com `@@` (ex: `@@contador_global`).
- Variáveis Globais: começam com `$` (ex: `$stdout`).

Exemplos:

```crystal
minha_variavel
NumeroMaximo
calcula_soma!
eh_vazio?
@idade
@@cache_total
$DEBUG

## 2.3 Literais

Literais representam valores fixos diretamente no código-fonte.

### Inteiros 

| Base        | Exemplos                   | Notas                                 |
|-------------|----------------------------|----------------------------------------|
| Decimal     | `123`, ou `1_000_000`      | Underscores são permitidos para melhorar a legibilidade |
| Hexadecimal | `0xAF`, `0xFF`             | Prefixo `0x`                          |
| Octal       | `0o755`, `0o123`           | Prefixo `0o`                          |
| Binário     | `0b1010`, `0b1111_0000`    | Prefixo `0b`                          |
| Tipagem     | `123i8`, `456u64`          | Sufixos para especificar tipo numérico |

### Ponto Flutuante 

| Tipo          | Exemplos                         | Notas                                 |
|---------------|----------------------------------|----------------------------------------|
| Decimal       | `3.14`, `-0.5`                   |                                        |
| Científica    | `1.0e-3`, `6.022_140_76e23`      | Notação científica                    |
| Tipagem       | `1.23f32`, `4.56f64`             | Sufixos para `Float32` ou `Float64`  |

### String

| Tipo         | Exemplos             | Observações                       |
|--------------|----------------------|-----------------------------------|
| Simples      | `"Olá, Mundo!"`      | Aspas duplas.                     |
| Escapadas    | `"Linha 1\nLinha 2"` | Suporta sequências de quebra de linha.     |
| Interpoladas | `"O valor é #(variavel)"` | Expressões combinadas com `#{}`. |
| HereDocs     | `<<-TEXT\nUm texto\nTEXT` | Strings multilinha delimitadas por identificadores. |

### Caracteres

| Tipo         | Exemplos          | Observações                      |
|--------------|-------------------|----------------------------------|
| ASCII/Unicode| `'a'`, `'@'`      | Delimitadas por aspas simples.   |
| Escape       | `'\n'`, `'\t'`, `'\u1234'` | Suporta quebras de linhas e Unicode.       |

### Símbolos

| Exemplos          | Observações                       |
|-------------------|-----------------------------------|
| `:nome`, `:"com-espaco"` | Representam nomes imutáveis únicos. |


### Booleanos 

| Exemplos          | Observações                       |
|-------------------|-----------------------------------|
| `true`            | `Verdadeiro`                      |
| `false`           | `Falso`                           |


### Nulo 

- `nil` representa ausência de valor.

### Arrays =

- Delimitados por colchetes: `[1, "dois", 3.0]`

### Hashes 

| Sintaxe                  | Exemplo                                 |
|--------------------------|------------------------------------------|
| Símbolos como chave      | `{nome: "Alice", idade: 30}`             |
| Strings ou valores mistos| `{"status" => "ativo"}`                 |

### Faixas 

| Tipo       | Exemplo       | Notas                                |
|------------|---------------|---------------------------------------|
| Inclusiva  | `1..5`        | Inclui o valor final (5)              |
| Exclusiva  | `0...100`     | Exclui o valor final (100)            |


---

## 2.4 Operadores

Operadores representam ações ou relações entre valores.

### Operadores Aritméticos

| Operador | Descrição           |
|----------|---------------------|
| `+`      | Soma                |
| `-`      | Subtração           |
| `*`      | Multiplicação       |
| `/`      | Divisão             |
| `%`      | Módulo (resto)      |
| `**`     | Exponenciação       |

### Operadores de Atribuição

| Operador | Descrição                         |
|----------|-----------------------------------|
| `=`      | Atribuição direta                 |
| `+=`     | Soma e atribui                    |
| `-=`     | Subtrai e atribui                 |
| `*=`     | Multiplica e atribui              |
| `/=`     | Divide e atribui                  |
| `%=`     | Módulo e atribui                  |
| `**=`    | Exponenciação e atribui           |

### Operadores de Comparação

| Operador | Descrição                        |
|----------|----------------------------------|
| `==`     | Igualdade                        |
| `!=`     | Diferença                        |
| `<`      | Menor que                        |
| `>`      | Maior que                        |
| `<=`     | Menor ou igual                   |
| `>=`     | Maior ou igual                   |
| `===`    | Comparação de identidade         |

### Operadores Lógicos Booleanos

| Operador | Descrição    |
|----------|--------------|
| `&&`     | E lógico     |
| `||`     | OU lógico    |
| `!`      | Negação      |

### Operadores Bit a Bit 

| Operador | Descrição          |
|----------|--------------------|
| `&`      | AND                |
| `|`      | OR                 |
| `^`      | XOR                |
| `~`      | NOT (inversão)     |
| `<<`     | Shift à esquerda   |
| `>>`     | Shift à direita    |

### Outros Operadores

| Operador | Uso                                                |
|----------|----------------------------------------------------|
| `.`      | Acesso a membros/métodos                           |
| `::`     | Acesso a constantes/módulos                        |
| `[]`     | Indexação                                          |
| `?:`     | Operador ternário (condição ? valor1 : valor2)     |
| `||=`    | Atribuição se nulo                                 |
| `?.`     | Chamada segura (verifica se não é nil)             |
| `*`      | Splat operator (Agrupar ou espalhar argumentos como array) |
| `&`      | Capturar bloco e tratá-lo como objeto              |

---

## 2.5 Comentários

### Linha Única

```crystal
# Este é um comentário de uma linha.
```

### Bloco/Documentação

```crystal
###
Este é um comentário de bloco.
Ele pode abranger várias linhas
e serve como documentação.
###
```

---

## 2.6 Separadores e Pontuação

| Símbolo   | Uso                                              |
|-----------|--------------------------------------------------|
| `(` `)`   | Parênteses para agrupar expressões               |
| `[` `]`   | Colchetes para arrays ou indexação               |
| `{` `}`   | Chaves para blocos ou hashes                     |
| `,`       | Separação de elementos                           |
| `;`       | Separação opcional de instruções                 |
| `:`       | Tipagem, símbolos ou pares chave:valor           |
| `=>`      | Hash rocket (associação chave-valor)             |
| `|`       | Definição de parâmetros em blocos                |

---

