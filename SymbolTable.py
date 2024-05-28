class SymbolTable:
    def __init__(self):
        # Initialize the symbol table as an empty dictionary
        self.symbols = {}

    def insert(self, name, type, value=None):
        """
        Insert a new symbol into the symbol table.
        
        Parameters:
        name (str): The name of the symbol.
        type (str): The type of the symbol (e.g., 'int', 'float', 'function').
        value (any): The value of the symbol (optional).
        """
        if name in self.symbols:
            raise KeyError(f"Symbol '{name}' already exists.")
        self.symbols[name] = {'type': type, 'value': value}

    def lookup(self, name):
        """
        Lookup a symbol in the symbol table.
        
        Parameters:
        name (str): The name of the symbol to lookup.
        
        Returns:
        dict: A dictionary with the type and value of the symbol if found, else None.
        """
        return self.symbols.get(name, None)

    def delete(self, name):
        """
        Delete a symbol from the symbol table.
        
        Parameters:
        name (str): The name of the symbol to delete.
        """
        if name not in self.symbols:
            raise KeyError(f"Symbol '{name}' not found.")
        del self.symbols[name]

    def update(self, name, type=None, value=None):
        """
        Update the type or value of an existing symbol in the symbol table.
        
        Parameters:
        name (str): The name of the symbol to update.
        type (str): The new type of the symbol (optional).
        value (any): The new value of the symbol (optional).
        """
        if name not in self.symbols:
            raise KeyError(f"Symbol '{name}' not found.")
        if type is not None:
            self.symbols[name]['type'] = type
        if value is not None:
            self.symbols[name]['value'] = value

    def __str__(self):
        """
        Return a string representation of the symbol table.
        """
        symbols_str = "\n".join([f"{name}: {info}" for name, info in self.symbols.items()])
        return f"Symbol Table:\n{symbols_str}"

# Example usage
if __name__ == "__main__":
    sym_table = SymbolTable()
    sym_table.insert("x", "int", 10)
    sym_table.insert("y", "float", 20.5)
    sym_table.insert("func", "function", 'int')

    print(sym_table)
    print(sym_table.lookup("x"))
    sym_table.update("x", value=15)
    print(sym_table.lookup("x"))
    sym_table.delete("y")
    print(sym_table)
