import ply.lex as lex
tokens = ("PLUS", "MINUS")
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'*'
t_DIVIDE  = r'/'
t_LPAREN  = r'('
t_RPAREN  = r')'
t_ignore  = ' \t' #Ignora branco, tabulação e quebra de linha

# Adiciona a função t_newline que atualiza a linha atual do analisador lexico.
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

lexer = lex.lex()
lexer.input("+\n  - --+\n +  +")
print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
  print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos)))