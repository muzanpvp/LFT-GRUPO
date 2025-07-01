#import ply.lex as lex

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
    'extends' : 'EXTENDS',
    'require' : 'REQUIRE', 
    'rescue' : 'RESCUE', 
    'ensure' : 'ENSURE',

    # Literais e Valores Especiais

    'true' : 'TRUE', 
    'false' : 'FALSE', 
    'nil' : 'NIL',
    'uninitialized' : 'UNINITIALIZED', 
    'self' : 'SELF', 
    'super' : 'SUPER',

    # Tipos, Operações e Metaprogramação

    'as' : 'AS', 
    'typeof' : 'TYPEOF', 
    'type' : 'TYPE', 
    'sizeof' : 'SIZEOF',
    'pointerof' : 'POINTEROF', 
    'lib' : 'LIB', 
    'out' : 'OUT',
    'private' : 'PRIVATE', 
    'protected' : 'PROTECTED', 
    'of' : 'OF',

    # Blocos e Outros

    'begin' : 'BEGIN', 
    'end' : 'END', 
    'asm' : 'ASM', 
    'select' : 'SELECT',
}

tokens = [

    'PLUS', 
    'MINUS', 
    'ASTERISK', 
    'SLASH', 
    'PERCENT', 
    'DOUBLE_ASTERISK',
    'EQUALS', 
    'PLUS_EQUALS', 
    'MINUS_EQUALS', 
    'ASTERISK_EQUALS', 
    'SLASH_EQUALS',
    'PERCENT_EQUALS', 
    'DOUBLE_ASTERISK_EQUALS', 
    'OR_EQUALS', 
    'DOUBLE_EQUALS',
    'NOT_EQUALS', 
    'LESS_THAN', 
    'GREATER_THAN', 
    'LESS_EQUALS', 
    'GREATER_EQUALS',
    'TRIPLE_EQUALS', 
    'LOGICAL_AND', 
    'LOGICAL_OR', 
    'BANG', 
    'AMPERSAND', 
    'PIPE',
    'CARET', 
    'TILDE', 
    'LEFT_SHIFT', 
    'RIGHT_SHIFT', 
    'INCLUSIVE_RANGE',
    'EXCLUSIVE_RANGE', 
    'QUESTION_DOT', 
    'HASH_ROCKET', 
    'DOUBLE_COLON',
    'LPAREN', 
    'RPAREN', 
    'LBRACKET', 
    'RBRACKET', 
    'LBRACE', 
    'RBRACE',
    'COMMA', 
    'SEMICOLON', 
    'COLON', 
    'DOT', 
    'QUESTION_MARK',

] + tuple(reservadas.values())