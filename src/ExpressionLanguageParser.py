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
                |   function_list'''
    
    # Lógica para as produções de 4 listas
    if len(p) == 5:
        p[0] = sa.Program(requires=p[1], constants=p[2], modules=p[3], functions=p[4])
    
    # Lógica para as produções de 3 listas
    elif len(p) == 4:
        if isinstance(p[1], list) and all(isinstance(x, sa.Require) for x in p[1]):
            if p[3] and isinstance(p[3], list) and all(isinstance(x, sa.Module) for x in p[3]):
                p[0] = sa.Program(requires=p[1], constants=p[2], modules=p[3])
            else:
                p[0] = sa.Program(requires=p[1], constants=p[2], functions=p[3])
        elif p[1] and isinstance(p[1], list) and all(isinstance(x, sa.Require) for x in p[1]):
            p[0] = sa.Program(requires=p[1], modules=p[2], functions=p[3])
        else:
            p[0] = sa.Program(constants=p[1], modules=p[2], functions=p[3])

    # Lógica para as produções de 2 listas
    elif len(p) == 3:
        if p[1] and isinstance(p[1], list) and all(isinstance(x, sa.Require) for x in p[1]):
            if p[2] and isinstance(p[2], list) and all(isinstance(x, sa.Constant) for x in p[2]):
                p[0] = sa.Program(requires=p[1], constants=p[2])
            elif p[2] and isinstance(p[2], list) and all(isinstance(x, sa.Module) for x in p[2]):
                p[0] = sa.Program(requires=p[1], modules=p[2])
            else:
                p[0] = sa.Program(requires=p[1], functions=p[2])
        elif p[1] and isinstance(p[1], list) and all(isinstance(x, sa.Constant) for x in p[1]):
            if p[2] and isinstance(p[2], list) and all(isinstance(x, sa.Module) for x in p[2]):
                p[0] = sa.Program(constants=p[1], modules=p[2])
            else:
                p[0] = sa.Program(constants=p[1], functions=p[2])
        else:
            p[0] = sa.Program(modules=p[1], functions=p[2])

    # Lógica para as produções de 1 lista
    elif len(p) == 2:
        if p[1] and isinstance(p[1], list) and all(isinstance(x, sa.Require) for x in p[1]):
            p[0] = sa.Program(requires=p[1])
        elif p[1] and isinstance(p[1], list) and all(isinstance(x, sa.Constant) for x in p[1]):
            p[0] = sa.Program(constants=p[1])
        elif p[1] and isinstance(p[1], list) and all(isinstance(x, sa.Module) for x in p[1]):
            p[0] = sa.Program(modules=p[1])
        else:
            p[0] = sa.Program(functions=p[1])

def p_program_statements(p):
    '''program : statements'''
    p[0] = sa.Program(statements=p[1])


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
    p[0] = sa.RequireItem(p[2])

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
    p[0] = sa.ConstantItem(name=None, expr=p[3])

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
    p[0] = sa.ModuleItem(name=p[2], statements=p[3])

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
        p[0] = sa.CompoundFunction(id=p[2], parameters=p[4], command=p[6]) 
    else: 
        p[0] = sa.CompoundFunctionNoParams(id=p[2], command=p[5])


def p_opt_argument_list(p):
    '''opt_argument_list    :   argument_list
                            |   empty'''
    p[0] = p[1] if p[1] is not None else []

def p_argument_list(p):
    '''argument_list    :   argument
                        |   argument COMMA argument_list'''
    if len(p) == 2: 
        p[0] = [p[1]] 
    else: 
        p[0] = [p[1]] + p[3]
    

def p_argument(p):
    '''argument :   ID
                |   ID COLON types
                |   ID ASSIGN expression
                |   ID COLON types ASSIGN expression'''
    
    if len(p) == 2: 
        p[0] = sa.VariableItem(name=p[1]) 
    elif len(p) == 4 and p[2] == ':': 
        p[0] = sa.VariableItem(name=p[1], type=p[3]) 
    elif len(p) == 4 and p[2] == '=': 
        p[0] = sa.VariableItem(name=p[1], value=p[3]) 
    else: p[0] = sa.VariableItem(name=p[1], type=p[3], value=p[5])

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
    p[0] = sa.TypeName(p[1]) if isinstance(p[1], str) else p[1]

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
    p[0] = sa.TypeName(p[1])

def p_float(p):
    '''float    :   FLOAT
                |   FLOAT32
                |   FLOAT64'''
    p[0] = sa.TypeName(p[1])

def p_boolean(p):
    '''boolean  :   BOOL'''
    p[0] = sa.TypeName(p[1])

def p_literal(p):
    '''literal  :   INTNUMBER
                |   FLOATNUMBER
                |   STRING
                |   CHAR
                |   TRUE
                |   FALSE'''
    t = p.slice[1].type 
    if t == 'INTNUMBER': 
        p[0] = sa.IntLiteral(int(p[1])) 
    elif t == 'FLOATNUMBER': 
        p[0] = sa.FloatLiteral(float(p[1])) 
    elif t == 'STRING': 
        p[0] = sa.StringLiteral(p[1])
    elif t == 'CHAR': 
        p[0] = sa.CharLiteral(p[1]) 
    elif t == 'TRUE': 
        p[0] = sa.BooleanLiteral(True) 
    elif t == 'FALSE': 
        p[0] = sa.BooleanLiteral(False)

#-----------------------------VARIABLES-----------------------------   

def p_variable_declaration(p):
    '''variable_declaration :   list_of_identifiers COLON types ASSIGN expression_list1
                            |   list_of_identifiers ASSIGN expression_list1'''
    if len(p) == 6:  
        p[0] = sa.VariableDeclaration(names=p[1], type=p[3], value=p[5])
    else:  
        p[0] = sa.VariableDeclaration(names=p[1], type=None, value=p[3])
    
def p_list_of_identifiers(p):
    '''list_of_identifiers  :   ID
                            |   ID COMMA list_of_identifiers'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression_list1(p):
    '''expression_list1 :   expression
                        |   expression COMMA expression_list1'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

#----------------------------FunctionCall-------------------------------------
def p_function_call(p):
    '''function_call    :   ID LPAREN expression_list RPAREN
                        |   ID LPAREN RPAREN'''
    if len(p) == 5: 
        p[0] = sa.FunctionCall(name=p[1], args=p[3]) 
    else: 
        p[0] = sa.FunctionCall(name=p[1], args=[])

def p_opt_expression_list(p):
    '''opt_expression_list  :   expression_list
                            |   empty'''
    p[0] = p[1] if p[1] is not None else []

def p_expression_list(p):
    '''expression_list  :   expression
                        |   expression_list COMMA expression'''
    if len(p) == 2: 
        p[0] = [p[1]] 
    else: p[0] = p[1] + [p[3]]
    
#-----------------------------STATEMENTS / CONTROL-----------------------------

def p_statements(p):
    '''statements : statements_list'''
    p[0] = p[1]

def p_statements_list(p):
    '''statements_list : statement NEWLINE statements_list
                       | statement'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]
    

