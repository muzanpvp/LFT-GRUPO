from abc import ABCMeta
from abc import abstractmethod


class Node(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Program(Node):
    def __init__(self, requires=None, constants=None, modules=None, functions=None, statements=None):
        self.requires = requires or []
        self.constants = constants or []
        self.modules = modules or []
        self.functions = functions or []
        self.statements = statements or []

    def accept(self, visitor):
        return visitor.visitProgram(self)

class RequireItem(Node):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.visitRequireItem(self)

class ConstantItem(Node):
    def __init__(self, name=None, expr=None):
        self.name = name
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitConstantItem(self)

class ModuleItem(Node):
    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitModuleItem(self)

class CompoundFunction(Node):
    def __init__(self, id, parameters=None, command=None):
        self.id = id
        self.parameters = parameters or []
        self.command = command

    def accept(self, visitor):
        return visitor.visitCompoundFunction(self)

class CompoundFunctionNoParams(Node):
    def __init__(self, id, command=None):
        self.id = id
        self.command = command

    def accept(self, visitor):
        return visitor.visitCompoundFunctionNoParams(self)


# Statements

class Statement(Node):
    pass

class ExpressionStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitExpressionStatement(self)

class VariableDeclaration(Statement):
    def __init__(self, name, type = None, value = None):
        self.names = name or []
        self.var_type = type
        self.values = value or []

    def accept(self, visitor):
        return visitor.visitVariableDeclaration(self)

class MultiVariableDeclaration(Statement):
    def __init__(self, ids=None, value=None, values=None):
        self.ids = ids or []
        self.value = value
        self.values = values or []

    def accept(self, visitor):
        return visitor.visitMultiVariableDeclaration(self)

class Assignment(Statement):
    def __init__(self, target, op, value):
        self.target = target
        self.op = op
        self.value = value

    def accept(self, visitor):
        return visitor.visitAssignment(self)

class IfStatement(Statement):
    def __init__(self, condition, then_block, elsif_list=None, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.elsif_list = elsif_list or []
        self.else_block = else_block

    def accept(self, visitor):
        return visitor.visitIfStatement(self)

class UnlessStatement(Statement):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def accept(self, visitor):
        return visitor.visitUnlessStatement(self)

class WhileLoop(Statement):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def accept(self, visitor):
        return visitor.visitWhileLoop(self)

class UntilLoop(Statement):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def accept(self, visitor):
        return visitor.visitUntilLoop(self)

class Loop(Statement):
    def __init__(self, block):
        self.block = block

    def accept(self, visitor):
        return visitor.visitLoop(self)

class Iterator(Statement):
    def __init__(self, expr, statements):
        self.expr = expr
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitIterator(self)

class EachIterator(Statement):
    def __init__(self, expr, var_id, statements):
        self.expr = expr
        self.var_id = var_id
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitEachIterator(self)

class CaseStatement(Statement):
    def __init__(self, expr, when_list, else_block=None):
        self.expr = expr
        self.when_list = when_list
        self.else_block = else_block

    def accept(self, visitor):
        return visitor.visitCaseStatement(self)

class WhenItem(Node):
    def __init__(self, expr, block):
        self.expr = expr
        self.block = block

    def accept(self, visitor):
        return visitor.visitWhenItem(self)

class ReturnStatement(Statement):
    def __init__(self, expr=None):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitReturnStatement(self)

class BreakStatement(Statement):
    def __init__(self, expr=None):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitBreakStatement(self)

class NextStatement(Statement):
    def __init__(self, expr=None):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitNextStatement(self)

class ElsifItem(Node):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def accept(self, visitor):
        return visitor.visitElsifItem(self)

class ConditionWithBlock(Node):
    def __init__(self, expr, block):
        self.expr = expr
        self.block = block

    def accept(self, visitor):
        return visitor.visitConditionWithBlock(self)

# Expressions

class Expression(Node):
    pass

class BinaryOp(Expression):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinaryOp(self)

class UnaryOp(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def accept(self, visitor):
        return visitor.visitUnaryOp(self)

class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.visitVariable(self)

class ArrayLiteral(Expression):
    def __init__(self, elements=None):
        self.elements = elements or []

    def accept(self, visitor):
        return visitor.visitArrayLiteral(self)

class NilLiteral(Expression):
    def accept(self, visitor):
        return visitor.visitNilLiteral(self)

class VariableItem(Node):
    def __init__(self, name, type=None, value=None):
        self.name = name
        self.type = type
        self.value = value

    def accept(self, visitor):
        return visitor.visitVariableItem(self)

class FunctionCall(Expression):
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or []

    def accept(self, visitor):
        return visitor.visitFunctionCall(self)

class TernaryIf(Expression):
    def __init__(self, condition, true_expr, false_expr):
        self.condition = condition
        self.true_expr = true_expr
        self.false_expr = false_expr

    def accept(self, visitor):
        return visitor.visitTernaryIf(self)

# Types

class TypeName(Node):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.visitTypeName(self)

# Literals

class IntLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitIntLiteral(self)

class FloatLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitFloatLiteral(self)

class StringLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitStringLiteral(self)

class CharLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitCharLiteral(self)

class BooleanLiteral(Expression):
    def __init__(self, value: bool):
        self.value = value

    def accept(self, visitor):
        return visitor.visitBooleanLiteral(self)
