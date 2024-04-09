# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_declaration.
    def visitVariable_declaration(self, ctx:GrammarParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#type.
    def visitType(self, ctx:GrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignment.
    def visitAssignment(self, ctx:GrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#print_statement.
    def visitPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#read_statement.
    def visitRead_statement(self, ctx:GrammarParser.Read_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#if_statement.
    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#while_loop.
    def visitWhile_loop(self, ctx:GrammarParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_loop.
    def visitFor_loop(self, ctx:GrammarParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_declaration.
    def visitFunction_declaration(self, ctx:GrammarParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parameters.
    def visitParameters(self, ctx:GrammarParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parameter.
    def visitParameter(self, ctx:GrammarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#block.
    def visitBlock(self, ctx:GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#additive_expression.
    def visitAdditive_expression(self, ctx:GrammarParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:GrammarParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#unary_expression.
    def visitUnary_expression(self, ctx:GrammarParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#primary_expression.
    def visitPrimary_expression(self, ctx:GrammarParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arguments.
    def visitArguments(self, ctx:GrammarParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lexerError.
    def visitLexerError(self, ctx:GrammarParser.LexerErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parserError.
    def visitParserError(self, ctx:GrammarParser.ParserErrorContext):
        return self.visitChildren(ctx)



del GrammarParser