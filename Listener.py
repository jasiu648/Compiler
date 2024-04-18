from antlr4 import *
from GrammarListener import *
from LLVMGenerator import *
from utils import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser


class Listener(GrammarListener):

    declarations = {}
    variables = {}
    stack = Stack()
    global_scope = True
    generator = LLVMGenerator()
    
    
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
        id = str(ctx.ID())
        if(id in self.variables):
            print(f"Variable {id} already declared")
            return

        if(ctx.ASSIGN()):
            self.variables[id] = 0
        else:
            self.variables[id] = 1

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
        if(ctx.INT_CONSTANT() is not None):
            self.generator.printf(str(ctx.INT_CONSTANT()))
        elif(ctx.FLOAT_CONSTANT() is not None):
            self.generator.printf(str(ctx.FLOAT_CONSTANT()))
        elif(ctx.ID() is not None):
            self.generator.printf_id(str(ctx.ID()))



    # Enter a parse tree produced by GrammarParser#read_statement.
    def enterRead_statement(self, ctx:GrammarParser.Read_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#read_statement.
    def exitRead_statement(self, ctx:GrammarParser.Read_statementContext):
        id = str(ctx.ID())

        if(id not in self.variables):
            self.variables[id] = 1
            self.generator.declare_int(id)
        self.generator.read(id)


    # Enter a parse tree produced by GrammarParser#if_statement.
    def enterIf_statement(self, ctx:GrammarParser.If_statementContext):
        print(ctx.boolean_expression())
        self.generator.if_start()

    # Exit a parse tree produced by GrammarParser#if_statement.
    def exitIf_statement(self, ctx:GrammarParser.If_statementContext):
        print(ctx.boolean_expression())
        self.generator.if_end()


    # Enter a parse tree produced by GrammarParser#while_loop.
    def enterWhile_loop(self, ctx:GrammarParser.While_loopContext):
        pass

    # Exit a parse tree produced by GrammarParser#while_loop.
    def exitWhile_loop(self, ctx:GrammarParser.While_loopContext):
        pass


    # Enter a parse tree produced by GrammarParser#function_declaration.
    def enterFunction_declaration(self, ctx:GrammarParser.Function_declarationContext):
        self.generator.func_decl_int(str(ctx.ID()))

    # Exit a parse tree produced by GrammarParser#function_declaration.
    def exitFunction_declaration(self, ctx:GrammarParser.Function_declarationContext):
        self.generator.func_return_int()


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
        if(ctx.INT_CONSTANT()):
            self.stack.push(str(ctx.INT_CONSTANT()))
        elif(ctx.FLOAT_CONSTANT()):
            self.stack.push(str(ctx.FLOAT_CONSTANT()))

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
