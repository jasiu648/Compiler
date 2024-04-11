from antlr4 import *
from GrammarListener import *
from LLVMGenerator import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser
    
class Listener(GrammarListener):

    declarations = {}
    variables = {}

    generator = LLVMGenerator()

    def add_item(dictionary, key, value):
        if key in dictionary:
            raise ValueError("Variable of name {key} already exists")
        else:
            dictionary[key] = value

    
    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        self.generator.generate()


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable_declaration.
    def enterVariable_declaration(self, ctx:GrammarParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable_declaration.
    def exitVariable_declaration(self, ctx:GrammarParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignment.
    def enterAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignment.
    def exitAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#print_statement.
    def enterPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#print_statement.
    def exitPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        self.generator.printf(ctx.expression)



    # Enter a parse tree produced by GrammarParser#read_statement.
    def enterRead_statement(self, ctx:GrammarParser.Read_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#read_statement.
    def exitRead_statement(self, ctx:GrammarParser.Read_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#if_statement.
    def enterIf_statement(self, ctx:GrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#if_statement.
    def exitIf_statement(self, ctx:GrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#while_loop.
    def enterWhile_loop(self, ctx:GrammarParser.While_loopContext):
        pass

    # Exit a parse tree produced by GrammarParser#while_loop.
    def exitWhile_loop(self, ctx:GrammarParser.While_loopContext):
        pass


    # Enter a parse tree produced by GrammarParser#for_loop.
    def enterFor_loop(self, ctx:GrammarParser.For_loopContext):
        pass

    # Exit a parse tree produced by GrammarParser#for_loop.
    def exitFor_loop(self, ctx:GrammarParser.For_loopContext):
        pass


    # Enter a parse tree produced by GrammarParser#function_declaration.
    def enterFunction_declaration(self, ctx:GrammarParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#function_declaration.
    def exitFunction_declaration(self, ctx:GrammarParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#parameters.
    def enterParameters(self, ctx:GrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by GrammarParser#parameters.
    def exitParameters(self, ctx:GrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by GrammarParser#parameter.
    def enterParameter(self, ctx:GrammarParser.ParameterContext):
        pass

    # Exit a parse tree produced by GrammarParser#parameter.
    def exitParameter(self, ctx:GrammarParser.ParameterContext):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#additive_expression.
    def enterAdditive_expression(self, ctx:GrammarParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#additive_expression.
    def exitAdditive_expression(self, ctx:GrammarParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:GrammarParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:GrammarParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#unary_expression.
    def enterUnary_expression(self, ctx:GrammarParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#unary_expression.
    def exitUnary_expression(self, ctx:GrammarParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#primary_expression.
    def enterPrimary_expression(self, ctx:GrammarParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#primary_expression.
    def exitPrimary_expression(self, ctx:GrammarParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#function_call.
    def enterFunction_call(self, ctx:GrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by GrammarParser#function_call.
    def exitFunction_call(self, ctx:GrammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by GrammarParser#arguments.
    def enterArguments(self, ctx:GrammarParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GrammarParser#arguments.
    def exitArguments(self, ctx:GrammarParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by GrammarParser#lexerError.
    def enterLexerError(self, ctx:GrammarParser.LexerErrorContext):
        pass

    # Exit a parse tree produced by GrammarParser#lexerError.
    def exitLexerError(self, ctx:GrammarParser.LexerErrorContext):
        pass


    # Enter a parse tree produced by GrammarParser#parserError.
    def enterParserError(self, ctx:GrammarParser.ParserErrorContext):
        pass

    # Exit a parse tree produced by GrammarParser#parserError.
    def exitParserError(self, ctx:GrammarParser.ParserErrorContext):
        pass
