import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *


#Onde tiver empty, na chamada pai, colocar um caso base com ele mesmo e tirar o empty.
# 
#Eliminar regras relacionadas a classes, foreach
#Trabalhar so com 32bits: inteiro
#na execução, verificar o parser.out no final para ver os conflitos, em quais estados e com quais expressões.


precedence = (
    ('right', 'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN',
     'MULTI_ASSIGN', 'DIVIDE_ASSIGN', 'MODULO_ASSIGN'),
    ('right', 'QMARK', 'TCOLON'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL', 'NOT_EQUAL', 'TIPO_EQUAL'),
    ('nonassoc', 'GREATER_THAN', 'LESS_THAN', 'GREATER_EQUAL', 'LESS_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTI', 'DIVIDE', 'MODULO'),
    ('right', 'POTENCIACAO'),
    ('right', 'UMINUS', 'UPLUS', 'EXCLAMATION', 'TILDE'),
    ('nonassoc', 'DOTDOT', 'DOTDOTDOT'),
    ('left', 'DOT'),
    ('left', 'LBRACKET', 'RBRACKET'),
)

#---------------------------------------------PROGRAM--------------------------------------------------------------
def p_program(p):
    '''program  :   require_list constant_list module_list function_list
                |   require_list constant_list module_list
                |   require_list constant_list function_list
                |   require_list module_list function_list
                |   constant_list module_list function_list
                |   require_list constant_list
                |   require_list module_list
                |   constant_list module_list
                |   require_list function_list
                |   constant_list function_list
                |   module_list function_list
                |   require_list
                |   constant_list
                |   module_list
                |   function_list'''

def p_require_list(p):
    '''require_list :   require require_list
                    |   require'''

def p_require(p):
    '''require  :   REQUIRE STRING'''

def p_constant_list(p):
    '''constant_list    :   constant constant_list
                        |   constant'''
    
def p_constant(p):
    '''constant :   CONSTANT ASSIGN expression'''
    
def p_module_list(p):
    '''module_list  :   module module_list
                    |   module'''

def p_module(p):
    '''module   :   MODULE ID NEWLINE statements END'''

#-----------------------------FUNCTIONS-----------------------------
def p_function_list(p):
    '''function_list    :   function 
                        |   function function_list'''

def p_function(p):
    '''function :   DEF ID LPAREN opt_argument_list RPAREN opt_return_type statements_block END
                |   DEF ID opt_return_type NEWLINE statements_block END'''

def p_opt_argument_list(p):
    '''opt_argument_list    :   argument_list
                            |   empty'''
def p_argument_list(p):
    '''argument_list    :   argument
                        |   argument COMMA argument_list'''

def p_argument(p):
    '''argument :   ID
                |   ID COLON types
                |   ID ASSIGN expression
                |   ID COLON types ASSIGN expression'''

def p_opt_return_type(p):
    '''opt_return_type  :   COLON types
                        |   empty'''

def p_types(p):
    '''types    :   STRING
                |   CHAR
                |   NIL
                |   integer
                |   float
                |   boolean'''

def p_integer(p):
    '''integer  :   INT
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
    '''boolean  :   BOOL'''

def p_literal(p):
    '''literal  :   INTNUMBER
                |   FLOATNUMBER
                |   string_literal
                |   CHAR
                |   TRUE
                |   FALSE'''

def p_function_call(p):
    '''function_call    :   ID LPAREN expression_list RPAREN'''
#|   ID LPAREN RPAREN tirei isso, pois expression_list vai para empty, iria so duas regras para o mesmo lugar, e o empty do expression_list serve para cuidar de arryas[] 

def p_opt_expression_list(p):
    '''opt_expression_list  :   expression_list
                            |   empty'''

def p_expression_list(p):
    '''expression_list  :   expression
                        |   expression_list COMMA expression'''
#-----------------------------VARIABLES-----------------------------   
def p_variable_declaration(p):
    '''variable_declaration :   ID types ASSIGN expression
                            |   ID ASSIGN expression
                            |   ID COMMA list_of_identifiers ASSIGN expression COMMA list_of_values'''

def p_list_of_identifiers(p):
    '''list_of_identifiers  :   ID
                            |   ID COMMA list_of_identifiers'''

def p_list_of_values(p):
    '''list_of_values   :   expression
                        |   expression COMMA list_of_values'''

#-----------------------------EXPRESSION HIERARCHY-----------------------------
def p_expression(p):
    '''expression   :   ternary_expression
                    |   assignment_expression'''
    p[0] = p[1]

def p_assignment_expression(p):
    '''assignment_expression    :   assignment_target ASSIGN expression
                                |   assignment_target PLUS_ASSIGN expression
                                |   assignment_target MINUS_ASSIGN expression
                                |   assignment_target MULTI_ASSIGN expression
                                |   assignment_target DIVIDE_ASSIGN expression'''

def p_assignment_target(p):
    '''assignment_target    :   postfix_expression
                            |   UNDERSCORE
                            |   ASTERISK assignment_target'''

def p_ternary_expression(p):
    '''ternary_expression   :   logical_or_expression QMARK expression TCOLON expression
                            |   logical_or_expression'''

def p_logical_or_expression(p):
    '''logical_or_expression    :   logical_and_expression
                                |   logical_or_expression OR logical_and_expression'''

def p_logical_and_expression(p):
    '''logical_and_expression   :   equality_expression
                                |   logical_and_expression AND equality_expression'''

def p_equality_expression(p):
    '''equality_expression  :   relational_expression
                            |   equality_expression EQUAL relational_expression
                            |   equality_expression NOT_EQUAL relational_expression
                            |   equality_expression TIPO_EQUAL relational_expression'''
   
def p_relational_expression(p):
    '''relational_expression    :   additive_expression
                                |   relational_expression GREATER_THAN additive_expression
                                |   relational_expression LESS_THAN additive_expression
                                |   relational_expression GREATER_EQUAL additive_expression
                                |   relational_expression LESS_EQUAL additive_expression'''

def p_additive_expression(p):
    '''additive_expression  :   multiplicative_expression
                            |   additive_expression PLUS multiplicative_expression
                            |   additive_expression MINUS multiplicative_expression '''


def p_multiplicative_expression(p):
    '''multiplicative_expression    :   potenciacao_expression
                                    |   multiplicative_expression MULTI potenciacao_expression
                                    |   multiplicative_expression DIVIDE potenciacao_expression
                                    |   multiplicative_expression MODULO potenciacao_expression'''

def p_potenciacao_expression(p):
    '''potenciacao_expression   :   unary_expression
                                |   potenciacao_expression POTENCIACAO unary_expression'''

def p_unary_expression(p):
    '''unary_expression :   PLUS unary_expression %prec UPLUS
                        |   MINUS unary_expression %prec UMINUS
                        |   EXCLAMATION unary_expression
                        |   TILDE unary_expression
                        |   postfix_expression'''

#-----------------------------POSTFIX (calls / index)-----------------------------

def p_postfix_expression(p):
    '''postfix_expression   :   primary_expression postfix_suffixes'''

def p_postfix_suffixes(p):
    '''postfix_suffixes :   postfix_suffix postfix_suffixes
                        |   postfix_suffix'''  #caso base substituir por postfix_suffix
#Falta a range_expression
def p_postfix_suffix(p):
    '''postfix_suffix   :   LBRACKET expression RBRACKET
                        |   DOTDOT primary_expression
                        |   DOTDOTDOT primary_expression'''

def p_primary_expression(p):
    '''primary_expression   :   expression_between_parentesis
                            |   array_literal
                            |   literal
                            |   ID'''

def p_expression_between_parentesis(p):
    ''' expression_between_parentesis : LPAREN expression RPAREN'''
def p_array_literal(p):
    '''array_literal    :   LBRACKET opt_expression_list RBRACKET'''
def p_string_literal(p):
    '''string_literal : STRING
                      | STRING INTERP_START expression INTERP_END string_literal'''
#-----------------------------STATEMENTS / CONTROL-----------------------------

def p_statements(p):
    '''statements   :   statement
                    |   statement NEWLINE statements'''

def p_statement(p):
    '''statement    :   expression
                    |   control_structure
                    |   variable_declaration'''
#expression
def p_control_structure(p):
    '''control_structure    :   conditional
                            |   loop_structure
                            |   case_structure
                            |   return_statement
                            |   break_statement
                            |   next_statement'''

def p_conditional(p):
    '''conditional  :   if_statement
                    |   unless_statement'''

def p_if_statement(p):
    '''if_statement :   IF expression statements_block opt_elsif opt_else END'''

def p_unless_statement(p):
    '''unless_statement :   UNLESS expression statements_block opt_else END'''

def p_opt_elsif(p):
    '''opt_elsif    :   ELSIF expression statements_block opt_elsif
                    | empty'''

def p_opt_else(p):
    '''opt_else :   ELSE statements_block
                |   empty'''

def p_loop_structure(p):
    '''loop_structure   :   while
                        |   until
                        |   loop
                        |   iterator'''

def p_while(p):
    '''while    :   WHILE expression statements_block'''

def p_until(p):
    '''until    :   UNTIL expression statements_block'''

def p_loop(p):
    '''loop :   LOOP statements_block'''

#tem que adicionar o foreach
def p_iterator(p):
    '''iterator :   expression DOT MULTI statements_block
                |   expression DOT EACH DO PIPE ID PIPE statements_block END
                |   expression DOT EACH LBRACE PIPE ID PIPE RBRACE statements_block'''

def p_case_structure(p):
    '''case_structure   :   CASE expression when_list opt_else END'''

def p_when_list(p):
    '''when_list    :   WHEN expression statements_block
                    |   when_list WHEN expression statements_block'''

def p_return_statement(p):
    '''return_statement :   RETURN opt_expression'''

def p_break_statement(p):
    '''break_statement  :   BREAK opt_expression'''

def p_next_statement(p):
    '''next_statement   :   NEXT opt_expression'''

def p_opt_expression(p):
    '''opt_expression   :   expression
                        |   empty'''

def p_statements_block(p):
    '''statements_block :   statements'''
#----------------------------------------------------NONE----------------------------------------------------------
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value {p.value}")
    else:
        print("Syntax error at EOF")

#----------------------------------------------------OTHERS----------------------------------------------------------
lexer = lex.lex()
parser = yacc.yacc()

if __name__ == '_main_':
    data = """
    x, y, z = 1, 2, 3
    
    f = 6
    g = true

    if f == 5
    # faz algo
    elsif g == true
        puts "po"
    end
    """
    result = parser.parse(data, lexer=lexer)
    print(result)