import ply.lex as lex
tokens = ("PLUS", "MINUS")
t_PLUS    = r'\+'
t_MINUS   = r'-'

t_ignore  = ' \t\n' #Ignora branco, tabulação e quebra de linha

lexer = lex.lex()
lexer.input("+\n  - --+\n +  +")
print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
  print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos)))