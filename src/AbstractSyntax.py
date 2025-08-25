from abc import abstractmethod
from abc import ABCMeta

#---------------------------------------------NÓS GERAIS---------------------------------------------
class Node(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

#---------------------------------------------PROGRAM---------------------------------------------
class Program(Node):
    def __init__(self, require_list=None, constant_list=None, module_list=None, function_list=None):
        self.require_list = require_list or []
        self.constant_list = constant_list or []
        self.module_list = module_list or []
        self.function_list = function_list or []

    def accept(self, visitor):
        return visitor.visit_program(self)

#---------------------------------------------CONSTANTS---------------------------------------------
class Constant(Node):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def accept(self, visitor):
        return visitor.visit_constant(self)

#---------------------------------------------MODULES---------------------------------------------
class Module(Node):
    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

    def accept(self, visitor):
        return visitor.visit_module(self)

#---------------------------------------------FUNCTIONS---------------------------------------------
class Function(Node, metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundFunction(Function):
    def __init__(self, name, parameters, statements):
        self.name = name
        self.parameters = parameters
        self.statements = statements

    def accept(self, visitor):
        return visitor.visit_compound_function(self)

class CompoundFunctionNoParams(Function):
    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

    def accept(self, visitor):
        return visitor.visit_compound_function_no_params(self)