def p_opt_statements(p):
    '''opt_statements : statements_list
                      | empty'''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1]
#criar ponto comum (filtro semantico)
#expression e variable_declaration
def p_statement(p):
    '''statement    :   expression
                    |   control_structure
                    |   variable_declaration
                    |   function_call'''
    p[0] = p[1]
    
def p_control_structure(p):
    '''control_structure    :   conditional
                            |   loop_structure
                            |   case_structure
                            |   return_statement
                            |   break_statement
                            |   next_statement'''
    p[0] = p[1]

def p_conditional(p):
    '''conditional  :   if_statement
                    |   unless_statement'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF if_condition statements opt_elsif opt_else END'''
    p[0] = sa.IfStatement(condition=p[2], then_block=p[3], elsif_list=p[4], else_block=p[5])

def p_unless_statement(p):
    '''unless_statement : UNLESS if_condition statements opt_else END'''
    p[0] = sa.UnlessStatement(condition=p[2], then_block=p[3], else_block=p[4])

def p_if_condition(p):
    '''if_condition : expression
                    | expression LBRACE statements RBRACE'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.ConditionWithBlock(expr=p[1], block=p[3])

def p_opt_elsif(p):
    '''opt_elsif : elsif_list
                 | empty'''
    p[0] = p[1]

def p_elsif_list(p):
    '''elsif_list : elsif_list elsif
                  | elsif'''
    if len(p) == 3: 
        p[0] = p[1] + [p[2]] 
    else: p[0] = [p[1]]

def p_elsif(p):
    '''elsif : ELSIF if_condition statements'''
    p[0] = sa.ElsifItem(condition=p[2], block=p[3])

def p_opt_else(p):
    '''opt_else : ELSE statements
                | empty'''
    p[0] = p[2] if len(p) > 2 else None

def p_loop_structure(p):
    '''loop_structure   :   while
                        |   until
                        |   loop
                        |   iterator'''
    p[0] = p[1]

def p_while(p):
    '''while    :   WHILE expression statements'''
    p[0] = sa.WhileLoop(condition=p[2], block=p[3])

def p_until(p):
    '''until    :   UNTIL expression statements'''
    p[0] = sa.UntilLoop(condition=p[2], block=p[3])

def p_loop(p):
    '''loop :   LOOP DO statements END
            |   LOOP LBRACE statements RBRACE'''
    p[0] = sa.Loop(block=p[3])

#Acho que o foreach já esta adicionado aqui!
def p_iterator(p):
    '''iterator :   expression DOT MULTI statements
                |   expression DOT EACH DO PIPE ID PIPE statements END
                |   expression DOT EACH LBRACE PIPE ID PIPE RBRACE statements'''
    if len(p) == 5: 
        p[0] = sa.Iterator(expr=p[1], statements=p[4]) 
    elif len(p) == 10: 
        p[0] = sa.EachIterator(expr=p[1], var_id=p[5], statements=p[8]) 
    elif len(p) == 9: 
        p[0] = sa.EachIterator(expr=p[1], var_id=p[5], statements=p[8])

def p_case_structure(p):
    '''case_structure   :   CASE expression when_list opt_else END'''
    p[0] = sa.CaseStatement(expr=p[2], when_list=p[3], else_block=p[4])

def p_when_list(p):
    '''when_list    :   WHEN expression statements
                    |   when_list WHEN expression statements'''
    if len(p) == 4: 
        p[0] = [sa.WhenItem(expr=p[2], block=p[3])] 
    else: 
        p[0] = p[1] + [sa.WhenItem(expr=p[3], block=p[4])]

def p_return_statement(p):
    '''return_statement :   RETURN opt_expression'''
    p[0] = sa.ReturnStatement(expr=p[2])

def p_break_statement(p):
    '''break_statement  :   BREAK opt_expression'''
    p[0] = sa.BreakStatement(expr=p[2])

def p_next_statement(p):
    '''next_statement   :   NEXT opt_expression'''
    p[0] = sa.NextStatement(expr=p[2])

def p_opt_expression(p):
    '''opt_expression   :   expression
                        |   empty'''
    p[0] = p[1]

#-----------------------------EXPRESSION HIERARCHY-----------------------------
def p_expression(p):
    '''expression   :   assignment_expression'''
    p[0] = p[1]

def p_assignment_expression(p):
    '''assignment_expression    :   assignment_target PLUS_ASSIGN expression
                                |   assignment_target MINUS_ASSIGN expression
                                |   assignment_target MULTI_ASSIGN expression
                                |   assignment_target DIVIDE_ASSIGN expression
                                |   ternary_expression'''
    if len(p) == 4:
        p[0] = sa.Assignment(target=p[1], op=p[2], value=p[3])
    else:
        p[0] = p[1]

def p_assignment_target(p): 
    '''assignment_target    :   ID
                            |   UNDERSCORE
                            |   ASTERISK assignment_target'''
    if len(p) == 2: 
        if p.slice[1].type == 'ID': 
            p[0] = sa.Variable(p[1]) 
        elif p.slice[1].type == 'UNDERSCORE': 
            p[0] = sa.Underscore() 
        else: 
            p[0] = sa.Asterisk(p[2])

def p_ternary_expression(p):
    '''ternary_expression   :   range_expression QMARK expression TCOLON expression
                            |   range_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.TernaryIf(condition=p[1], true_expr=p[3], false_expr=p[5])
    
