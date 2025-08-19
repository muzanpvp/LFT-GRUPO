import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *

#---------------------------------------------PROGRAM--------------------------------------------------------------
def p_program(p):
    '''program : opt_require opt_globals opt_classes opt_modules opt_ code_functions opt_code'''

#---------------------------------------------REQUIRE--------------------------------------------------------------

def p_opt_require(p):
    '''opt_require  :   require
                    |   empty'''
    
def p_require_declarations(p):
    '''require_declarations :   require
                            |   require NEWLINE require_declarations'''

def p_require(p):
    '''require    : REQUIRE STRING delimiter'''

#----------------------------------------------GLOBALS-------------------------------------------------------------

def p_opt_globals(p):
    '''opt_globals  :   globals_declarations
                    |   empty'''
    
def p_globals_declarations(p):
    '''globals_declarations :   globals
                            |   globals_declarations NEWLINE globals'''
def p_globals(p):
    '''globals  :   CONSTANT ASSIGN expression delimiter '''

#-----------------------------------------------CLASSES------------------------------------------------------------

def p_opt_classes(p):
    '''opt_classes  :   classes_functions
                    |    empty'''
    
def p_classes(p):
    ''''''
#-----------------------------------------------MODULES------------------------------------------------------------

def p_opt_modules(p):
    '''opt_modules : empty'''  

#-----------------------------------------------FUNCTIONS----------------------------------------------------------

def p_code_functions(p):
    '''code_functions : empty'''  

#----------------------------------------------------CODE----------------------------------------------------------
def opt_code(p):
    '''opt_code :  empty '''



#---------------------------------------------------OPERAND--------------------------------------------------------

def p_operand(p):
    '''operand  :   constant
                |   functionCall
                |   expParentheses'''
     
def p_constant(p):
    '''constant :   constant_integer
                |   constant_float
                |   constant_string
                |   constant_boolean
                |   constant_char
                |   constant_id'''

def p_constant_integer(p):
    '''constant_integer :   INTNUMBER
                        |   HEXNUMBER
                        |   BINNUMBER
                        |   OCTNUMBER'''

def p_constant_float(p):
    '''constant_float   :   FLOATNUMBER'''

def p_constant_string(p):
    '''constant_string  :   STRING'''

def p_constant_char(p):
    '''constant_char    :   CHAR'''

def p_constant_boolean(p):
    '''constant_boolean :   TRUE
                        |   FALSE'''
#Falta coisa
def p_constant_id(p):
    '''constant_id  :   ID
                   |    GLOBALVAR
                   |    INSTANCEVAR
                   |    CLASSVAR'''

def p_functionCall(p):
    '''functionCall :   ID LPAREN opt_arguments RPAREN'''
    
def p_opt_arguments(p):
    '''opt_arguments    :   arguments
                        |   empty'''

def p_arguments(p):
    '''arguments    :   expression
                    |   expression COMMA arguments'''    


def p_expParentheses(p):
    '''expParentheses   :   LPAREN expression RPAREN'''


#--------------------------------------------------STATEMENTS------------------------------------------------------
def p_statements(p):
    '''statements   :   expression
                    |   expression NEWLINE statements
                    |   control_structures
                    |   control_structures NEWLINE statements'''
    
def p_control_structures(p):
    '''control_structures : loop
                          | conditional
                          | case
                          | return'''
    
def p_conditional(p):
    '''conditional  :   if 
                    |   unless'''

def p_loop_structure(p):
    '''loop_structure   :   while
                        |   until
                        |   loop
                        |   iterator'''

def p_while(p):
    '''while_loop   :   WHILE expression statements_block'''

def p_until(p):
    '''until_loop   :   UNTIL expression statements_block'''

def p_loop(p):
    '''loop :   LOOP statements_block'''

def p_iterator(p):
    '''iterator :   expression DOT TIMES statements_block
                |   expression DOT EACH DO PIPE ID PIPE statements_block END
                |   expression DOT EACH LBRACE PIPE ID PIPE RBRACE block'''

#--------------------------------------------------CONDITIONS------------------------------------------------------

def p_if(p):
    '''if   :   IF expression statements_block opt_elseif opt_else END'''
    
def p_opt_elseif(p):
    '''opt_elseif   :   ELSEIF expression statements_block opt_elseif
                    |   empty'''
    
def p_opt_else(p):
    '''opt_else :   ELSE statements_block
                |   empty'''
    
def p_unless(p):
    '''unless   :   UNLESS expression statements_block opt_else END'''


def p_case(p):
    '''case :   CASE expression when_list opt_else END'''

def p_when_list(p):
    '''when_list    :   when_list WHEN expression statements_block
                    |   WHEN expression statements_block'''
   
def p_opt_blocks(p):
    '''opt_blocks   :   WHEN expression statements_block opt_else END
                    |   empty'''


#--------------------------------------------------CONTROL_FLOW----------------------------------------------------

def p_break(p):
    '''break_statement  :   BREAK expression
                        |   BREAK'''
    

