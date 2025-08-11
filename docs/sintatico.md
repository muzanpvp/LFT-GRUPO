Documentação Sintática da linguaguem Crystal

1. Elementos Sintáticos

Um programa em Crystal é composto por uma ou mais funções. Uma função Crystal apresenta sintaxe similar a Ruby.
O código em Crystal  começa diretamente com instruções no nível superior (top-level code), e o compilador automaticamente as executa na ordem em que aparecem.

```
program->ID |assign|funcao|
      funcao program
funcao->"def"ID""(""sigParams")" ""stm" "end"
``` 
Onde os dois primeiros ID se referem, respectivamente, ao token def, utilizado para a definição de uma função e o nome da função, singParams representa os argumentos da função. Por último temos stms que representam um ou mais comandos finalizados por um end. Na próxima seção será apresentado os comandos da linguagem Crystal. 

1.1 Comando da Linguagem Crystal

Com relação aos aceitos, Crystal lida apenas com comandos de expressôes, o comando de repetição while, for, o comando de condição if e o comando de retorn, conforme apresentado nas seguintes regras:

```
stms-> stm|stm stms

opcional-> ELSIF exp "then" stms "end" | ELSE stms"end" |λ

stm-> exp
   |WHILE"("exp")"stms"end"
   |WHILE exp stms"end"
   |FOR ID"in"exp"do"stms"end"
   |FOR ID"in" exp stms"end"
   |IF exp "then"stms"end"opcional
   |IF exp stms"end"opcional
   |IF"("exp")""then"stms"end"opcional
   |IF"("exp")"stms"end"opcional
   |return exp
```
O comando while inicia com a palavra reservada while, seguido por uma expressão envolvida entre parênteses. Adicionalmente, ele apresenta obrigatoriamente uma sequência de comandos, envolvidos por chaves.

O comando for inicia com a palavra reservada for, seguido por um identificador, a palavra reservada in e uma expressão. Em seguida, apresenta obrigatoriamente uma sequência de comandos, envolvidos por chaves.

O comando if inicia com a palavra reservada if, seguida por uma expressão, que pode ou não estar envolvida entre parênteses, e opcionalmente precedida pela palavra reservada then. Em seguida, apresenta obrigatoriamente uma sequência de comandos, encerrada pela palavra reservada end. Opcionalmente, pode conter cláusulas elsif ou else, cada uma acompanhada de sua própria sequência de comandos e também encerrada por end.

Quanto ao comando return ele inicia com a palavra reservada return, seguido por uma expressão. Ao seu final, é usado o delimitador

1.2 Expressôes em Crystal
Crystal dá suporte a expressoes aritméticas de soma, multiplicação, exponenciação, subtração, divisão e resto. Adicionalmente, também dá suporte e chamadas de função(call), atribuição de valores a variáveis(assing). Por fim, expressôes também podem ser números(NUM) e variáveis(ID). A sintaxe das expressôes Crystal é apresentada pela seguinte regra:

```
exp-> exp"+"exp|
      exp"*"exp|
      exp"-"exp|
      exp"/"exp|
      exp"**"exp|
      exp"%"exp|
      exp"=="exp|
      exp"==="exp|
      exp"!="exp|
      exp">"exp|
      exp">"exp|
      exp"<="exp|
      exp">="exp|
      exp"||"exp|
      exp"&&"exp|
      exp"!"exp|
      call|
      assign|
      NUM|
      ID|
      
```

1.2.1 Chamadas de Função e Atribuição

Crystal dá suporte a chamadas de função com e sem parâmetros. Um parâmetros de função pode ser qualquer expressão Crystal. Adicionalmente, Crystal permite atribuir valores a variávais, conforme regras apresentadas a seguir:

´´´
call-> ID"("sigParams")" |
       ID"("")"          |
       ID                |
       ID sigParams
sigParams-> exp","sigParams|
       exp
assign->ID"="exp      
```
2. Exemplos de Código
A seguir, alguns exemplos de código na Linguagem Crystal:

```
Sem paramêtros

def say_hello
  puts "Hello Penny!"
end

Com um paramêtros

def say_hello(recipient)
  puts "Hello #{recipient}!"
end

say_hello "World"
say_hello "Crystal"

Com argumento já determinando seu atributo 

def say_hello(recipient = "World")
  puts "Hello #{recipient}!"
end

say_hello
say_hello "Crystal"

Com argumento já determinando o tipo do atributo

def say_hello(recipient : String)
  puts "Hello #{recipient}!"
end

say_hello "World"
say_hello "Crystal"

Uso da Sobrecarga

def say_hello(recipient : String)
  puts "Hello #{recipient}!"
end

def say_hello(times : Int32)
  puts "Hello " * times
end

say_hello "World"
say_hello 3
```




