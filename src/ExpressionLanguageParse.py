import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *

#---------------------------------------------PROGRAM--------------------------------------------------------------
def p_program(p):
    '''program : opt_require opt_globals opt_modules opt_code_functions opt_code'''

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

#-----------------------------------------------MODULES------------------------------------------------------------

def p_opt_modules(p):
    '''opt_modules  : modules
                    | empty'''

def p_modules(p):
    '''modules  :   modules module
                |   module'''  

def p_module(p):
    '''module   :   MODULE ID NEWLINE opt_code END'''

#-----------------------------------------------FUNCTIONS----------------------------------------------------------

def p_opt_code_functions(p):
    '''opt_code_functions   : code_functions
                            | empty''' 

def p_code_functions(p):
    '''code_functions   :   code_functions functions
                        |   functions''' 

def p_functions(p):
    '''functions    :  DEF ID opt_params NEWLINE opt_code END'''

#----------------------------------------------------CODE----------------------------------------------------------
def p_opt_code(p):
    '''opt_code :   statements
                |   empty '''


def p_statementes(p):
    '''statementes : statement
                  | statement statementes'''

def p_statement(p):
    '''statement : expression
                 | control_structures
                 | return_statement
                 | break_statement
                 | next_statement'''
 


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
                          | return_statement'''
    
def p_conditional(p):
    '''conditional  :   if 
                    |   unless'''

def p_loop_structure(p):
    '''loop_structure   :   while
                        |   until
                        |   loop
                        |   iterator'''
#Falta select
def p_while(p):
    '''while   :   WHILE expression statements_block'''

def p_until(p):
    '''until  :   UNTIL expression statements_block'''

def p_loop(p):
    '''loop :   LOOP statements_block'''

def p_iterator(p):
    '''iterator :   expression DOT MULTI statements_block
                |   expression DOT EACH DO PIPE ID PIPE statements_block END
                |   expression DOT EACH LBRACE PIPE ID PIPE RBRACE statements_block'''

#--------------------------------------------------CONDITIONS------------------------------------------------------

def p_if(p):
    '''if   :   IF expression statements_block opt_elsif opt_else END'''
    
def p_opt_elsif(p):
    '''opt_elsif    :   ELSIF expression statements_block opt_elsif
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
#Esta sendo visivel, mas olhar melhor esse BREAK Expresseion
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
    '''multi_expression :   multi_expression MULTI exponent_expression
                        |   multi_expression DIVIDE exponent_expression
                        |   multi_expression MODULO exponent_expression
                        |   exponent_expression'''

def p_exponent_expression(p):
    '''exponent_expression  :   unary_expression POTENCIACAO exponent_expression
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
    '''range_expression : or_expression
                        | or_expression DOTDOT or_expression
                        | or_expression DOTDOTDOT or_expression'''
def p_opt_params(p):
    '''opt_params : empty'''

def p_expression_list(p):
    '''expression_list : expression
                       | expression COMMA expression_list'''



#-------------------------------------------------------------
def p_empty(p):
    'empty :'
    pass

def p_statements_block(p):
    '''statements_block :   DO statements END
                        |   LBRACE statements RBRACE
                        |   statements'''

def p_delimiter(p):
    '''delimiter    :   SEMICOLON
                    |   empty'''


def p_types(p):
    '''types    :   integer
                |   float 
                |   boolean'''
    
def p_types_null(p):
    '''types_null   :   types
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

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value {p.value}")
    else:
        print("Syntax error at EOF")


#----------------------------------------------OtherPart-----------------------------------------------------------

# Constrói o analisador léxico a partir das regras definidas
lexer = lex.lex()

# Constrói o analisador sintático a partir das regras definidas
parser = yacc.yacc()

# Exemplo de como usar o parser para analisar uma entrada
if __name__ == '__main__':
    data = 'puts "oi" ' # Exemplo de código para testar
    result = parser.parse(data, lexer=lexer)
    print(result) # Imprime o resultado da análise (geralmente uma AST)