def p_next(p):
    '''next_statement   :   NEXT expression
                        |   NEXT'''

def p_return_statement(p):
    '''return_statement :   RETURN expression
                        |   RETURN'''

#--------------------------------------------------EXPRESSIONS-----------------------------------------------------

def p_expression(p):
    '''expression : assignment_expression'''

def p_assignment_expression(p):
    '''assignment_expression    :   ID ASSIGN expression
                                |   ID PLUS_ASSIGN expression
                                |   ID MINUS_ASSIGN expression
                                |   ID MULTI_ASSIGN expression
                                |   ID DIVIDE_ASSIGN expression
                                |   ID MODULO_ASSIGN expression
                                |   ID POTENCIACAO_ASSIGN expression
                                |   ID OR_ASSIGN expression
                                |   ID AND_ASSIGN expression
                                |   multiple_assignment
                                |   ternary_expression'''
    

def p_multiple_assignment(p):
    '''multiple_assignment  :   ID COMMA ID ASSIGN expression COMMA expression
                            |   ID COMMA ID ASSIGN LBRACKET expression_list RBRACKET
                            |   ID ASSIGN LBRACKET expression_list RBRACKET'''

def p_ternary_expression(p):
    '''ternary_expression   :   or_expression QMARK expression TCOLON expression'''

def p_or_expression(p):
    '''or_expression    :   or_expression OR and_expression
                        |   and_expression'''
   
def p_and_expression(p):
    '''and_expression   :   and_expression AND equality_expression
                        |   equality_expression'''

def p_equality_expression(p):
    '''equality_expression  :   equality_expression EQUAL relational_expression
                            |   equality_expression NOT_EQUAL relational_expression
                            |   equality_expression TIPO_EQUAL relational_expression
                            |   relational_expression'''

def p_relational_expression(p):
    '''relational_expression : relational_expression GREATER_THAN add_expression
                             | relational_expression LESS_THAN add_expression
                             | relational_expression GREATER_EQUAL add_expression
                             | relational_expression LESS_EQUAL add_expression
                             | bitwise_expression'''

def p_bitwise_expression(p):
    '''bitwise_expression : bitwise_expression SHIFT_LEFT add_expression
                          | bitwise_expression SHIFT_RIGHT add_expression
                          | bitwise_expression BIT_AND add_expression
                          | bitwise_expression BIT_OR add_expression
                          | bitwise_expression BIT_XOR add_expression
                          | add_expression'''

def p_add_expression(p):
    '''add_expression   :   add_expression PLUS multi_expression
                        |   add_expression MINUS multi_expression
                        |   multi_expression'''
  
def p_multi_expression(p):
    '''multi_expression :   multi_expression TIMES exponent_expression
                        |   multi_expression DIVISION exponent_expression
                        |   multi_expression MOD exponent_expression
                        |   exponent_expression'''

def p_exponent_expression(p):
    '''exponent_expression  :   unary_expression POTENCIACAO_ASSIGN exponent_expression
                            |   unary_expression'''

def p_unary_expression(p):
    '''unary_expression : EXCLAMATION unary_expression
                        | TILDE unary_expression
                        | PLUS unary_expression
                        | MINUS unary_expression
                        | primary_expression'''

def p_primary_expression(p):
    '''primary_expression : LPAREN expression RPAREN
                          | ID
                          | LITERAL
                          | range_expression'''
    
def p_range_expression(p):
    '''range_expression : expression DOTDOT expression
                        | expression DOTDOTDOT expression'''




#-------------------------------------------------------------
def p_empty(p):
    'empty :'
    pass

def p_statements_block(p):
    '''statements_block :   DO statements END
                        |   LBRACE statements RBRACE
                        |   statements'''

def p_delimiter(p):
    '''delimiter    :   NEWLINE
                    |   SEMICOLON
                    |   empty'''


def p_types(p):
    '''types    :   integer
                |   float 
                |   boolean'''
    
def p_types_null(p):
    '''types_null   :   type
                    |   empty'''
    
def p_integer(p):
    '''integer :    INT
                |   INT8
                |   INT16
                |   INT32
                |   INT64
                |   INT128
                |   UINT8
                |   UINT16
                |   UINT32
                |   UINT64
                |   UINT128'''
    
def p_float(p):
    '''float    :   FLOAT
                |   FLOAT32
                |   FLOAT64'''
    
def p_boolean(p):
    'boolean    :   BOOL'

#----------------------------------------------OtherPart-----------------------------------------------------------

# Constrói o analisador léxico a partir das regras definidas
lexer = lex.lex()

# Constrói o analisador sintático a partir das regras definidas
parser = yacc.yacc()

# Exemplo de como usar o parser para analisar uma entrada
if __name__ == '__main__':
    data = '@ integer variavel ;' # Exemplo de código para testar
    result = parser.parse(data, lexer=lexer)
    print(result) # Imprime o resultado da análise (geralmente uma AST)



