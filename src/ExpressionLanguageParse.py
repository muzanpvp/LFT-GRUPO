import ply.yacc as yacc
import ExpressionLanguageLex as lex 
reservadas = lex.reservadas

def p_program(p):
    '''program : opt_require opt_globals opt_classes code_functions'''

def p_opt_require(p):
    '''opt_require  :   require
                    |   empty'''

def p_opt_globals(p):
    '''opt_globals  :   global_declarations
                    |   empty'''

def p_opt_classes(p):
    '''opt_classes  :   class_functions
                    |    empty'''

def p_empty(p):
    'empty :'
    pass

def p_require(p):
    'require  : REQUIRE ID delimitador'