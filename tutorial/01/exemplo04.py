import ply.lex as lex

# Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS", "ID")
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_ID = r'[A-Za-z]+'
t_ignore  = ' \t'

def t_newline(t): #Adiciona a função t_newline
     r'\n+'
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a
                                    #depender da quantidade de \n

# Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("+  - --+ +  +\nestada")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos)