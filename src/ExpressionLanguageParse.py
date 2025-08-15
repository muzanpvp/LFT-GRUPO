import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *


def p_program(p):
    '''program : opt_require opt_globals opt_classes opt_modules opt_ code_functions opt_code'''

def p_opt_require(p):
    '''opt_require  :   require
                    |   empty'''

def p_opt_globals(p):
    '''opt_globals  :   global_declarations
                    |   empty'''

def p_opt_classes(p):
    '''opt_classes  :   classes_functions
                    |    empty'''


def p_empty(p):
    'empty :'
    pass

def p_delimiter(p):
    '''delimiter    :   NEWLINE
                    |   SEMICOLON
                    |   empty'''

def p_require(p):
    '''require    :   REQUIRE ID delimiter
                  |   REQUIRE STRING delimiter'''
    
def p_globals_declarations(p):
    '''globals_declarations :   globals
                            |   globals_declarations globals'''
def p_globals(p):
    '''globals  :   DOLAR_SIGN ID delimiter
                |   DOLAR_SIGN ID EQUALS expression delimiter '''
    
def p_classes(p):
    ''''''


def p_types(p):
    '''types    :   intenger
                |   float 
                |   boolean'''
    
def p_integer(p):
    '''interger :   INT
                |   INT8
                |   INT16
                |   INT32
                |   INT64
                |   INT128'''
    
def p_float(p):
    '''float    :   FLOAT
                |   FLOAT32
                |   FLOAT64'''
    
def p_boolean(p):
    'boolean    :   BOOL'


# Constrói o analisador léxico a partir das regras definidas
lexer = lex.lex()

# Constrói o analisador sintático a partir das regras definidas
parser = yacc.yacc()

# Exemplo de como usar o parser para analisar uma entrada
if __name__ == '__main__':
    data = '@ integer variavel ;' # Exemplo de código para testar
    result = parser.parse(data, lexer=lexer)
    print(result) # Imprime o resultado da análise (geralmente uma AST)