def p_range_expression(p):
    '''range_expression :   logical_or_expression DOTDOT logical_or_expression
                        |   logical_or_expression DOTDOTDOT logical_or_expression
                        |   logical_or_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_logical_or_expression(p):
    '''logical_or_expression    :   logical_and_expression
                                |   logical_or_expression OR logical_and_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_logical_and_expression(p):
    '''logical_and_expression   :   equality_expression
                                |   logical_and_expression AND equality_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_equality_expression(p):
    '''equality_expression  :   relational_expression
                            |   equality_expression EQUAL relational_expression
                            |   equality_expression NOT_EQUAL relational_expression
                            |   equality_expression TIPO_EQUAL relational_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_relational_expression(p):
    '''relational_expression    :   additive_expression
                                |   relational_expression GREATER_THAN additive_expression
                                |   relational_expression LESS_THAN additive_expression
                                |   relational_expression GREATER_EQUAL additive_expression
                                |   relational_expression LESS_EQUAL additive_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_additive_expression(p):
    '''additive_expression  :   multiplicative_expression
                            |   additive_expression PLUS multiplicative_expression
                            |   additive_expression MINUS multiplicative_expression '''
    if len(p) == 2:
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_multiplicative_expression(p):
    '''multiplicative_expression    :   potenciacao_expression
                                    |   multiplicative_expression MULTI potenciacao_expression
                                    |   multiplicative_expression DIVIDE potenciacao_expression
                                    |   multiplicative_expression MODULO potenciacao_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_potenciacao_expression(p):
    '''potenciacao_expression   :   unary_expression
                                |   potenciacao_expression POTENCIACAO unary_expression'''
    if len(p) == 2: 
        p[0] = p[1] 
    else: 
        p[0] = sa.BinaryOp(p[2], p[1], p[3])

