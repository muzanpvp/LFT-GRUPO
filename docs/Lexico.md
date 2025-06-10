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
| `enum`           | `union`         | `macro`       | `fun`         |
| `abstract`       | `annotation`    | `alias`       | `include`     |
| `extend`         | `require`       | `rescue`      | `ensure`      |

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
| `as`                   | `typeof`                | `type`                  | `instance_sizeof`     |
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
