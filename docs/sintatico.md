Documentação Sintática da linguaguem Crystal

1. Elementos Sintáticos.

Um programa em Crystal é composto por uma ou mais funções. Uma função Crystal apresenta sintaxe similar a Ruby.

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




