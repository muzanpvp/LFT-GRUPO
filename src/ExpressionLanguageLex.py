import ply.lex as lex
from tabulate import tabulate 
reservadas = {
    # Controle de Fluxo
    'if'    :   'IF', 
    'else'  :   'ELSE', 
    'elsif' :   'ELSIF', 
    'case'  :   'CASE', 
    'when'  :   'WHEN', 
    'while' :   'WHILE', 
    'until' :   'UNTIL',
    'break' :   'BREAK', 
    'next'  :   'NEXT', 
    'yield' :   'YIELD',
    'do'    :   'DO', 
    'then'  :   'THEN', 
    'in'    :   'IN',
    'unless'    :   'UNLESS',
    'return'    :   'RETURN', 

    # Declaração e Definicao
    'def'   :   'DEF', 
    'class' :   'CLASS', 
    'enum'  :   'ENUM', 
    'union' :   'UNION', 
    'macro' :   'MACRO', 
    'module'    :   'MODULE', 
    'struct'    :   'STRUCT',
    'include'   :   'INCLUDE', 
    'require'   :   'REQUIRE', 

    # Literais e Valores Especiais
    'true'  :   'TRUE', 
    'false' :   'FALSE', 
    'nil'   :   'NIL',
    'uninitialized' :   'UNINITIALIZED', 
    'as'    :   'AS', 
    'type'  :   'TYPE', 
    'out'   : 'OUT',
    'of'    :   'OF',
    'private'   :   'PRIVATE', 
    'protected' :   'PROTECTED', 
    'sizeof'    :   'SIZEOF',
    'typeof'    :   'TYPEOF', 

    # Blocos e Outros
    'begin' : 'BEGIN', 
    'end'   : 'END',
    'select'    : 'SELECT',

    # Tipos de Dados
    'Int'   :   'INT',
    'Int8'  :   'INT8',
    'Int16' :   'INT16',
    'Int32' :   'INT32',
    'Int64' :   'INT64',
    'Int128'    :   'INT128',
    'UInt8' :   'UINT8',
    'UInt16'    :   'UINT16',
    'UInt32'    :   'UINT32',
    'UInt64'    :   'UINT64',
    'UInt128'   :   'UINT128',
    'Float' :   'FLOAT',
    'Float32'   :   'FLOAT32',
    'Float64'   :   'FLOAT64',
    'Bool'  :   'BOOL'
}

tokens = [
    'ID', 'STRING', 'CHAR', 'SYMBOL', 'VAR_GLOBAL', 'CLASS_VAR', 'INSTANCE_VAR', 'POTENCIACAO', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULTI_ASSIGN', 'DIVIDE_ASSIGN', 'MODULO_ASSIGN',
    'PLUS', 'MINUS', 'MULTI', 'DIVIDE', 'MODULO', 'ASSIGN', 'TIPO_EQUAL', 'EQUAL', 'NOT_EQUAL', 'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN', 'AND', 'OR', 'NOT', 
    'SAFE_CALL', 'DOT', 'SCOPE', 'PASSA_ARGUMENTO', 'DEFINE_BLOCO', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE','COMMA', 'SEMICOLON', 'COLON', 'ASSOCIACAO', 'AT', 'DOLAR_SIGN', 'QMARK', 'DOTDOT' , 'DOTDOTDOT',
    'INTNUMBER', 'HEXNUMBER', 'BINNUMBER', 'OCTNUMBER', 'FLOATNUMBER' ,'NEWLINE', 'CONSTANT', 'GLOBALVAR', 'INSTANCEVAR', 'CLASSVAR','LOOP', 'EACH', 'PIPE', 'POTENCIACAO_ASSIGN', 'OR_ASSIGN', 'TCOLON', 'SHIFT_LEFT', 'SHIFT_RIGHT',
    'EXCLAMATION', 'TILDE', 'LITERAL', 'UNDERSCORE', 'ASTERISK' , 'INTERP_START' , 'INTERP_END'
] + list(reservadas.values())


