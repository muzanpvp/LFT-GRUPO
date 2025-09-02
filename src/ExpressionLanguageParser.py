import ply.lex as lex
import ply.yacc as yacc
from ExpressionLanguageLex import *
import AbstractSyntax as sa


# Os problemas de shif/reduce relacionado aos terminal Plus e Minus da unary_expression, o qual descreve o uso de atribuição simples ao uma variavel, mas especificando
# se o número é positivo ou negativo, como no exemplos a seguir : x = -5 ou x = +5
# o proprio PLY resolve esse conflito por shift, e o sintático reconhece corretamente o token.

# O sintatico não aceita esse exemplo : [0..5], ou uma [expression], ou aceita isso como array, pois o unico uso tirando os conceitos de classes, só funcionaria para o 
#range expression.


#Eliminar regras relacionadas a classes, foreach
#Trabalhar so com 32bits: inteiro

precedence = (
    ('nonassoc', 'LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL'),
    ('left', 'EQUAL', 'NOT_EQUAL', 'TIPO_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTI', 'DIVIDE', 'MODULO'),
    ('right', 'POTENCIACAO'),
    ('right', 'UMINUS', 'UPLUS', 'NOT', 'TILDE'),
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
                |   function_list
                |   statements'''
    
    require_list = None
    constant_list = None
    module_list = None
    function_list = None

    for item in p[1:]:
        if item is None:
            continue
        if isinstance(item, list) and item:  # lista não vazia
            first_elem = item[0]
            if isinstance(first_elem, sa.Constant):
                constant_list = item
            elif isinstance(first_elem, sa.Module):
                module_list = item
            elif isinstance(first_elem, (sa.CompoundFunction, sa.CompoundFunctionNoParams)):
                function_list = item
            else:
                require_list = item
        else:
            # item único
            # Aqui você pode tentar identificar o tipo, ou assumir que seja require_list
            require_list = [item]  # ou ajustar conforme o tipo real

    # Substituir None por listas vazias para evitar erros posteriores
    require_list = require_list or []
    constant_list = constant_list or []
    module_list = module_list or []
    function_list = function_list or []

    p[0] = sa.Program(
        require_list=require_list,
        constant_list=constant_list,
        module_list=module_list,
        function_list=function_list
    )

#---------------------------------------------REQUIRE---------------------------------------------

def p_require_list(p):
    '''require_list :   require require_list
                    |   require'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_require(p):
    '''require  :   REQUIRE STRING'''
    p[0] = p[2]

#---------------------------------------------CONSTANTS---------------------------------------------
def p_constant_list(p):
    '''constant_list    :   constant constant_list
                        |   constant'''
    
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]
    
def p_constant(p):
    '''constant :   CONSTANT ASSIGN expression'''
    p[0] = sa.Constant(name=None, expr=p[3])

#---------------------------------------------MODULES---------------------------------------------

def p_module_list(p):
    '''module_list  :   module module_list
                    |   module'''
    
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_module(p):
    '''module   :   MODULE ID statements END'''
    p[0] = sa.Module(name=p[2], statements=p[3])

#-----------------------------FUNCTIONS-----------------------------
def p_function_list(p):
    '''function_list    :   function 
                        |   function function_list'''

    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_function(p):
    '''function :   DEF ID LPAREN opt_argument_list RPAREN opt_return_type statements END
                |   DEF ID opt_return_type NEWLINE statements END'''

    if len(p) == 8:
        p[0] = sa.CompoundFunction(name=p[2], parameters=p[4], statements=p[6])
    else:
        p[0] = sa.CompoundFunctionNoParams(name=p[2], statements=p[5])

def p_opt_argument_list(p):
    '''opt_argument_list    :   argument_list
                            |   empty'''
    p[0] = p[1] if p[1] is not None else []

def p_argument_list(p):
    '''argument_list    :   argument
                        |   argument COMMA argument_list'''
    
    if len(p) == 3:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_argument(p):
    '''argument :   ID
                |   ID COLON types
                |   ID ASSIGN expression
                |   ID COLON types ASSIGN expression'''
    
    if len(p) == 2:
        p[0] = sa.Variable(name=p[1])
    elif len(p) == 4 and p[2] == ':':
        p[0] = sa.Variable(name=p[1], type_=p[3])
    elif len(p) == 4 and p[2] == '=':
        p[0] = sa.Variable(name=p[1], value=p[3])
    else:
        p[0] = sa.Variable(name=p[1], type_=p[3], value=p[5])

def p_opt_return_type(p):
    '''opt_return_type  :   COLON types
                        |   empty'''
    p[0] = p[2] if len(p) > 2 else None

#---------------------------------------------VARIABLES---------------------------------------------

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

def p_string_literal(p):
    '''string_literal   :   STRING
                        |   STRING INTERP_START expression INTERP_END string_literal'''

