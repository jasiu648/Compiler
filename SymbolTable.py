class SymbolTable:
    def __init__(self):
        # Initialize the symbol table as an empty dictionary
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
