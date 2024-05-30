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
    

class Value:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class VarType(Enum):
    INT32 = 1
    INT64 = 2
    FLOAT32 = 3
    DOUBLE = 4
    BOOL = 5
    STRING = 6
    ARRAY = 7
    STRUCT = 8

def string_to_type(string):
    if string == "int32":
        return VarType.INT32
    elif string == "int64":
        return VarType.INT64
    elif string == "float32":
        return VarType.FLOAT32
    elif string == "double":
        return VarType.DOUBLE
    elif string == 'bool' or string == VarType.BOOL:
        return VarType.BOOL
    elif string == 'string':
        return VarType.STRING
    else:
       return string


def get_llvm_type_str(varTp):
    if varTp == VarType.INT32:
        return 'i32'
    elif varTp == VarType.INT64:
        return 'i64'
    elif varTp == VarType.FLOAT32:
        return 'float'
    elif varTp == VarType.DOUBLE:
        return 'double'
    elif varTp == VarType.BOOL:
        return 'i1'
    elif varTp == VarType.STRING:
        return 'i8*'
    # elif varTp == VarType.ARRAY:
    #     return ''

def llvm_to_type(varTp):
    if varTp == 'i32':
        return VarType.INT32
    elif varTp == 'i64':
        return VarType.INT64
    elif varTp == 'float':
        return VarType.FLOAT32
    elif varTp == 'double':
        return VarType.DOUBLE
    elif varTp == 'i1':
        return VarType.BOOL
    elif varTp == 'i8*':
        return VarType.STRING
    # elif varTp == VarType.ARRAY:
    #     return ''