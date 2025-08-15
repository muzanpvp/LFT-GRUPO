
import ply.lex as lex


reservadas = {
    # Controle de Fluxo

    'if' : 'IF', 
    'else' : 'ELSE', 
    'elsif' : 'ELSIF', 
    'unless' : 'UNLESS',
    'case' : 'CASE', 
    'when' : 'WHEN', 
    'while' : 'WHILE', 
    'until' : 'UNTIL',
    'for' : 'FOR', 
    'break' : 'BREAK', 
    'next' : 'NEXT', 
    'yield' : 'YIELD',
    'return' : 'RETURN', 
    'do' : 'DO', 
    'then' : 'THEN', 
    'in' : 'IN',

    # Declaração e Definição

    'def' : 'DEF', 
    'class' : 'CLASS', 
    'module' : 'MODULE', 
    'struct' : 'STRUCT',
    'enum' : 'ENUM', 
    'union' : 'UNION', 
    'macro' : 'MACRO', 
    'abstract' : 'ABSTRACT',
    'alias' : 'ALIAS', 
    'include' : 'INCLUDE', 
    'require' : 'REQUIRE', 


    # Literais e Valores Especiais

    'true' : 'TRUE', 
    'false' : 'FALSE', 
    'nil' : 'NIL',
    'uninitialized' : 'UNINITIALIZED', 
  

    # Tipos, Operações e Metaprogramação

    'as' : 'AS', 
    'typeof' : 'TYPEOF', 
    'type' : 'TYPE', 
    'sizeof' : 'SIZEOF',
    'out' : 'OUT',
    'private' : 'PRIVATE', 
    'protected' : 'PROTECTED', 
    'of' : 'OF',

    # Blocos e Outros

    'begin' : 'BEGIN', 
    'end' : 'END', 
    'select' : 'SELECT',

    #Tipos
    'int'   :   'INT',
    'int8'  :   'INT8',
    'int16' :   'INT16',
    'int32' :   'INT32',
    'int64' :   'INT64',
    'int128':   'INT128',
    'float' :   'FLOAT',
    'float32' :   'FLOAT32',
    'float64' :   'FLOAT64',
    'bool'  :   'BOOL'

}

tokens = [
    'ID', 'STRING', 'CHAR', 'SYMBOL', 'VAR_GLOBAL', 'CLASS_VAR', 'INSTANCE_VAR', 'POTENCIACAO', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULTI_ASSIGN', 'DIVIDE_ASSIGN', 'MODULO_ASSIGN', 'PLUS', 'MINUS', 'MULTI', 'DIVIDE', 'MODULO', 'ASSIGN', 'TIPO_EQUAL', 'EQUAL', 'NOT_EQUAL', 'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN', 'AND', 'OR', 'NOT', 'SAFE_CALL' , 'TERNARIO', 'DOT', 'SCOPE', 'PASSA_ARGUMENTO', 'DEFINE_BLOCO', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON', 'COLON', 'ASSOCIACAO' , 'AT' 
] + list(reservadas.values())

#Não coloquei os operadores bit a bit 

t_POTENCIACAO      = r'\*\*'
# Os operadores com ASSIGN, seria os que realizar a operação e atribui(+=)
t_PLUS_ASSIGN      = r'\+='
t_MINUS_ASSIGN     = r'-='
t_MULTI_ASSIGN     = r'\*='
t_DIVIDE_ASSIGN    = r'/='
t_MODULO_ASSIGN    = r'%='
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_MULTI            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_ASSIGN           = r'='
# Igualdade estrita
t_TIPO_EQUAL       = r'==='  
t_EQUAL            = r'=='
t_NOT_EQUAL        = r'!='
t_LESS_EQUAL       = r'<='
t_GREATER_EQUAL    = r'>='
t_LESS_THAN        = r'<'
t_GREATER_THAN    = r'>'   
t_AND              = r'&&'
t_OR               = r'\|\|'
t_NOT              = r'!'
#Chamada segura do método
# t_SAFE_CALL        = r'\?\.' 
#t_TERNARIO         = r'\?'
#t_DOT              = r'\.'
t_SCOPE            = r'::'
# Operador para passar bloco como argumento 
t_PASSA_ARGUMENTO  = r'&'    
# Definição de bloco/lambda 
# t_DEFINE_BLOCO     = r'->'     
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_SEMICOLON        = r';'
t_COLON            = r':'
#É o operador usado para definir pares chave-valor em hashes. Da para entender com o (map) do java 
t_ASSOCIACAO       = r'=>'
t_AT               = r'@'

def t_FLOAT(t):
    r'([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][-+]?[0-9]+)?|[0-9]+[eE][-+]?[0-9]+'
    # Remove underscores e converte para float
    t.value = float(t.value.replace('_', ''))
    return t

def t_INTEGER(t):
    r'0x[0-9a-fA-F_]+|0o[0-7_]+|0b[01_]+|[0-9_]+'
    value = t.value.replace('_', '')
    if value.startswith('0x'):
        t.value = int(value, 16)
    elif value.startswith('0o'):
        t.value = int(value, 8)
    elif value.startswith('0b'):
        t.value = int(value, 2)
    else:
        t.value = int(value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|\\.)*?\"'
    return t

def t_CHAR(t):
    r"'([^'\\]|\\.)'"
    # Remove as aspas simples
    t.value = t.value[1:-1]
    return t

def t_SYMBOL(t):
    r':([a-zA-Z_]\w*|\"([^\\\n])*\"|\'([^\'\\])*\')'
    return t

def t_VAR_GLOBAL(t):
    r'\$[a-zA-Z_]\w*'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*[\!\?]?'
    # Verifica se é palavra reservada, substitui tipo do token
    t.type = reservadas.get(t.value , 'ID')
    return t

t_ignore = ' \t'

def t_COMMENT_BLOCK(t):
    # Ignora comentários de bloco
    r'\#\#\#(.|\n)*?\#\#\#'
    pass  

def t_COMMENT_SINGLE_LINE(t):
    # Ignora comentários de uma linha
    r'\#.*'
    pass 

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
entrada = ''
lexer.input(entrada)
for tok in lexer:
        print(tok)
