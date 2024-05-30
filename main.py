from antlr4 import *
from ExtendedListener import *
from antlr_generated.CSoftLexer import CSoftLexer
from antlr_generated.CSoftParser import CSoftParser
import sys

input_stream = FileStream(sys.argv[1])
lexer = CSoftLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CSoftParser(stream)
tree = parser.prog()
print(tree.toStringTree(recog=parser))
listener = ExtendedListener() 

walker = ParseTreeWalker()
walker.walk(listener, tree)

