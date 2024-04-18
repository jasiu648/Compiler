from antlr4 import *

from antlr_files.GrammarLexer import GrammarLexer
from antlr_files.GrammarParser import GrammarParser
from antlr_files.GrammarListener import GrammarListener
from Listener import Listener
import sys

def main():
    # Load the input file
    input_stream = FileStream(sys.argv[1])

    # Create lexer and parser
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)

    # Add custom listener
    listener = Listener()
    parser.addParseListener(listener)

    # Start parsing
    tree = parser.program()
    #print(listener.variables)
   
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
