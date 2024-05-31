// Generated from //wsl.localhost/Ubuntu-22.04/home/jihyo/Compiler/antlr_generated/CSoft.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CSoftParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, COMMA=7, DOT=8, LPAREN=9, 
		RPAREN=10, LBRACE=11, RBRACE=12, LBRACKET=13, RBRACKET=14, PRINT=15, READ=16, 
		IF=17, WHILE=18, STRUCT=19, CLASS=20, BOOL=21, REPEAT=22, ASSIGN=23, INT=24, 
		FLOAT=25, AddOper=26, MultOper=27, NegOper=28, RelOper=29, AndOper=30, 
		OrOper=31, XorOper=32, COMMENT=33, ID=34, STRING=35, WS=36;
	public static final int
		RULE_type = 0, RULE_prog = 1, RULE_statement = 2, RULE_ident = 3, RULE_assignment = 4, 
		RULE_print_statement = 5, RULE_read_statement = 6, RULE_arrayAssign = 7, 
		RULE_expr = 8, RULE_condXorStm = 9, RULE_condStmAnd = 10, RULE_condStmRel = 11, 
		RULE_addExpr = 12, RULE_multExpr = 13, RULE_negFactor = 14, RULE_factor = 15, 
		RULE_ifStm = 16, RULE_blockIf = 17, RULE_repeatStm = 18, RULE_repNum = 19, 
		RULE_blockRepeat = 20, RULE_whileL = 21, RULE_blockWhile = 22, RULE_function = 23, 
		RULE_blockFun = 24, RULE_classDecl = 25, RULE_blockClass = 26, RULE_method = 27, 
		RULE_blockMethod = 28, RULE_methodType = 29, RULE_methodName = 30, RULE_className = 31, 
		RULE_methodCall = 32, RULE_classAssign = 33, RULE_parameters = 34, RULE_parameter = 35, 
		RULE_structDecl = 36, RULE_blockStruct = 37, RULE_structVarDecl = 38, 
		RULE_structAssign = 39, RULE_structFieldAssign = 40, RULE_structFieldAccess = 41, 
		RULE_arrayAccess = 42, RULE_funcCall = 43, RULE_funType = 44, RULE_funName = 45, 
		RULE_structName = 46;
	private static String[] makeRuleNames() {
		return new String[] {
			"type", "prog", "statement", "ident", "assignment", "print_statement", 
			"read_statement", "arrayAssign", "expr", "condXorStm", "condStmAnd", 
			"condStmRel", "addExpr", "multExpr", "negFactor", "factor", "ifStm", 
			"blockIf", "repeatStm", "repNum", "blockRepeat", "whileL", "blockWhile", 
			"function", "blockFun", "classDecl", "blockClass", "method", "blockMethod", 
			"methodType", "methodName", "className", "methodCall", "classAssign", 
			"parameters", "parameter", "structDecl", "blockStruct", "structVarDecl", 
			"structAssign", "structFieldAssign", "structFieldAccess", "arrayAccess", 
			"funcCall", "funType", "funName", "structName"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'double'", "'int'", "'long'", "'bool'", "'string'", "'()'", "','", 
			"'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'print'", "'read'", 
			"'if'", "'while'", "'struct'", "'class'", null, "'repeat'", "'='", null, 
			null, null, null, "'!'", null, "'&&'", "'||'", "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "COMMA", "DOT", "LPAREN", "RPAREN", 
			"LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "PRINT", "READ", "IF", "WHILE", 
			"STRUCT", "CLASS", "BOOL", "REPEAT", "ASSIGN", "INT", "FLOAT", "AddOper", 
			"MultOper", "NegOper", "RelOper", "AndOper", "OrOper", "XorOper", "COMMENT", 
			"ID", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CSoft.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CSoftParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CSoftParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 51866730558L) != 0)) {
				{
				{
				setState(96);
				statement();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(102);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StructDeclarationContext extends StatementContext {
		public StructDeclContext structDecl() {
			return getRuleContext(StructDeclContext.class,0);
		}
		public StructDeclarationContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileLoopContext extends StatementContext {
		public WhileLContext whileL() {
			return getRuleContext(WhileLContext.class,0);
		}
		public WhileLoopContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReadContext extends StatementContext {
		public Read_statementContext read_statement() {
			return getRuleContext(Read_statementContext.class,0);
		}
		public ReadContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RepeatStatementContext extends StatementContext {
		public RepeatStmContext repeatStm() {
			return getRuleContext(RepeatStmContext.class,0);
		}
		public RepeatStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ElementAssignContext extends StatementContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode LBRACKET() { return getToken(CSoftParser.LBRACKET, 0); }
		public TerminalNode INT() { return getToken(CSoftParser.INT, 0); }
		public TerminalNode RBRACKET() { return getToken(CSoftParser.RBRACKET, 0); }
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ElementAssignContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprressionContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprressionContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StructAssignmetContext extends StatementContext {
		public StructAssignContext structAssign() {
			return getRuleContext(StructAssignContext.class,0);
		}
		public StructAssignmetContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends StatementContext {
		public IfStmContext ifStm() {
			return getRuleContext(IfStmContext.class,0);
		}
		public IfStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ClassDeclarationContext extends StatementContext {
		public ClassDeclContext classDecl() {
			return getRuleContext(ClassDeclContext.class,0);
		}
		public ClassDeclarationContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends StatementContext {
		public Print_statementContext print_statement() {
			return getRuleContext(Print_statementContext.class,0);
		}
		public PrintContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ClassAssignmentContext extends StatementContext {
		public ClassAssignContext classAssign() {
			return getRuleContext(ClassAssignContext.class,0);
		}
		public ClassAssignmentContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncDeclContext extends StatementContext {
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public FuncDeclContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends StatementContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArrAssignContext extends StatementContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public ArrayAssignContext arrayAssign() {
			return getRuleContext(ArrayAssignContext.class,0);
		}
		public ArrAssignContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StructFieldAssignmentContext extends StatementContext {
		public StructFieldAssignContext structFieldAssign() {
			return getRuleContext(StructFieldAssignContext.class,0);
		}
		public StructFieldAssignmentContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new PrintContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(104);
				print_statement();
				}
				break;
			case 2:
				_localctx = new ReadContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				read_statement();
				}
				break;
			case 3:
				_localctx = new ExprressionContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(106);
				expr();
				}
				break;
			case 4:
				_localctx = new AssignContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(107);
				ident();
				setState(108);
				match(ASSIGN);
				setState(109);
				expr();
				}
				break;
			case 5:
				_localctx = new ElementAssignContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(111);
				match(ID);
				setState(112);
				match(LBRACKET);
				setState(113);
				match(INT);
				setState(114);
				match(RBRACKET);
				setState(115);
				match(ASSIGN);
				setState(116);
				expr();
				}
				break;
			case 6:
				_localctx = new ArrAssignContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(117);
				ident();
				setState(118);
				match(ASSIGN);
				setState(119);
				arrayAssign();
				}
				break;
			case 7:
				_localctx = new RepeatStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(121);
				repeatStm();
				}
				break;
			case 8:
				_localctx = new IfStatementContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(122);
				ifStm();
				}
				break;
			case 9:
				_localctx = new WhileLoopContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(123);
				whileL();
				}
				break;
			case 10:
				_localctx = new FuncDeclContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(124);
				function();
				}
				break;
			case 11:
				_localctx = new StructDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(125);
				structDecl();
				}
				break;
			case 12:
				_localctx = new StructFieldAssignmentContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(126);
				structFieldAssign();
				}
				break;
			case 13:
				_localctx = new StructAssignmetContext(_localctx);
				enterOuterAlt(_localctx, 13);
				{
				setState(127);
				structAssign();
				}
				break;
			case 14:
				_localctx = new ClassDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 14);
				{
				setState(128);
				classDecl();
				}
				break;
			case 15:
				_localctx = new ClassAssignmentContext(_localctx);
				enterOuterAlt(_localctx, 15);
				{
				setState(129);
				classAssign();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ident);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) {
				{
				setState(132);
				type();
				}
			}

			setState(135);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			ident();
			setState(138);
			match(ASSIGN);
			setState(139);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_statementContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(CSoftParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(CSoftParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(CSoftParser.RPAREN, 0); }
		public Print_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_statement; }
	}

	public final Print_statementContext print_statement() throws RecognitionException {
		Print_statementContext _localctx = new Print_statementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_print_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(PRINT);
			setState(142);
			match(LPAREN);
			setState(143);
			match(ID);
			setState(144);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Read_statementContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(CSoftParser.READ, 0); }
		public TerminalNode LPAREN() { return getToken(CSoftParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(CSoftParser.RPAREN, 0); }
		public Read_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_statement; }
	}

	public final Read_statementContext read_statement() throws RecognitionException {
		Read_statementContext _localctx = new Read_statementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_read_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(READ);
			setState(147);
			match(LPAREN);
			setState(148);
			match(ID);
			setState(149);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayAssignContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(CSoftParser.LBRACKET, 0); }
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TerminalNode RBRACKET() { return getToken(CSoftParser.RBRACKET, 0); }
		public List<TerminalNode> COMMA() { return getTokens(CSoftParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSoftParser.COMMA, i);
		}
		public ArrayAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayAssign; }
	}

	public final ArrayAssignContext arrayAssign() throws RecognitionException {
		ArrayAssignContext _localctx = new ArrayAssignContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_arrayAssign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(LBRACKET);
			setState(152);
			factor();
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(153);
				match(COMMA);
				setState(154);
				factor();
				}
				}
				setState(159);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(160);
			match(RBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<CondXorStmContext> condXorStm() {
			return getRuleContexts(CondXorStmContext.class);
		}
		public CondXorStmContext condXorStm(int i) {
			return getRuleContext(CondXorStmContext.class,i);
		}
		public TerminalNode OrOper() { return getToken(CSoftParser.OrOper, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expr);
		try {
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				condXorStm();
				setState(163);
				match(OrOper);
				setState(164);
				condXorStm();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(166);
				condXorStm();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondXorStmContext extends ParserRuleContext {
		public List<CondStmAndContext> condStmAnd() {
			return getRuleContexts(CondStmAndContext.class);
		}
		public CondStmAndContext condStmAnd(int i) {
			return getRuleContext(CondStmAndContext.class,i);
		}
		public TerminalNode XorOper() { return getToken(CSoftParser.XorOper, 0); }
		public CondXorStmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condXorStm; }
	}

	public final CondXorStmContext condXorStm() throws RecognitionException {
		CondXorStmContext _localctx = new CondXorStmContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_condXorStm);
		try {
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				condStmAnd();
				setState(170);
				match(XorOper);
				setState(171);
				condStmAnd();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(173);
				condStmAnd();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondStmAndContext extends ParserRuleContext {
		public List<CondStmRelContext> condStmRel() {
			return getRuleContexts(CondStmRelContext.class);
		}
		public CondStmRelContext condStmRel(int i) {
			return getRuleContext(CondStmRelContext.class,i);
		}
		public TerminalNode AndOper() { return getToken(CSoftParser.AndOper, 0); }
		public CondStmAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condStmAnd; }
	}

	public final CondStmAndContext condStmAnd() throws RecognitionException {
		CondStmAndContext _localctx = new CondStmAndContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_condStmAnd);
		try {
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				condStmRel();
				setState(177);
				match(AndOper);
				setState(178);
				condStmRel();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				condStmRel();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondStmRelContext extends ParserRuleContext {
		public List<AddExprContext> addExpr() {
			return getRuleContexts(AddExprContext.class);
		}
		public AddExprContext addExpr(int i) {
			return getRuleContext(AddExprContext.class,i);
		}
		public TerminalNode RelOper() { return getToken(CSoftParser.RelOper, 0); }
		public CondStmRelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condStmRel; }
	}

	public final CondStmRelContext condStmRel() throws RecognitionException {
		CondStmRelContext _localctx = new CondStmRelContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condStmRel);
		try {
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				addExpr();
				setState(184);
				match(RelOper);
				setState(185);
				addExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				addExpr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddExprContext extends ParserRuleContext {
		public List<MultExprContext> multExpr() {
			return getRuleContexts(MultExprContext.class);
		}
		public MultExprContext multExpr(int i) {
			return getRuleContext(MultExprContext.class,i);
		}
		public TerminalNode AddOper() { return getToken(CSoftParser.AddOper, 0); }
		public AddExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addExpr; }
	}

	public final AddExprContext addExpr() throws RecognitionException {
		AddExprContext _localctx = new AddExprContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_addExpr);
		try {
			setState(195);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				multExpr();
				setState(191);
				match(AddOper);
				setState(192);
				multExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(194);
				multExpr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultExprContext extends ParserRuleContext {
		public List<NegFactorContext> negFactor() {
			return getRuleContexts(NegFactorContext.class);
		}
		public NegFactorContext negFactor(int i) {
			return getRuleContext(NegFactorContext.class,i);
		}
		public TerminalNode MultOper() { return getToken(CSoftParser.MultOper, 0); }
		public MultExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multExpr; }
	}

	public final MultExprContext multExpr() throws RecognitionException {
		MultExprContext _localctx = new MultExprContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_multExpr);
		try {
			setState(202);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(197);
				negFactor();
				setState(198);
				match(MultOper);
				setState(199);
				negFactor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(201);
				negFactor();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NegFactorContext extends ParserRuleContext {
		public TerminalNode NegOper() { return getToken(CSoftParser.NegOper, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public NegFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negFactor; }
	}

	public final NegFactorContext negFactor() throws RecognitionException {
		NegFactorContext _localctx = new NegFactorContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_negFactor);
		try {
			setState(207);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NegOper:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				match(NegOper);
				setState(205);
				factor();
				}
				break;
			case BOOL:
			case INT:
			case FLOAT:
			case ID:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				factor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CSoftParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CSoftParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(CSoftParser.STRING, 0); }
		public TerminalNode BOOL() { return getToken(CSoftParser.BOOL, 0); }
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public ArrayAccessContext arrayAccess() {
			return getRuleContext(ArrayAccessContext.class,0);
		}
		public FuncCallContext funcCall() {
			return getRuleContext(FuncCallContext.class,0);
		}
		public StructFieldAccessContext structFieldAccess() {
			return getRuleContext(StructFieldAccessContext.class,0);
		}
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_factor);
		try {
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				match(INT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				match(FLOAT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(211);
				match(STRING);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(212);
				match(BOOL);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(213);
				match(ID);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(214);
				arrayAccess();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(215);
				funcCall();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(216);
				structFieldAccess();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(217);
				methodCall();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(CSoftParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(CSoftParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSoftParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockIfContext blockIf() {
			return getRuleContext(BlockIfContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public IfStmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStm; }
	}

	public final IfStmContext ifStm() throws RecognitionException {
		IfStmContext _localctx = new IfStmContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_ifStm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(IF);
			setState(221);
			match(LPAREN);
			setState(222);
			expr();
			setState(223);
			match(RPAREN);
			setState(224);
			match(LBRACE);
			setState(225);
			blockIf();
			setState(226);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockIfContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockIfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockIf; }
	}

	public final BlockIfContext blockIf() throws RecognitionException {
		BlockIfContext _localctx = new BlockIfContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_blockIf);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 51866730558L) != 0)) {
				{
				{
				setState(228);
				statement();
				}
				}
				setState(233);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeatStmContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(CSoftParser.REPEAT, 0); }
		public TerminalNode LPAREN() { return getToken(CSoftParser.LPAREN, 0); }
		public RepNumContext repNum() {
			return getRuleContext(RepNumContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSoftParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockRepeatContext blockRepeat() {
			return getRuleContext(BlockRepeatContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public RepeatStmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeatStm; }
	}

	public final RepeatStmContext repeatStm() throws RecognitionException {
		RepeatStmContext _localctx = new RepeatStmContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_repeatStm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(REPEAT);
			setState(235);
			match(LPAREN);
			setState(236);
			repNum();
			setState(237);
			match(RPAREN);
			setState(238);
			match(LBRACE);
			setState(239);
			blockRepeat();
			setState(240);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepNumContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public RepNumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repNum; }
	}

	public final RepNumContext repNum() throws RecognitionException {
		RepNumContext _localctx = new RepNumContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_repNum);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			factor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockRepeatContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockRepeatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockRepeat; }
	}

	public final BlockRepeatContext blockRepeat() throws RecognitionException {
		BlockRepeatContext _localctx = new BlockRepeatContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_blockRepeat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 51866730558L) != 0)) {
				{
				{
				setState(244);
				statement();
				}
				}
				setState(249);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileLContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(CSoftParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(CSoftParser.LPAREN, 0); }
		public TerminalNode BOOL() { return getToken(CSoftParser.BOOL, 0); }
		public TerminalNode RPAREN() { return getToken(CSoftParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockWhileContext blockWhile() {
			return getRuleContext(BlockWhileContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public WhileLContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileL; }
	}

	public final WhileLContext whileL() throws RecognitionException {
		WhileLContext _localctx = new WhileLContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_whileL);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(WHILE);
			setState(251);
			match(LPAREN);
			setState(252);
			match(BOOL);
			setState(253);
			match(RPAREN);
			setState(254);
			match(LBRACE);
			setState(255);
			blockWhile();
			setState(256);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockWhileContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockWhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockWhile; }
	}

	public final BlockWhileContext blockWhile() throws RecognitionException {
		BlockWhileContext _localctx = new BlockWhileContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_blockWhile);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(261);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 51866730558L) != 0)) {
				{
				{
				setState(258);
				statement();
				}
				}
				setState(263);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public FunTypeContext funType() {
			return getRuleContext(FunTypeContext.class,0);
		}
		public FunNameContext funName() {
			return getRuleContext(FunNameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(CSoftParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CSoftParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockFunContext blockFun() {
			return getRuleContext(BlockFunContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			funType();
			setState(265);
			funName();
			setState(266);
			match(LPAREN);
			setState(268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17179869246L) != 0)) {
				{
				setState(267);
				parameters();
				}
			}

			setState(270);
			match(RPAREN);
			setState(271);
			match(LBRACE);
			setState(272);
			blockFun();
			setState(273);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockFunContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockFunContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockFun; }
	}

	public final BlockFunContext blockFun() throws RecognitionException {
		BlockFunContext _localctx = new BlockFunContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_blockFun);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 51866730558L) != 0)) {
				{
				{
				setState(275);
				statement();
				}
				}
				setState(280);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassDeclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(CSoftParser.CLASS, 0); }
		public ClassNameContext className() {
			return getRuleContext(ClassNameContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockClassContext blockClass() {
			return getRuleContext(BlockClassContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public ClassDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDecl; }
	}

	public final ClassDeclContext classDecl() throws RecognitionException {
		ClassDeclContext _localctx = new ClassDeclContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_classDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			match(CLASS);
			setState(282);
			className();
			setState(283);
			match(LBRACE);
			setState(284);
			blockClass();
			setState(285);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockClassContext extends ParserRuleContext {
		public List<StructVarDeclContext> structVarDecl() {
			return getRuleContexts(StructVarDeclContext.class);
		}
		public StructVarDeclContext structVarDecl(int i) {
			return getRuleContext(StructVarDeclContext.class,i);
		}
		public List<MethodContext> method() {
			return getRuleContexts(MethodContext.class);
		}
		public MethodContext method(int i) {
			return getRuleContext(MethodContext.class,i);
		}
		public BlockClassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockClass; }
	}

	public final BlockClassContext blockClass() throws RecognitionException {
		BlockClassContext _localctx = new BlockClassContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_blockClass);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(287);
					structVarDecl();
					}
					} 
				}
				setState(292);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) {
				{
				{
				setState(293);
				method();
				}
				}
				setState(298);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodContext extends ParserRuleContext {
		public MethodTypeContext methodType() {
			return getRuleContext(MethodTypeContext.class,0);
		}
		public MethodNameContext methodName() {
			return getRuleContext(MethodNameContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockMethodContext blockMethod() {
			return getRuleContext(BlockMethodContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public MethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method; }
	}

	public final MethodContext method() throws RecognitionException {
		MethodContext _localctx = new MethodContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_method);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			methodType();
			setState(300);
			methodName();
			setState(301);
			match(LBRACE);
			setState(302);
			blockMethod();
			setState(303);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockMethodContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockMethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockMethod; }
	}

	public final BlockMethodContext blockMethod() throws RecognitionException {
		BlockMethodContext _localctx = new BlockMethodContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_blockMethod);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 51866730558L) != 0)) {
				{
				{
				setState(305);
				statement();
				}
				}
				setState(310);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodTypeContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public MethodTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodType; }
	}

	public final MethodTypeContext methodType() throws RecognitionException {
		MethodTypeContext _localctx = new MethodTypeContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_methodType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public MethodNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodName; }
	}

	public final MethodNameContext methodName() throws RecognitionException {
		MethodNameContext _localctx = new MethodNameContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_methodName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public ClassNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_className; }
	}

	public final ClassNameContext className() throws RecognitionException {
		ClassNameContext _localctx = new ClassNameContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_className);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSoftParser.DOT, 0); }
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public MethodCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodCall; }
	}

	public final MethodCallContext methodCall() throws RecognitionException {
		MethodCallContext _localctx = new MethodCallContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_methodCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			match(ID);
			setState(318);
			match(DOT);
			setState(319);
			ident();
			setState(320);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassAssignContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public TerminalNode CLASS() { return getToken(CSoftParser.CLASS, 0); }
		public ClassNameContext className() {
			return getRuleContext(ClassNameContext.class,0);
		}
		public ClassAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classAssign; }
	}

	public final ClassAssignContext classAssign() throws RecognitionException {
		ClassAssignContext _localctx = new ClassAssignContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_classAssign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			ident();
			setState(323);
			match(ASSIGN);
			setState(324);
			match(CLASS);
			setState(325);
			className();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CSoftParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSoftParser.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			parameter();
			setState(332);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(328);
				match(COMMA);
				setState(329);
				parameter();
				}
				}
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			ident();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructDeclContext extends ParserRuleContext {
		public TerminalNode STRUCT() { return getToken(CSoftParser.STRUCT, 0); }
		public StructNameContext structName() {
			return getRuleContext(StructNameContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CSoftParser.LBRACE, 0); }
		public BlockStructContext blockStruct() {
			return getRuleContext(BlockStructContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSoftParser.RBRACE, 0); }
		public StructDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structDecl; }
	}

	public final StructDeclContext structDecl() throws RecognitionException {
		StructDeclContext _localctx = new StructDeclContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_structDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(337);
			match(STRUCT);
			setState(338);
			structName();
			setState(339);
			match(LBRACE);
			setState(340);
			blockStruct();
			setState(341);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockStructContext extends ParserRuleContext {
		public List<StructVarDeclContext> structVarDecl() {
			return getRuleContexts(StructVarDeclContext.class);
		}
		public StructVarDeclContext structVarDecl(int i) {
			return getRuleContext(StructVarDeclContext.class,i);
		}
		public BlockStructContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockStruct; }
	}

	public final BlockStructContext blockStruct() throws RecognitionException {
		BlockStructContext _localctx = new BlockStructContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_blockStruct);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17179869246L) != 0)) {
				{
				{
				setState(343);
				structVarDecl();
				}
				}
				setState(348);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructVarDeclContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public StructVarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structVarDecl; }
	}

	public final StructVarDeclContext structVarDecl() throws RecognitionException {
		StructVarDeclContext _localctx = new StructVarDeclContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_structVarDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			ident();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructAssignContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public TerminalNode STRUCT() { return getToken(CSoftParser.STRUCT, 0); }
		public StructNameContext structName() {
			return getRuleContext(StructNameContext.class,0);
		}
		public StructAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structAssign; }
	}

	public final StructAssignContext structAssign() throws RecognitionException {
		StructAssignContext _localctx = new StructAssignContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_structAssign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			ident();
			setState(352);
			match(ASSIGN);
			setState(353);
			match(STRUCT);
			setState(354);
			structName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructFieldAssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSoftParser.DOT, 0); }
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(CSoftParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StructFieldAssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structFieldAssign; }
	}

	public final StructFieldAssignContext structFieldAssign() throws RecognitionException {
		StructFieldAssignContext _localctx = new StructFieldAssignContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_structFieldAssign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(356);
			match(ID);
			setState(357);
			match(DOT);
			setState(358);
			ident();
			setState(359);
			match(ASSIGN);
			setState(360);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructFieldAccessContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CSoftParser.DOT, 0); }
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public StructFieldAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structFieldAccess; }
	}

	public final StructFieldAccessContext structFieldAccess() throws RecognitionException {
		StructFieldAccessContext _localctx = new StructFieldAccessContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_structFieldAccess);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			match(ID);
			setState(363);
			match(DOT);
			setState(364);
			ident();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayAccessContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public TerminalNode LBRACKET() { return getToken(CSoftParser.LBRACKET, 0); }
		public TerminalNode INT() { return getToken(CSoftParser.INT, 0); }
		public TerminalNode RBRACKET() { return getToken(CSoftParser.RBRACKET, 0); }
		public ArrayAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayAccess; }
	}

	public final ArrayAccessContext arrayAccess() throws RecognitionException {
		ArrayAccessContext _localctx = new ArrayAccessContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_arrayAccess);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
			match(ID);
			setState(367);
			match(LBRACKET);
			setState(368);
			match(INT);
			setState(369);
			match(RBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public FuncCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcCall; }
	}

	public final FuncCallContext funcCall() throws RecognitionException {
		FuncCallContext _localctx = new FuncCallContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_funcCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(371);
			match(ID);
			setState(372);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunTypeContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public FunTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funType; }
	}

	public final FunTypeContext funType() throws RecognitionException {
		FunTypeContext _localctx = new FunTypeContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_funType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public FunNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funName; }
	}

	public final FunNameContext funName() throws RecognitionException {
		FunNameContext _localctx = new FunNameContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_funName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CSoftParser.ID, 0); }
		public StructNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structName; }
	}

	public final StructNameContext structName() throws RecognitionException {
		StructNameContext _localctx = new StructNameContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_structName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u017d\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0001\u0000\u0001\u0000\u0001\u0001\u0005\u0001"+
		"b\b\u0001\n\u0001\f\u0001e\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002\u0083\b\u0002\u0001\u0003\u0003\u0003\u0086\b"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u009c\b\u0007\n\u0007\f\u0007"+
		"\u009f\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0003\b\u00a8\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\t\u00af\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00b6\b\n"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u00bd\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00c4\b"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00cb\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u00d0\b\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u00db\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0005\u0011\u00e6\b\u0011\n\u0011\f\u0011\u00e9\t\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0005\u0014\u00f6\b\u0014\n"+
		"\u0014\f\u0014\u00f9\t\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0005"+
		"\u0016\u0104\b\u0016\n\u0016\f\u0016\u0107\t\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u010d\b\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0005\u0018\u0115\b\u0018"+
		"\n\u0018\f\u0018\u0118\t\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0005\u001a\u0121\b\u001a\n"+
		"\u001a\f\u001a\u0124\t\u001a\u0001\u001a\u0005\u001a\u0127\b\u001a\n\u001a"+
		"\f\u001a\u012a\t\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0005\u001c\u0133\b\u001c\n\u001c"+
		"\f\u001c\u0136\t\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e"+
		"\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001 \u0001 \u0001!\u0001"+
		"!\u0001!\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0005\"\u014b\b\"\n\"\f"+
		"\"\u014e\t\"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"%\u0005%\u0159\b%\n%\f%\u015c\t%\u0001&\u0001&\u0001\'\u0001\'\u0001\'"+
		"\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0001(\u0001(\u0001(\u0001)\u0001"+
		")\u0001)\u0001)\u0001*\u0001*\u0001*\u0001*\u0001*\u0001+\u0001+\u0001"+
		"+\u0001,\u0001,\u0001-\u0001-\u0001.\u0001.\u0001.\u0000\u0000/\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\\u0000\u0001\u0001\u0000\u0001"+
		"\u0005\u0177\u0000^\u0001\u0000\u0000\u0000\u0002c\u0001\u0000\u0000\u0000"+
		"\u0004\u0082\u0001\u0000\u0000\u0000\u0006\u0085\u0001\u0000\u0000\u0000"+
		"\b\u0089\u0001\u0000\u0000\u0000\n\u008d\u0001\u0000\u0000\u0000\f\u0092"+
		"\u0001\u0000\u0000\u0000\u000e\u0097\u0001\u0000\u0000\u0000\u0010\u00a7"+
		"\u0001\u0000\u0000\u0000\u0012\u00ae\u0001\u0000\u0000\u0000\u0014\u00b5"+
		"\u0001\u0000\u0000\u0000\u0016\u00bc\u0001\u0000\u0000\u0000\u0018\u00c3"+
		"\u0001\u0000\u0000\u0000\u001a\u00ca\u0001\u0000\u0000\u0000\u001c\u00cf"+
		"\u0001\u0000\u0000\u0000\u001e\u00da\u0001\u0000\u0000\u0000 \u00dc\u0001"+
		"\u0000\u0000\u0000\"\u00e7\u0001\u0000\u0000\u0000$\u00ea\u0001\u0000"+
		"\u0000\u0000&\u00f2\u0001\u0000\u0000\u0000(\u00f7\u0001\u0000\u0000\u0000"+
		"*\u00fa\u0001\u0000\u0000\u0000,\u0105\u0001\u0000\u0000\u0000.\u0108"+
		"\u0001\u0000\u0000\u00000\u0116\u0001\u0000\u0000\u00002\u0119\u0001\u0000"+
		"\u0000\u00004\u0122\u0001\u0000\u0000\u00006\u012b\u0001\u0000\u0000\u0000"+
		"8\u0134\u0001\u0000\u0000\u0000:\u0137\u0001\u0000\u0000\u0000<\u0139"+
		"\u0001\u0000\u0000\u0000>\u013b\u0001\u0000\u0000\u0000@\u013d\u0001\u0000"+
		"\u0000\u0000B\u0142\u0001\u0000\u0000\u0000D\u0147\u0001\u0000\u0000\u0000"+
		"F\u014f\u0001\u0000\u0000\u0000H\u0151\u0001\u0000\u0000\u0000J\u015a"+
		"\u0001\u0000\u0000\u0000L\u015d\u0001\u0000\u0000\u0000N\u015f\u0001\u0000"+
		"\u0000\u0000P\u0164\u0001\u0000\u0000\u0000R\u016a\u0001\u0000\u0000\u0000"+
		"T\u016e\u0001\u0000\u0000\u0000V\u0173\u0001\u0000\u0000\u0000X\u0176"+
		"\u0001\u0000\u0000\u0000Z\u0178\u0001\u0000\u0000\u0000\\\u017a\u0001"+
		"\u0000\u0000\u0000^_\u0007\u0000\u0000\u0000_\u0001\u0001\u0000\u0000"+
		"\u0000`b\u0003\u0004\u0002\u0000a`\u0001\u0000\u0000\u0000be\u0001\u0000"+
		"\u0000\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000df\u0001"+
		"\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000fg\u0005\u0000\u0000\u0001"+
		"g\u0003\u0001\u0000\u0000\u0000h\u0083\u0003\n\u0005\u0000i\u0083\u0003"+
		"\f\u0006\u0000j\u0083\u0003\u0010\b\u0000kl\u0003\u0006\u0003\u0000lm"+
		"\u0005\u0017\u0000\u0000mn\u0003\u0010\b\u0000n\u0083\u0001\u0000\u0000"+
		"\u0000op\u0005\"\u0000\u0000pq\u0005\r\u0000\u0000qr\u0005\u0018\u0000"+
		"\u0000rs\u0005\u000e\u0000\u0000st\u0005\u0017\u0000\u0000t\u0083\u0003"+
		"\u0010\b\u0000uv\u0003\u0006\u0003\u0000vw\u0005\u0017\u0000\u0000wx\u0003"+
		"\u000e\u0007\u0000x\u0083\u0001\u0000\u0000\u0000y\u0083\u0003$\u0012"+
		"\u0000z\u0083\u0003 \u0010\u0000{\u0083\u0003*\u0015\u0000|\u0083\u0003"+
		".\u0017\u0000}\u0083\u0003H$\u0000~\u0083\u0003P(\u0000\u007f\u0083\u0003"+
		"N\'\u0000\u0080\u0083\u00032\u0019\u0000\u0081\u0083\u0003B!\u0000\u0082"+
		"h\u0001\u0000\u0000\u0000\u0082i\u0001\u0000\u0000\u0000\u0082j\u0001"+
		"\u0000\u0000\u0000\u0082k\u0001\u0000\u0000\u0000\u0082o\u0001\u0000\u0000"+
		"\u0000\u0082u\u0001\u0000\u0000\u0000\u0082y\u0001\u0000\u0000\u0000\u0082"+
		"z\u0001\u0000\u0000\u0000\u0082{\u0001\u0000\u0000\u0000\u0082|\u0001"+
		"\u0000\u0000\u0000\u0082}\u0001\u0000\u0000\u0000\u0082~\u0001\u0000\u0000"+
		"\u0000\u0082\u007f\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000\u0000"+
		"\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0005\u0001\u0000\u0000"+
		"\u0000\u0084\u0086\u0003\u0000\u0000\u0000\u0085\u0084\u0001\u0000\u0000"+
		"\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000"+
		"\u0000\u0087\u0088\u0005\"\u0000\u0000\u0088\u0007\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0003\u0006\u0003\u0000\u008a\u008b\u0005\u0017\u0000\u0000"+
		"\u008b\u008c\u0003\u0010\b\u0000\u008c\t\u0001\u0000\u0000\u0000\u008d"+
		"\u008e\u0005\u000f\u0000\u0000\u008e\u008f\u0005\t\u0000\u0000\u008f\u0090"+
		"\u0005\"\u0000\u0000\u0090\u0091\u0005\n\u0000\u0000\u0091\u000b\u0001"+
		"\u0000\u0000\u0000\u0092\u0093\u0005\u0010\u0000\u0000\u0093\u0094\u0005"+
		"\t\u0000\u0000\u0094\u0095\u0005\"\u0000\u0000\u0095\u0096\u0005\n\u0000"+
		"\u0000\u0096\r\u0001\u0000\u0000\u0000\u0097\u0098\u0005\r\u0000\u0000"+
		"\u0098\u009d\u0003\u001e\u000f\u0000\u0099\u009a\u0005\u0007\u0000\u0000"+
		"\u009a\u009c\u0003\u001e\u000f\u0000\u009b\u0099\u0001\u0000\u0000\u0000"+
		"\u009c\u009f\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000"+
		"\u009d\u009e\u0001\u0000\u0000\u0000\u009e\u00a0\u0001\u0000\u0000\u0000"+
		"\u009f\u009d\u0001\u0000\u0000\u0000\u00a0\u00a1\u0005\u000e\u0000\u0000"+
		"\u00a1\u000f\u0001\u0000\u0000\u0000\u00a2\u00a3\u0003\u0012\t\u0000\u00a3"+
		"\u00a4\u0005\u001f\u0000\u0000\u00a4\u00a5\u0003\u0012\t\u0000\u00a5\u00a8"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a8\u0003\u0012\t\u0000\u00a7\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a8\u0011\u0001"+
		"\u0000\u0000\u0000\u00a9\u00aa\u0003\u0014\n\u0000\u00aa\u00ab\u0005 "+
		"\u0000\u0000\u00ab\u00ac\u0003\u0014\n\u0000\u00ac\u00af\u0001\u0000\u0000"+
		"\u0000\u00ad\u00af\u0003\u0014\n\u0000\u00ae\u00a9\u0001\u0000\u0000\u0000"+
		"\u00ae\u00ad\u0001\u0000\u0000\u0000\u00af\u0013\u0001\u0000\u0000\u0000"+
		"\u00b0\u00b1\u0003\u0016\u000b\u0000\u00b1\u00b2\u0005\u001e\u0000\u0000"+
		"\u00b2\u00b3\u0003\u0016\u000b\u0000\u00b3\u00b6\u0001\u0000\u0000\u0000"+
		"\u00b4\u00b6\u0003\u0016\u000b\u0000\u00b5\u00b0\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b4\u0001\u0000\u0000\u0000\u00b6\u0015\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b8\u0003\u0018\f\u0000\u00b8\u00b9\u0005\u001d\u0000\u0000\u00b9"+
		"\u00ba\u0003\u0018\f\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb\u00bd"+
		"\u0003\u0018\f\u0000\u00bc\u00b7\u0001\u0000\u0000\u0000\u00bc\u00bb\u0001"+
		"\u0000\u0000\u0000\u00bd\u0017\u0001\u0000\u0000\u0000\u00be\u00bf\u0003"+
		"\u001a\r\u0000\u00bf\u00c0\u0005\u001a\u0000\u0000\u00c0\u00c1\u0003\u001a"+
		"\r\u0000\u00c1\u00c4\u0001\u0000\u0000\u0000\u00c2\u00c4\u0003\u001a\r"+
		"\u0000\u00c3\u00be\u0001\u0000\u0000\u0000\u00c3\u00c2\u0001\u0000\u0000"+
		"\u0000\u00c4\u0019\u0001\u0000\u0000\u0000\u00c5\u00c6\u0003\u001c\u000e"+
		"\u0000\u00c6\u00c7\u0005\u001b\u0000\u0000\u00c7\u00c8\u0003\u001c\u000e"+
		"\u0000\u00c8\u00cb\u0001\u0000\u0000\u0000\u00c9\u00cb\u0003\u001c\u000e"+
		"\u0000\u00ca\u00c5\u0001\u0000\u0000\u0000\u00ca\u00c9\u0001\u0000\u0000"+
		"\u0000\u00cb\u001b\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005\u001c\u0000"+
		"\u0000\u00cd\u00d0\u0003\u001e\u000f\u0000\u00ce\u00d0\u0003\u001e\u000f"+
		"\u0000\u00cf\u00cc\u0001\u0000\u0000\u0000\u00cf\u00ce\u0001\u0000\u0000"+
		"\u0000\u00d0\u001d\u0001\u0000\u0000\u0000\u00d1\u00db\u0005\u0018\u0000"+
		"\u0000\u00d2\u00db\u0005\u0019\u0000\u0000\u00d3\u00db\u0005#\u0000\u0000"+
		"\u00d4\u00db\u0005\u0015\u0000\u0000\u00d5\u00db\u0005\"\u0000\u0000\u00d6"+
		"\u00db\u0003T*\u0000\u00d7\u00db\u0003V+\u0000\u00d8\u00db\u0003R)\u0000"+
		"\u00d9\u00db\u0003@ \u0000\u00da\u00d1\u0001\u0000\u0000\u0000\u00da\u00d2"+
		"\u0001\u0000\u0000\u0000\u00da\u00d3\u0001\u0000\u0000\u0000\u00da\u00d4"+
		"\u0001\u0000\u0000\u0000\u00da\u00d5\u0001\u0000\u0000\u0000\u00da\u00d6"+
		"\u0001\u0000\u0000\u0000\u00da\u00d7\u0001\u0000\u0000\u0000\u00da\u00d8"+
		"\u0001\u0000\u0000\u0000\u00da\u00d9\u0001\u0000\u0000\u0000\u00db\u001f"+
		"\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005\u0011\u0000\u0000\u00dd\u00de"+
		"\u0005\t\u0000\u0000\u00de\u00df\u0003\u0010\b\u0000\u00df\u00e0\u0005"+
		"\n\u0000\u0000\u00e0\u00e1\u0005\u000b\u0000\u0000\u00e1\u00e2\u0003\""+
		"\u0011\u0000\u00e2\u00e3\u0005\f\u0000\u0000\u00e3!\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e6\u0003\u0004\u0002\u0000\u00e5\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8#\u0001\u0000\u0000\u0000"+
		"\u00e9\u00e7\u0001\u0000\u0000\u0000\u00ea\u00eb\u0005\u0016\u0000\u0000"+
		"\u00eb\u00ec\u0005\t\u0000\u0000\u00ec\u00ed\u0003&\u0013\u0000\u00ed"+
		"\u00ee\u0005\n\u0000\u0000\u00ee\u00ef\u0005\u000b\u0000\u0000\u00ef\u00f0"+
		"\u0003(\u0014\u0000\u00f0\u00f1\u0005\f\u0000\u0000\u00f1%\u0001\u0000"+
		"\u0000\u0000\u00f2\u00f3\u0003\u001e\u000f\u0000\u00f3\'\u0001\u0000\u0000"+
		"\u0000\u00f4\u00f6\u0003\u0004\u0002\u0000\u00f5\u00f4\u0001\u0000\u0000"+
		"\u0000\u00f6\u00f9\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8)\u0001\u0000\u0000\u0000"+
		"\u00f9\u00f7\u0001\u0000\u0000\u0000\u00fa\u00fb\u0005\u0012\u0000\u0000"+
		"\u00fb\u00fc\u0005\t\u0000\u0000\u00fc\u00fd\u0005\u0015\u0000\u0000\u00fd"+
		"\u00fe\u0005\n\u0000\u0000\u00fe\u00ff\u0005\u000b\u0000\u0000\u00ff\u0100"+
		"\u0003,\u0016\u0000\u0100\u0101\u0005\f\u0000\u0000\u0101+\u0001\u0000"+
		"\u0000\u0000\u0102\u0104\u0003\u0004\u0002\u0000\u0103\u0102\u0001\u0000"+
		"\u0000\u0000\u0104\u0107\u0001\u0000\u0000\u0000\u0105\u0103\u0001\u0000"+
		"\u0000\u0000\u0105\u0106\u0001\u0000\u0000\u0000\u0106-\u0001\u0000\u0000"+
		"\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0108\u0109\u0003X,\u0000\u0109"+
		"\u010a\u0003Z-\u0000\u010a\u010c\u0005\t\u0000\u0000\u010b\u010d\u0003"+
		"D\"\u0000\u010c\u010b\u0001\u0000\u0000\u0000\u010c\u010d\u0001\u0000"+
		"\u0000\u0000\u010d\u010e\u0001\u0000\u0000\u0000\u010e\u010f\u0005\n\u0000"+
		"\u0000\u010f\u0110\u0005\u000b\u0000\u0000\u0110\u0111\u00030\u0018\u0000"+
		"\u0111\u0112\u0005\f\u0000\u0000\u0112/\u0001\u0000\u0000\u0000\u0113"+
		"\u0115\u0003\u0004\u0002\u0000\u0114\u0113\u0001\u0000\u0000\u0000\u0115"+
		"\u0118\u0001\u0000\u0000\u0000\u0116\u0114\u0001\u0000\u0000\u0000\u0116"+
		"\u0117\u0001\u0000\u0000\u0000\u01171\u0001\u0000\u0000\u0000\u0118\u0116"+
		"\u0001\u0000\u0000\u0000\u0119\u011a\u0005\u0014\u0000\u0000\u011a\u011b"+
		"\u0003>\u001f\u0000\u011b\u011c\u0005\u000b\u0000\u0000\u011c\u011d\u0003"+
		"4\u001a\u0000\u011d\u011e\u0005\f\u0000\u0000\u011e3\u0001\u0000\u0000"+
		"\u0000\u011f\u0121\u0003L&\u0000\u0120\u011f\u0001\u0000\u0000\u0000\u0121"+
		"\u0124\u0001\u0000\u0000\u0000\u0122\u0120\u0001\u0000\u0000\u0000\u0122"+
		"\u0123\u0001\u0000\u0000\u0000\u0123\u0128\u0001\u0000\u0000\u0000\u0124"+
		"\u0122\u0001\u0000\u0000\u0000\u0125\u0127\u00036\u001b\u0000\u0126\u0125"+
		"\u0001\u0000\u0000\u0000\u0127\u012a\u0001\u0000\u0000\u0000\u0128\u0126"+
		"\u0001\u0000\u0000\u0000\u0128\u0129\u0001\u0000\u0000\u0000\u01295\u0001"+
		"\u0000\u0000\u0000\u012a\u0128\u0001\u0000\u0000\u0000\u012b\u012c\u0003"+
		":\u001d\u0000\u012c\u012d\u0003<\u001e\u0000\u012d\u012e\u0005\u000b\u0000"+
		"\u0000\u012e\u012f\u00038\u001c\u0000\u012f\u0130\u0005\f\u0000\u0000"+
		"\u01307\u0001\u0000\u0000\u0000\u0131\u0133\u0003\u0004\u0002\u0000\u0132"+
		"\u0131\u0001\u0000\u0000\u0000\u0133\u0136\u0001\u0000\u0000\u0000\u0134"+
		"\u0132\u0001\u0000\u0000\u0000\u0134\u0135\u0001\u0000\u0000\u0000\u0135"+
		"9\u0001\u0000\u0000\u0000\u0136\u0134\u0001\u0000\u0000\u0000\u0137\u0138"+
		"\u0003\u0000\u0000\u0000\u0138;\u0001\u0000\u0000\u0000\u0139\u013a\u0005"+
		"\"\u0000\u0000\u013a=\u0001\u0000\u0000\u0000\u013b\u013c\u0005\"\u0000"+
		"\u0000\u013c?\u0001\u0000\u0000\u0000\u013d\u013e\u0005\"\u0000\u0000"+
		"\u013e\u013f\u0005\b\u0000\u0000\u013f\u0140\u0003\u0006\u0003\u0000\u0140"+
		"\u0141\u0005\u0006\u0000\u0000\u0141A\u0001\u0000\u0000\u0000\u0142\u0143"+
		"\u0003\u0006\u0003\u0000\u0143\u0144\u0005\u0017\u0000\u0000\u0144\u0145"+
		"\u0005\u0014\u0000\u0000\u0145\u0146\u0003>\u001f\u0000\u0146C\u0001\u0000"+
		"\u0000\u0000\u0147\u014c\u0003F#\u0000\u0148\u0149\u0005\u0007\u0000\u0000"+
		"\u0149\u014b\u0003F#\u0000\u014a\u0148\u0001\u0000\u0000\u0000\u014b\u014e"+
		"\u0001\u0000\u0000\u0000\u014c\u014a\u0001\u0000\u0000\u0000\u014c\u014d"+
		"\u0001\u0000\u0000\u0000\u014dE\u0001\u0000\u0000\u0000\u014e\u014c\u0001"+
		"\u0000\u0000\u0000\u014f\u0150\u0003\u0006\u0003\u0000\u0150G\u0001\u0000"+
		"\u0000\u0000\u0151\u0152\u0005\u0013\u0000\u0000\u0152\u0153\u0003\\."+
		"\u0000\u0153\u0154\u0005\u000b\u0000\u0000\u0154\u0155\u0003J%\u0000\u0155"+
		"\u0156\u0005\f\u0000\u0000\u0156I\u0001\u0000\u0000\u0000\u0157\u0159"+
		"\u0003L&\u0000\u0158\u0157\u0001\u0000\u0000\u0000\u0159\u015c\u0001\u0000"+
		"\u0000\u0000\u015a\u0158\u0001\u0000\u0000\u0000\u015a\u015b\u0001\u0000"+
		"\u0000\u0000\u015bK\u0001\u0000\u0000\u0000\u015c\u015a\u0001\u0000\u0000"+
		"\u0000\u015d\u015e\u0003\u0006\u0003\u0000\u015eM\u0001\u0000\u0000\u0000"+
		"\u015f\u0160\u0003\u0006\u0003\u0000\u0160\u0161\u0005\u0017\u0000\u0000"+
		"\u0161\u0162\u0005\u0013\u0000\u0000\u0162\u0163\u0003\\.\u0000\u0163"+
		"O\u0001\u0000\u0000\u0000\u0164\u0165\u0005\"\u0000\u0000\u0165\u0166"+
		"\u0005\b\u0000\u0000\u0166\u0167\u0003\u0006\u0003\u0000\u0167\u0168\u0005"+
		"\u0017\u0000\u0000\u0168\u0169\u0003\u0010\b\u0000\u0169Q\u0001\u0000"+
		"\u0000\u0000\u016a\u016b\u0005\"\u0000\u0000\u016b\u016c\u0005\b\u0000"+
		"\u0000\u016c\u016d\u0003\u0006\u0003\u0000\u016dS\u0001\u0000\u0000\u0000"+
		"\u016e\u016f\u0005\"\u0000\u0000\u016f\u0170\u0005\r\u0000\u0000\u0170"+
		"\u0171\u0005\u0018\u0000\u0000\u0171\u0172\u0005\u000e\u0000\u0000\u0172"+
		"U\u0001\u0000\u0000\u0000\u0173\u0174\u0005\"\u0000\u0000\u0174\u0175"+
		"\u0005\u0006\u0000\u0000\u0175W\u0001\u0000\u0000\u0000\u0176\u0177\u0003"+
		"\u0000\u0000\u0000\u0177Y\u0001\u0000\u0000\u0000\u0178\u0179\u0005\""+
		"\u0000\u0000\u0179[\u0001\u0000\u0000\u0000\u017a\u017b\u0005\"\u0000"+
		"\u0000\u017b]\u0001\u0000\u0000\u0000\u0016c\u0082\u0085\u009d\u00a7\u00ae"+
		"\u00b5\u00bc\u00c3\u00ca\u00cf\u00da\u00e7\u00f7\u0105\u010c\u0116\u0122"+
		"\u0128\u0134\u014c\u015a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}