# Operadores

t_POTENCIACAO      = r'\*\*'
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
t_TIPO_EQUAL       = r'==='  
t_EQUAL            = r'=='
t_NOT_EQUAL        = r'!='
t_LESS_EQUAL       = r'<='
t_GREATER_EQUAL    = r'>='
t_LESS_THAN        = r'<'
t_GREATER_THAN     = r'>'   
t_AND              = r'&&'
t_OR               = r'\|\|'
t_NOT              = r'!'
t_SCOPE            = r'::'
t_PASSA_ARGUMENTO  = r'&'     
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_SEMICOLON        = r';'
t_COLON            = r':'
t_ASSOCIACAO       = r'=>'
t_AT               = r'@'
t_DOLAR_SIGN       = r'\$'
t_QMARK            = r'\?'
t_DOT              = r'.'
t_DOTDOT           = r'\.\.'
t_DOTDOTDOT        = r'\.\.\.'
t_PIPE             = r'\|'
t_EXCLAMATION      = r'!'
t_TILDE            = r'~'
t_TCOLON           = r'\?'
t_SHIFT_LEFT       = r'<<'
t_SHIFT_RIGHT      = r'>>'
t_UNDERSCORE       = r'_'
t_ASTERISK          = r'\*'



def t_INTNUMBER(t):
    r'[0-9_]+'
    t.value = int(t.value.replace('_',''))
    return t

def t_FLOATNUMBER(t):
    r'([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][-+]?[0-9]+)?|[0-9]+[eE][-+]?[0-9]+'
    # Remove underscores e converte para float
    t.value = float(t.value.replace('_',''))
    return t

def t_BINNUMBER(t):
    r'0b[01_]+'
    t.value = int(t.value.replace('_',''), 2)
    return t

def t_OCTNUMBER(t):
    r'0o[0-7_]+'
    t.value = int(t.value.replace('_',''), 8)
    return t

def t_HEXNUMBER(t):
    r'0x[0-9a-fA-F_]+'
    t.value = int(t.value.replace('_',''), 16)
    return t

def t_STRING(t):
    r'\"([^\\\n]|\\.)*?\"'
    return t

def t_INTERP_START(t):
    r'\#\{'
    return t

def t_INTERP_END(t):
    r'\}'

def t_CHAR(t):
    r"'([^'\\]|\\.)'"
    t.value = t.value[1:-1]
    return t

def t_SYMBOL(t):
    r':([a-zA-Z_]\w*|\"([^\\\n])*\"|\'([^\'\\])*?\')'
    return t

def t_VAR_GLOBAL(t):
    r'\$[A-Z_]\w*'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*[\!\?]?'
    t.type = reservadas.get(t.value , 'ID')
    return t

def t_CONSTANT(t):
    r'[A-Z_][A-Z0-9_]*'
    return t

def t_GLOBALVAR(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_INSTANCEVAR(t): 
    r'\@[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_CLASSVAR(t):
    r'\@\@[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_ignore = ' \t'

def t_COMMENT_BLOCK(t):
    r'\#\#\#(.|\n)*?\#\#\#'
    pass

def t_COMMENT_SINGLE_LINE(t):
    r'\#.*'
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

#Inicializacao
lexer = lex.lex()

entrada= """
(0...5).each do |i|
  puts "Número: #{i}"
end

def greet(name = "World")
  puts "Hello #{name}"
end

x, y = 1, 2
a, b, c = [1, 2, 3]
i -= 1
}
"""
lexer.input(entrada)
tabela = []

# Função para calcular coluna
def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

for tok in lexer:
    coluna = find_column(entrada, tok)
    tabela.append([tok.type, tok.value, tok.lineno, tok.lexpos])

cabecalho = ["Token", "Lexema", "Linha", "Posição"]

print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))