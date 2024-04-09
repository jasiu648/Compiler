from antlr4 import *

from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarListener import GrammarListener

# class MyListener(GrammarListener):
#     def enterStart(self, ctx:GrammarParser.StartContext):
#         print("Entering start rule")

#     def exitStart(self, ctx:GrammarParser.StartContext):
#         print("Exiting start rule")

#     def enterSomeRule(self, ctx:GrammarParser.SomeRuleContext):
#         print("Entering someRule")

#     def exitSomeRule(self, ctx:GrammarParser.SomeRuleContext):
#         print("Exiting someRule")

def main():
    # Load the input file
    input_stream = FileStream("input.txt")

    # Create lexer and parser
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)

    # Add custom listener
    listener = GrammarListener()
    parser.addParseListener(listener)

    # Start parsing
    tree = parser.program()

    # You can traverse the tree and do more processing if needed
    # For example, printing the tree:
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