def p_unary_expression(p):
    '''unary_expression :   PLUS unary_expression %prec UPLUS
                        |   MINUS unary_expression %prec UMINUS
                        |   EXCLAMATION unary_expression
                        |   TILDE unary_expression
                        |   primary_expression'''
    if len(p) == 3: 
        p[0] = sa.UnaryOp(p[1], p[2]) 
    else: 
        p[0] = p[1]

#-----------------------------POSTFIX (calls / index)-----------------------------

def p_primary_expression(p):
    '''primary_expression   :   LPAREN expression RPAREN
                            |   array_literal
                            |   literal
                            |   ID'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 2:
        if p.slice[1].type == 'ID':
            p[0] = sa.Variable(p[1])
        else:
            p[0] = p[1]

def p_array_literal(p):
    '''array_literal    :   LBRACKET opt_expression_list RBRACKET'''
    p[0] = sa.ArrayLiteral(elements=p[2])
    
#----------------------------------------------------NONE----------------------------------------------------------
def p_empty(p):
    'empty :'
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value {p.value}")
    else:
        print("Syntax error at EOF")

#----------------------------------------------------OTHERS----------------------------------------------------------
lexer = lex.lex()
parser = yacc.yacc()

data = """
(0...5).each do |i|
  puts "Número: #{i}"
  r = +(-5-4)
  puts "#{r}"
end

"""
result = parser.parse(data, lexer=lexer, debug = True)
print(result)