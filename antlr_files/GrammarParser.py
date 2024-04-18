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
        4,1,40,218,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,70,8,1,1,2,1,2,1,2,1,2,3,2,76,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,106,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,3,9,118,8,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,126,8,10,10,
        10,12,10,129,9,10,1,11,1,11,1,11,1,12,1,12,5,12,136,8,12,10,12,12,
        12,139,9,12,1,12,1,12,1,13,1,13,3,13,145,8,13,1,14,3,14,148,8,14,
        1,14,1,14,1,14,5,14,153,8,14,10,14,12,14,156,9,14,1,15,1,15,1,15,
        1,15,1,15,3,15,163,8,15,1,16,1,16,1,16,5,16,168,8,16,10,16,12,16,
        171,9,16,1,16,1,16,1,17,1,17,1,17,3,17,178,8,17,1,18,1,18,1,18,3,
        18,183,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,193,8,19,
        1,20,1,20,1,21,1,21,1,21,3,21,200,8,21,1,21,1,21,1,22,1,22,1,22,
        5,22,207,8,22,10,22,12,22,210,9,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,0,7,1,0,1,4,1,0,15,17,1,0,29,31,1,0,23,28,1,0,
        18,19,1,0,20,22,2,0,5,6,17,17,220,0,53,1,0,0,0,2,69,1,0,0,0,4,71,
        1,0,0,0,6,79,1,0,0,0,8,81,1,0,0,0,10,86,1,0,0,0,12,92,1,0,0,0,14,
        98,1,0,0,0,16,107,1,0,0,0,18,113,1,0,0,0,20,122,1,0,0,0,22,130,1,
        0,0,0,24,133,1,0,0,0,26,144,1,0,0,0,28,147,1,0,0,0,30,162,1,0,0,
        0,32,169,1,0,0,0,34,174,1,0,0,0,36,182,1,0,0,0,38,192,1,0,0,0,40,
        194,1,0,0,0,42,196,1,0,0,0,44,203,1,0,0,0,46,211,1,0,0,0,48,214,
        1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,
        53,54,1,0,0,0,54,1,1,0,0,0,55,53,1,0,0,0,56,70,3,4,2,0,57,70,3,8,
        4,0,58,70,3,10,5,0,59,70,3,12,6,0,60,70,3,14,7,0,61,70,3,16,8,0,
        62,70,3,18,9,0,63,64,5,14,0,0,64,65,3,26,13,0,65,66,5,37,0,0,66,
        70,1,0,0,0,67,70,3,24,12,0,68,70,3,42,21,0,69,56,1,0,0,0,69,57,1,
        0,0,0,69,58,1,0,0,0,69,59,1,0,0,0,69,60,1,0,0,0,69,61,1,0,0,0,69,
        62,1,0,0,0,69,63,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,3,1,0,0,
        0,71,72,3,6,3,0,72,75,5,17,0,0,73,74,5,39,0,0,74,76,3,26,13,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,37,0,0,78,5,1,0,0,
        0,79,80,7,0,0,0,80,7,1,0,0,0,81,82,5,17,0,0,82,83,5,39,0,0,83,84,
        3,26,13,0,84,85,5,37,0,0,85,9,1,0,0,0,86,87,5,13,0,0,87,88,5,33,
        0,0,88,89,7,1,0,0,89,90,5,34,0,0,90,91,5,37,0,0,91,11,1,0,0,0,92,
        93,5,12,0,0,93,94,5,33,0,0,94,95,5,17,0,0,95,96,5,34,0,0,96,97,5,
        37,0,0,97,13,1,0,0,0,98,99,5,8,0,0,99,100,5,33,0,0,100,101,3,28,
        14,0,101,102,5,34,0,0,102,105,3,24,12,0,103,104,5,9,0,0,104,106,
        3,24,12,0,105,103,1,0,0,0,105,106,1,0,0,0,106,15,1,0,0,0,107,108,
        5,10,0,0,108,109,5,33,0,0,109,110,3,28,14,0,110,111,5,34,0,0,111,
        112,3,24,12,0,112,17,1,0,0,0,113,114,3,6,3,0,114,115,5,17,0,0,115,
        117,5,33,0,0,116,118,3,20,10,0,117,116,1,0,0,0,117,118,1,0,0,0,118,
        119,1,0,0,0,119,120,5,34,0,0,120,121,3,24,12,0,121,19,1,0,0,0,122,
        127,3,22,11,0,123,124,5,38,0,0,124,126,3,22,11,0,125,123,1,0,0,0,
        126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,21,1,0,0,0,129,
        127,1,0,0,0,130,131,3,6,3,0,131,132,5,17,0,0,132,23,1,0,0,0,133,
        137,5,35,0,0,134,136,3,2,1,0,135,134,1,0,0,0,136,139,1,0,0,0,137,
        135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,137,1,0,0,0,140,
        141,5,36,0,0,141,25,1,0,0,0,142,145,3,28,14,0,143,145,3,32,16,0,
        144,142,1,0,0,0,144,143,1,0,0,0,145,27,1,0,0,0,146,148,5,32,0,0,
        147,146,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,154,3,30,15,
        0,150,151,7,2,0,0,151,153,3,28,14,0,152,150,1,0,0,0,153,156,1,0,
        0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,29,1,0,0,0,156,154,1,0,0,
        0,157,163,3,40,20,0,158,159,3,32,16,0,159,160,7,3,0,0,160,161,3,
        32,16,0,161,163,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,0,163,31,1,
        0,0,0,164,165,3,34,17,0,165,166,7,4,0,0,166,168,1,0,0,0,167,164,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,
        1,0,0,0,171,169,1,0,0,0,172,173,3,34,17,0,173,33,1,0,0,0,174,177,
        3,36,18,0,175,176,7,5,0,0,176,178,3,34,17,0,177,175,1,0,0,0,177,
        178,1,0,0,0,178,35,1,0,0,0,179,180,7,4,0,0,180,183,3,36,18,0,181,
        183,3,38,19,0,182,179,1,0,0,0,182,181,1,0,0,0,183,37,1,0,0,0,184,
        193,5,15,0,0,185,193,5,16,0,0,186,193,5,17,0,0,187,188,5,33,0,0,
        188,189,3,26,13,0,189,190,5,34,0,0,190,193,1,0,0,0,191,193,3,42,
        21,0,192,184,1,0,0,0,192,185,1,0,0,0,192,186,1,0,0,0,192,187,1,0,
        0,0,192,191,1,0,0,0,193,39,1,0,0,0,194,195,7,6,0,0,195,41,1,0,0,
        0,196,197,5,17,0,0,197,199,5,33,0,0,198,200,3,44,22,0,199,198,1,
        0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,202,5,34,0,0,202,43,1,
        0,0,0,203,208,3,26,13,0,204,205,5,38,0,0,205,207,3,26,13,0,206,204,
        1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,45,1,
        0,0,0,210,208,1,0,0,0,211,212,9,0,0,0,212,213,6,23,-1,0,213,47,1,
        0,0,0,214,215,9,0,0,0,215,216,6,24,-1,0,216,49,1,0,0,0,17,53,69,
        75,105,117,127,137,144,147,154,162,169,177,182,192,199,208
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'matrix'", "'bool'", 
                     "'true'", "'false'", "'void'", "'if'", "'else'", "'while'", 
                     "'for'", "'read'", "'print'", "'return'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
                     "'&&'", "'||'", "'^'", "'!'", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "'='" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "MATRIX", "BOOL", "TRUE", 
                      "FALSE", "VOID", "IF", "ELSE", "WHILE", "FOR", "READ", 
                      "PRINT", "RETURN", "INT_CONSTANT", "FLOAT_CONSTANT", 
                      "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "GT", 
                      "LTE", "GTE", "EQ", "NEQ", "AND", "OR", "XOR", "NOT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", 
                      "COMMA", "ASSIGN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variable_declaration = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_print_statement = 5
    RULE_read_statement = 6
    RULE_if_statement = 7
    RULE_while_loop = 8
    RULE_function_declaration = 9
    RULE_parameters = 10
    RULE_parameter = 11
    RULE_block = 12
    RULE_expression = 13
    RULE_boolean_expression = 14
    RULE_primary_boolean_expression = 15
    RULE_additive_expression = 16
    RULE_multiplicative_expression = 17
    RULE_unary_expression = 18
    RULE_primary_expression = 19
    RULE_bool = 20
    RULE_function_call = 21
    RULE_arguments = 22
    RULE_lexerError = 23
    RULE_parserError = 24

    ruleNames =  [ "program", "statement", "variable_declaration", "type", 
                   "assignment", "print_statement", "read_statement", "if_statement", 
                   "while_loop", "function_declaration", "parameters", "parameter", 
                   "block", "expression", "boolean_expression", "primary_boolean_expression", 
                   "additive_expression", "multiplicative_expression", "unary_expression", 
                   "primary_expression", "bool", "function_call", "arguments", 
                   "lexerError", "parserError" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    MATRIX=3
    BOOL=4
    TRUE=5
    FALSE=6
    VOID=7
    IF=8
    ELSE=9
    WHILE=10
    FOR=11
    READ=12
    PRINT=13
    RETURN=14
    INT_CONSTANT=15
    FLOAT_CONSTANT=16
    ID=17
    ADD=18
    SUB=19
    MUL=20
    DIV=21
    MOD=22
    LT=23
    GT=24
    LTE=25
    GTE=26
    EQ=27
    NEQ=28
    AND=29
    OR=30
    XOR=31
    NOT=32
    LPAREN=33
    RPAREN=34
    LBRACE=35
    RBRACE=36
    SEMICOLON=37
    COMMA=38
    ASSIGN=39
    WS=40

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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359899422) != 0):
                self.state = 50
                self.statement()
                self.state = 55
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


        def function_call(self):
            return self.getTypedRuleContext(GrammarParser.Function_callContext,0)


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
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.read_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.while_loop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.function_declaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.match(GrammarParser.RETURN)
                self.state = 64
                self.expression()
                self.state = 65
                self.match(GrammarParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 67
                self.block()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 68
                self.function_call()
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
            self.state = 71
            self.type_()
            self.state = 72
            self.match(GrammarParser.ID)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 73
                self.match(GrammarParser.ASSIGN)
                self.state = 74
                self.expression()


            self.state = 77
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

        def BOOL(self):
            return self.getToken(GrammarParser.BOOL, 0)

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
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
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
            self.state = 81
            self.match(GrammarParser.ID)
            self.state = 82
            self.match(GrammarParser.ASSIGN)
            self.state = 83
            self.expression()
            self.state = 84
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

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def INT_CONSTANT(self):
            return self.getToken(GrammarParser.INT_CONSTANT, 0)

        def FLOAT_CONSTANT(self):
            return self.getToken(GrammarParser.FLOAT_CONSTANT, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(GrammarParser.PRINT)
            self.state = 87
            self.match(GrammarParser.LPAREN)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
            self.match(GrammarParser.RPAREN)
            self.state = 90
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

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

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
            self.state = 92
            self.match(GrammarParser.READ)
            self.state = 93
            self.match(GrammarParser.LPAREN)
            self.state = 94
            self.match(GrammarParser.ID)
            self.state = 95
            self.match(GrammarParser.RPAREN)
            self.state = 96
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

        def boolean_expression(self):
            return self.getTypedRuleContext(GrammarParser.Boolean_expressionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BlockContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(GrammarParser.IF)
            self.state = 99
            self.match(GrammarParser.LPAREN)
            self.state = 100
            self.boolean_expression()
            self.state = 101
            self.match(GrammarParser.RPAREN)
            self.state = 102
            self.block()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 103
                self.match(GrammarParser.ELSE)
                self.state = 104
                self.block()


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

        def boolean_expression(self):
            return self.getTypedRuleContext(GrammarParser.Boolean_expressionContext,0)


        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


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
            self.state = 107
            self.match(GrammarParser.WHILE)
            self.state = 108
            self.match(GrammarParser.LPAREN)
            self.state = 109
            self.boolean_expression()
            self.state = 110
            self.match(GrammarParser.RPAREN)
            self.state = 111
            self.block()
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
        self.enterRule(localctx, 18, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.type_()
            self.state = 114
            self.match(GrammarParser.ID)
            self.state = 115
            self.match(GrammarParser.LPAREN)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 116
                self.parameters()


            self.state = 119
            self.match(GrammarParser.RPAREN)
            self.state = 120
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
        self.enterRule(localctx, 20, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.parameter()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 123
                self.match(GrammarParser.COMMA)
                self.state = 124
                self.parameter()
                self.state = 129
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
        self.enterRule(localctx, 22, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.type_()
            self.state = 131
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
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(GrammarParser.LBRACE)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359899422) != 0):
                self.state = 134
                self.statement()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
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

        def boolean_expression(self):
            return self.getTypedRuleContext(GrammarParser.Boolean_expressionContext,0)


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
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.boolean_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.additive_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_boolean_expression(self):
            return self.getTypedRuleContext(GrammarParser.Primary_boolean_expressionContext,0)


        def NOT(self):
            return self.getToken(GrammarParser.NOT, 0)

        def boolean_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Boolean_expressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Boolean_expressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.AND)
            else:
                return self.getToken(GrammarParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.OR)
            else:
                return self.getToken(GrammarParser.OR, i)

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.XOR)
            else:
                return self.getToken(GrammarParser.XOR, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_boolean_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_expression" ):
                listener.enterBoolean_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_expression" ):
                listener.exitBoolean_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expression" ):
                return visitor.visitBoolean_expression(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expression(self):

        localctx = GrammarParser.Boolean_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolean_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 146
                self.match(GrammarParser.NOT)


            self.state = 149
            self.primary_boolean_expression()
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 150
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 151
                    self.boolean_expression() 
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_boolean_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_(self):
            return self.getTypedRuleContext(GrammarParser.BoolContext,0)


        def additive_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Additive_expressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Additive_expressionContext,i)


        def LT(self):
            return self.getToken(GrammarParser.LT, 0)

        def GT(self):
            return self.getToken(GrammarParser.GT, 0)

        def LTE(self):
            return self.getToken(GrammarParser.LTE, 0)

        def GTE(self):
            return self.getToken(GrammarParser.GTE, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def NEQ(self):
            return self.getToken(GrammarParser.NEQ, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_primary_boolean_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_boolean_expression" ):
                listener.enterPrimary_boolean_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_boolean_expression" ):
                listener.exitPrimary_boolean_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_boolean_expression" ):
                return visitor.visitPrimary_boolean_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_boolean_expression(self):

        localctx = GrammarParser.Primary_boolean_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primary_boolean_expression)
        self._la = 0 # Token type
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.bool_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.additive_expression()
                self.state = 159
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self.additive_expression()
                pass


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
        self.enterRule(localctx, 32, self.RULE_additive_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 164
                    self.multiplicative_expression()
                    self.state = 165
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 172
            self.multiplicative_expression()
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

        def unary_expression(self):
            return self.getTypedRuleContext(GrammarParser.Unary_expressionContext,0)


        def multiplicative_expression(self):
            return self.getTypedRuleContext(GrammarParser.Multiplicative_expressionContext,0)


        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

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
        self.enterRule(localctx, 34, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.unary_expression()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0):
                self.state = 175
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.multiplicative_expression()


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
        self.enterRule(localctx, 36, self.RULE_unary_expression)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 180
                self.unary_expression()
                pass
            elif token in [15, 16, 17, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
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
        self.enterRule(localctx, 38, self.RULE_primary_expression)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(GrammarParser.INT_CONSTANT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(GrammarParser.FLOAT_CONSTANT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(GrammarParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.match(GrammarParser.LPAREN)
                self.state = 188
                self.expression()
                self.state = 189
                self.match(GrammarParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(GrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GrammarParser.FALSE, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = GrammarParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 131168) != 0)):
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
        self.enterRule(localctx, 42, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(GrammarParser.ID)
            self.state = 197
            self.match(GrammarParser.LPAREN)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 12885917792) != 0):
                self.state = 198
                self.arguments()


            self.state = 201
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
        self.enterRule(localctx, 44, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expression()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 204
                self.match(GrammarParser.COMMA)
                self.state = 205
                self.expression()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerErrorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_lexerError

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerError" ):
                listener.enterLexerError(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerError" ):
                listener.exitLexerError(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerError" ):
                return visitor.visitLexerError(self)
            else:
                return visitor.visitChildren(self)




    def lexerError(self):

        localctx = GrammarParser.LexerErrorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_lexerError)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.matchWildcard()
            emitErrorMessage("Lexer error at line " + getLine() + ", column " + getCharPositionInLine() + ": " + getText());
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParserErrorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_parserError

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParserError" ):
                listener.enterParserError(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParserError" ):
                listener.exitParserError(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserError" ):
                return visitor.visitParserError(self)
            else:
                return visitor.visitChildren(self)




    def parserError(self):

        localctx = GrammarParser.ParserErrorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parserError)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.matchWildcard()
            emitErrorMessage("Parser error at line " + getLine() + ", column " + getCharPositionInLine() + ": " + getText());
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





