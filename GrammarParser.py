# Generated from Grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,3,2,68,8,2,1,
        2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,3,9,105,8,9,1,9,1,9,1,9,1,9,3,9,111,8,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,3,10,120,8,10,1,10,1,10,1,10,1,11,1,11,1,11,
        5,11,128,8,11,10,11,12,11,131,9,11,1,12,1,12,1,12,1,13,1,13,5,13,
        138,8,13,10,13,12,13,141,9,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,
        5,15,150,8,15,10,15,12,15,153,9,15,1,16,1,16,1,16,5,16,158,8,16,
        10,16,12,16,161,9,16,1,17,1,17,1,17,3,17,166,8,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,3,18,177,8,18,1,19,1,19,1,19,3,19,
        182,8,19,1,19,1,19,1,20,1,20,1,20,5,20,189,8,20,10,20,12,20,192,
        9,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,0,3,1,0,1,3,1,0,16,17,1,0,18,20,199,0,45,1,0,0,0,2,61,1,
        0,0,0,4,63,1,0,0,0,6,71,1,0,0,0,8,73,1,0,0,0,10,78,1,0,0,0,12,82,
        1,0,0,0,14,86,1,0,0,0,16,95,1,0,0,0,18,101,1,0,0,0,20,115,1,0,0,
        0,22,124,1,0,0,0,24,132,1,0,0,0,26,135,1,0,0,0,28,144,1,0,0,0,30,
        146,1,0,0,0,32,154,1,0,0,0,34,165,1,0,0,0,36,176,1,0,0,0,38,178,
        1,0,0,0,40,185,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,
        45,43,1,0,0,0,45,46,1,0,0,0,46,1,1,0,0,0,47,45,1,0,0,0,48,62,3,4,
        2,0,49,62,3,8,4,0,50,62,3,10,5,0,51,62,3,12,6,0,52,62,3,14,7,0,53,
        62,3,16,8,0,54,62,3,18,9,0,55,62,3,20,10,0,56,57,5,11,0,0,57,58,
        3,28,14,0,58,59,5,34,0,0,59,62,1,0,0,0,60,62,3,26,13,0,61,48,1,0,
        0,0,61,49,1,0,0,0,61,50,1,0,0,0,61,51,1,0,0,0,61,52,1,0,0,0,61,53,
        1,0,0,0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,60,1,0,0,0,
        62,3,1,0,0,0,63,64,3,6,3,0,64,67,5,12,0,0,65,66,5,36,0,0,66,68,3,
        28,14,0,67,65,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,34,0,0,
        70,5,1,0,0,0,71,72,7,0,0,0,72,7,1,0,0,0,73,74,5,12,0,0,74,75,5,36,
        0,0,75,76,3,28,14,0,76,77,5,34,0,0,77,9,1,0,0,0,78,79,5,10,0,0,79,
        80,3,28,14,0,80,81,5,34,0,0,81,11,1,0,0,0,82,83,5,9,0,0,83,84,5,
        12,0,0,84,85,5,34,0,0,85,13,1,0,0,0,86,87,5,5,0,0,87,88,5,30,0,0,
        88,89,3,28,14,0,89,90,5,31,0,0,90,93,3,2,1,0,91,92,5,6,0,0,92,94,
        3,2,1,0,93,91,1,0,0,0,93,94,1,0,0,0,94,15,1,0,0,0,95,96,5,7,0,0,
        96,97,5,30,0,0,97,98,3,28,14,0,98,99,5,31,0,0,99,100,3,2,1,0,100,
        17,1,0,0,0,101,102,5,8,0,0,102,104,5,30,0,0,103,105,3,4,2,0,104,
        103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,34,0,0,107,
        108,3,28,14,0,108,110,5,34,0,0,109,111,3,8,4,0,110,109,1,0,0,0,110,
        111,1,0,0,0,111,112,1,0,0,0,112,113,5,31,0,0,113,114,3,2,1,0,114,
        19,1,0,0,0,115,116,3,6,3,0,116,117,5,12,0,0,117,119,5,30,0,0,118,
        120,3,22,11,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,
        122,5,31,0,0,122,123,3,26,13,0,123,21,1,0,0,0,124,129,3,24,12,0,
        125,126,5,35,0,0,126,128,3,24,12,0,127,125,1,0,0,0,128,131,1,0,0,
        0,129,127,1,0,0,0,129,130,1,0,0,0,130,23,1,0,0,0,131,129,1,0,0,0,
        132,133,3,6,3,0,133,134,5,12,0,0,134,25,1,0,0,0,135,139,5,32,0,0,
        136,138,3,2,1,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,
        139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,5,33,0,0,
        143,27,1,0,0,0,144,145,3,30,15,0,145,29,1,0,0,0,146,151,3,32,16,
        0,147,148,7,1,0,0,148,150,3,32,16,0,149,147,1,0,0,0,150,153,1,0,
        0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,31,1,0,0,0,153,151,1,0,0,
        0,154,159,3,34,17,0,155,156,7,2,0,0,156,158,3,34,17,0,157,155,1,
        0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,33,1,0,
        0,0,161,159,1,0,0,0,162,163,7,1,0,0,163,166,3,34,17,0,164,166,3,
        36,18,0,165,162,1,0,0,0,165,164,1,0,0,0,166,35,1,0,0,0,167,177,5,
        13,0,0,168,177,5,14,0,0,169,177,5,15,0,0,170,177,5,12,0,0,171,172,
        5,30,0,0,172,173,3,28,14,0,173,174,5,31,0,0,174,177,1,0,0,0,175,
        177,3,38,19,0,176,167,1,0,0,0,176,168,1,0,0,0,176,169,1,0,0,0,176,
        170,1,0,0,0,176,171,1,0,0,0,176,175,1,0,0,0,177,37,1,0,0,0,178,179,
        5,12,0,0,179,181,5,30,0,0,180,182,3,40,20,0,181,180,1,0,0,0,181,
        182,1,0,0,0,182,183,1,0,0,0,183,184,5,31,0,0,184,39,1,0,0,0,185,
        190,3,28,14,0,186,187,5,35,0,0,187,189,3,28,14,0,188,186,1,0,0,0,
        189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,41,1,0,0,0,192,
        190,1,0,0,0,15,45,61,67,93,104,110,119,129,139,151,159,165,176,181,
        190
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'matrix'", "'void'", 
                     "'if'", "'else'", "'while'", "'for'", "'read'", "'print'", 
                     "'return'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'!'", "'('", "')'", "'{'", "'}'", "';'", "','", "'='" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "MATRIX", "VOID", "IF", 
                      "ELSE", "WHILE", "FOR", "READ", "PRINT", "RETURN", 
                      "ID", "INT_CONSTANT", "FLOAT_CONSTANT", "MATRIX_CONSTANT", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "GT", "LTE", 
                      "GTE", "EQ", "NEQ", "AND", "OR", "NOT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", "COMMA", 
                      "ASSIGN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variable_declaration = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_print_statement = 5
    RULE_read_statement = 6
    RULE_if_statement = 7
    RULE_while_loop = 8
    RULE_for_loop = 9
    RULE_function_declaration = 10
    RULE_parameters = 11
    RULE_parameter = 12
    RULE_block = 13
    RULE_expression = 14
    RULE_additive_expression = 15
    RULE_multiplicative_expression = 16
    RULE_unary_expression = 17
    RULE_primary_expression = 18
    RULE_function_call = 19
    RULE_arguments = 20

    ruleNames =  [ "program", "statement", "variable_declaration", "type", 
                   "assignment", "print_statement", "read_statement", "if_statement", 
                   "while_loop", "for_loop", "function_declaration", "parameters", 
                   "parameter", "block", "expression", "additive_expression", 
                   "multiplicative_expression", "unary_expression", "primary_expression", 
                   "function_call", "arguments" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    MATRIX=3
    VOID=4
    IF=5
    ELSE=6
    WHILE=7
    FOR=8
    READ=9
    PRINT=10
    RETURN=11
    ID=12
    INT_CONSTANT=13
    FLOAT_CONSTANT=14
    MATRIX_CONSTANT=15
    ADD=16
    SUB=17
    MUL=18
    DIV=19
    MOD=20
    LT=21
    GT=22
    LTE=23
    GTE=24
    EQ=25
    NEQ=26
    AND=27
    OR=28
    NOT=29
    LPAREN=30
    RPAREN=31
    LBRACE=32
    RBRACE=33
    SEMICOLON=34
    COMMA=35
    ASSIGN=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294975406) != 0):
                self.state = 42
                self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(GrammarParser.Variable_declarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GrammarParser.AssignmentContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(GrammarParser.Print_statementContext,0)


        def read_statement(self):
            return self.getTypedRuleContext(GrammarParser.Read_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(GrammarParser.If_statementContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(GrammarParser.While_loopContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(GrammarParser.For_loopContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(GrammarParser.Function_declarationContext,0)


        def RETURN(self):
            return self.getToken(GrammarParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.read_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.while_loop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.for_loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 55
                self.function_declaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 56
                self.match(GrammarParser.RETURN)
                self.state = 57
                self.expression()
                self.state = 58
                self.match(GrammarParser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = GrammarParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.type_()
            self.state = 64
            self.match(GrammarParser.ID)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 65
                self.match(GrammarParser.ASSIGN)
                self.state = 66
                self.expression()


            self.state = 69
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def MATRIX(self):
            return self.getToken(GrammarParser.MATRIX, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(GrammarParser.ID)
            self.state = 74
            self.match(GrammarParser.ASSIGN)
            self.state = 75
            self.expression()
            self.state = 76
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GrammarParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = GrammarParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(GrammarParser.PRINT)
            self.state = 79
            self.expression()
            self.state = 80
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(GrammarParser.READ, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_read_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_statement" ):
                listener.enterRead_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_statement" ):
                listener.exitRead_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_statement" ):
                return visitor.visitRead_statement(self)
            else:
                return visitor.visitChildren(self)




    def read_statement(self):

        localctx = GrammarParser.Read_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_read_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GrammarParser.READ)
            self.state = 83
            self.match(GrammarParser.ID)
            self.state = 84
            self.match(GrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GrammarParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(GrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = GrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(GrammarParser.IF)
            self.state = 87
            self.match(GrammarParser.LPAREN)
            self.state = 88
            self.expression()
            self.state = 89
            self.match(GrammarParser.RPAREN)
            self.state = 90
            self.statement()
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(GrammarParser.ELSE)
                self.state = 92
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GrammarParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = GrammarParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(GrammarParser.WHILE)
            self.state = 96
            self.match(GrammarParser.LPAREN)
            self.state = 97
            self.expression()
            self.state = 98
            self.match(GrammarParser.RPAREN)
            self.state = 99
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GrammarParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(GrammarParser.Variable_declarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GrammarParser.AssignmentContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = GrammarParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(GrammarParser.FOR)
            self.state = 102
            self.match(GrammarParser.LPAREN)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 103
                self.variable_declaration()


            self.state = 106
            self.match(GrammarParser.SEMICOLON)
            self.state = 107
            self.expression()
            self.state = 108
            self.match(GrammarParser.SEMICOLON)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 109
                self.assignment()


            self.state = 112
            self.match(GrammarParser.RPAREN)
            self.state = 113
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(GrammarParser.ParametersContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = GrammarParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.type_()
            self.state = 116
            self.match(GrammarParser.ID)
            self.state = 117
            self.match(GrammarParser.LPAREN)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 118
                self.parameters()


            self.state = 121
            self.match(GrammarParser.RPAREN)
            self.state = 122
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ParameterContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = GrammarParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.parameter()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 125
                self.match(GrammarParser.COMMA)
                self.state = 126
                self.parameter()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = GrammarParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.type_()
            self.state = 133
            self.match(GrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(GrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GrammarParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(GrammarParser.LBRACE)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294975406) != 0):
                self.state = 136
                self.statement()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(GrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self):
            return self.getTypedRuleContext(GrammarParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.additive_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Multiplicative_expressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Multiplicative_expressionContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.ADD)
            else:
                return self.getToken(GrammarParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SUB)
            else:
                return self.getToken(GrammarParser.SUB, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expression" ):
                return visitor.visitAdditive_expression(self)
            else:
                return visitor.visitChildren(self)




    def additive_expression(self):

        localctx = GrammarParser.Additive_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_additive_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.multiplicative_expression()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.multiplicative_expression()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Unary_expressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Unary_expressionContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MUL)
            else:
                return self.getToken(GrammarParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.DIV)
            else:
                return self.getToken(GrammarParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.MOD)
            else:
                return self.getToken(GrammarParser.MOD, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expression" ):
                return visitor.visitMultiplicative_expression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative_expression(self):

        localctx = GrammarParser.Multiplicative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.unary_expression()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0):
                self.state = 155
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.unary_expression()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self):
            return self.getTypedRuleContext(GrammarParser.Unary_expressionContext,0)


        def ADD(self):
            return self.getToken(GrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)

        def primary_expression(self):
            return self.getTypedRuleContext(GrammarParser.Primary_expressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expression" ):
                return visitor.visitUnary_expression(self)
            else:
                return visitor.visitChildren(self)




    def unary_expression(self):

        localctx = GrammarParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unary_expression)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.unary_expression()
                pass
            elif token in [12, 13, 14, 15, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.primary_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_CONSTANT(self):
            return self.getToken(GrammarParser.INT_CONSTANT, 0)

        def FLOAT_CONSTANT(self):
            return self.getToken(GrammarParser.FLOAT_CONSTANT, 0)

        def MATRIX_CONSTANT(self):
            return self.getToken(GrammarParser.MATRIX_CONSTANT, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def function_call(self):
            return self.getTypedRuleContext(GrammarParser.Function_callContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = GrammarParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary_expression)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(GrammarParser.INT_CONSTANT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(GrammarParser.FLOAT_CONSTANT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.match(GrammarParser.MATRIX_CONSTANT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.match(GrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.match(GrammarParser.LPAREN)
                self.state = 172
                self.expression()
                self.state = 173
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 175
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(GrammarParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = GrammarParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(GrammarParser.ID)
            self.state = 179
            self.match(GrammarParser.LPAREN)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073999872) != 0):
                self.state = 180
                self.arguments()


            self.state = 183
            self.match(GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = GrammarParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.expression()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 186
                self.match(GrammarParser.COMMA)
                self.state = 187
                self.expression()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