#-----------------------------VARIABLES-----------------------------   
def p_variable_declaration(p):
    '''variable_declaration :   ID COLON types ASSIGN expression
                            |   ID ASSIGN expression
                            |   ID COMMA list_of_identifiers ASSIGN expression COMMA list_of_values'''

def p_list_of_identifiers(p):
    '''list_of_identifiers  :   ID
                            |   ID COMMA list_of_identifiers'''

def p_list_of_values(p):
    '''list_of_values   :   expression
                        |   expression COMMA list_of_values'''
    
#----------------------------FunctionCall-------------------------------------
def p_function_call(p):
    '''function_call    :   ID LPAREN expression_list RPAREN
                        |   ID LPAREN RPAREN'''

def p_opt_expression_list(p):
    '''opt_expression_list  :   expression_list
                            |   empty'''

def p_expression_list(p):
    '''expression_list  :   expression
                        |   expression_list COMMA expression'''
    
#-----------------------------STATEMENTS / CONTROL-----------------------------

def p_statements(p):
    '''statements   :   statements_list '''
                    
def p_statements_list(p):
    '''statements_list  :   statements_list statements_base
                        |   empty '''
    
def p_statements_base(p):
    '''statements_base   :   statement NEWLINE
                         |   statement SEMICOLON'''
#criar ponto comum (filtro semantico)
#expression e variable_declaration
def p_statement(p):
    '''statement    :   expression
                    |   control_structure
                    |   variable_declaration
                    |   function_call'''
    
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
    '''if_statement : IF if_condition statements opt_elsif opt_else END'''

def p_unless_statement(p):
    '''unless_statement : UNLESS if_condition statements opt_else END'''

def p_if_condition(p):
    '''if_condition : expression
                    | expression LBRACE statements RBRACE'''

def p_opt_elsif(p):
    '''opt_elsif : elsif_list
                 | empty'''

def p_elsif_list(p):
    '''elsif_list : elsif_list elsif
                  | elsif'''

def p_elsif(p):
    '''elsif : ELSIF if_condition statements'''

def p_opt_else(p):
    '''opt_else : ELSE statements
                | empty'''

def p_loop_structure(p):
    '''loop_structure   :   while
                        |   until
                        |   loop
                        |   iterator'''

def p_while(p):
    '''while    :   WHILE expression statements'''

def p_until(p):
    '''until    :   UNTIL expression statements'''

def p_loop(p):
    '''loop :   LOOP statements'''

#Acho que o foreach já esta adicionado aqui!
def p_iterator(p):
    '''iterator :   expression DOT MULTI statements
                |   expression DOT EACH DO PIPE ID PIPE statements END
                |   expression DOT EACH LBRACE PIPE ID PIPE RBRACE statements'''

def p_case_structure(p):
    '''case_structure   :   CASE expression when_list opt_else END'''

def p_when_list(p):
    '''when_list    :   WHEN expression statements
                    |   when_list WHEN expression statements'''

def p_return_statement(p):
    '''return_statement :   RETURN opt_expression'''

def p_break_statement(p):
    '''break_statement  :   BREAK opt_expression'''

def p_next_statement(p):
    '''next_statement   :   NEXT opt_expression'''

def p_opt_expression(p):
    '''opt_expression   :   expression
                        |   empty'''

#-----------------------------EXPRESSION HIERARCHY-----------------------------
def p_expression(p):
    '''expression   :   assignment_expression'''

def p_assignment_expression(p):
    '''assignment_expression    :   assignment_target ASSIGN expression
                                |   assignment_target PLUS_ASSIGN expression
                                |   assignment_target MINUS_ASSIGN expression
                                |   assignment_target MULTI_ASSIGN expression
                                |   assignment_target DIVIDE_ASSIGN expression
                                |   ternary_expression'''
             
def p_assignment_target(p): 
    '''assignment_target    :   ID
                            |   UNDERSCORE
                            |   ASTERISK assignment_target'''

def p_ternary_expression(p):
    '''ternary_expression   :   range_expression QMARK expression TCOLON expression
                            |   range_expression'''
    
def p_range_expression(p):
    '''range_expression :   logical_or_expression DOTDOT logical_or_expression
                        |   logical_or_expression DOTDOTDOT logical_or_expression
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
                        |   primary_expression'''

#-----------------------------POSTFIX (calls / index)-----------------------------

def p_primary_expression(p):
    '''primary_expression   :   LPAREN expression RPAREN
                            |   array_literal
                            |   literal
                            |   ID'''

def p_array_literal(p):
    '''array_literal    :   LBRACKET opt_expression_list RBRACKET'''
    
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

data = """
def X
x = +5 + 3 + 1
z : Int8 = 5
end
"""
result = parser.parse(data, lexer=lexer, debug = True)
print(result)