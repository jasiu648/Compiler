from enum import Enum

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def add_item(dictionary, key, value):
        if key in dictionary:
            raise ValueError("Variable of name {key} already exists")
        else:
            dictionary[key] = value


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, type, value=None):

        if name in self.symbols:
            raise KeyError(f"Symbol '{name}' already exists.")
        self.symbols[name] = {'type': type, 'value': value}

    def lookup(self, name):

        return self.symbols.get(name, None)

    def delete(self, name):

        if name not in self.symbols:
            raise KeyError(f"Symbol '{name}' not found.")
        del self.symbols[name]

    def update(self, name, type=None, value=None):

        if name not in self.symbols:
            raise KeyError(f"Symbol '{name}' not found.")
        if type is not None:
            self.symbols[name]['type'] = type
        if value is not None:
            self.symbols[name]['value'] = value

    def __str__(self):

        symbols_str = "\n".join([f"{name}: {info}" for name, info in self.symbols.items()])
        return f"Symbol Table:\n{symbols_str}"
    

class ValueType:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class VariableType(Enum):
    INT = 1
    LONG = 2
    DOUBLE = 3
    BOOL = 4
    STRING = 5
    ARRAY = 6
    STRUCT = 7

def string_to_type(string):
    if string == "int":
        return VariableType.INT
    elif string == "long":
        return VariableType.LONG
    elif string == "double":
        return VariableType.DOUBLE
    elif string == 'bool' or string == VariableType.BOOL:
        return VariableType.BOOL
    elif string == 'string':
        return VariableType.STRING
    else:
       return string


def get_llvm_type_str(varTp):
    if varTp == VariableType.INT:
        return 'i32'
    elif varTp == VariableType.LONG:
        return 'i64'
    elif varTp == VariableType.DOUBLE:
        return 'double'
    elif varTp == VariableType.BOOL:
        return 'i1'
    elif varTp == VariableType.STRING:
        return 'i8*'

def llvm_to_type(varTp):
    if varTp == 'i32':
        return VariableType.INT
    elif varTp == 'i64':
        return VariableType.LONG
    elif varTp == 'double':
        return VariableType.DOUBLE
    elif varTp == 'i1':
        return VariableType.BOOL
    elif varTp == 'i8*':
        return VariableType.STRING