// Generated from //wsl.localhost/Ubuntu-22.04/home/jihyo/Compiler/antlr_generated/CSoft.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CSoftParser}.
 */
public interface CSoftListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CSoftParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(CSoftParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(CSoftParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CSoftParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CSoftParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code print}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrint(CSoftParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code print}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrint(CSoftParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code read}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterRead(CSoftParser.ReadContext ctx);
	/**
	 * Exit a parse tree produced by the {@code read}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitRead(CSoftParser.ReadContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exprression}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExprression(CSoftParser.ExprressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exprression}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExprression(CSoftParser.ExprressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assign}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssign(CSoftParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assign}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssign(CSoftParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code elementAssign}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterElementAssign(CSoftParser.ElementAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code elementAssign}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitElementAssign(CSoftParser.ElementAssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrAssign}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterArrAssign(CSoftParser.ArrAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrAssign}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitArrAssign(CSoftParser.ArrAssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code repeatStatement}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterRepeatStatement(CSoftParser.RepeatStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code repeatStatement}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitRepeatStatement(CSoftParser.RepeatStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifStatement}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(CSoftParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifStatement}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(CSoftParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code funcDecl}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterFuncDecl(CSoftParser.FuncDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funcDecl}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitFuncDecl(CSoftParser.FuncDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code structDeclaration}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclaration(CSoftParser.StructDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code structDeclaration}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclaration(CSoftParser.StructDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code structFieldAssignment}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStructFieldAssignment(CSoftParser.StructFieldAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code structFieldAssignment}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStructFieldAssignment(CSoftParser.StructFieldAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code structAssignmet}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStructAssignmet(CSoftParser.StructAssignmetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code structAssignmet}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStructAssignmet(CSoftParser.StructAssignmetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code classDeclaration}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterClassDeclaration(CSoftParser.ClassDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code classDeclaration}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitClassDeclaration(CSoftParser.ClassDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code classAssignment}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterClassAssignment(CSoftParser.ClassAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code classAssignment}
	 * labeled alternative in {@link CSoftParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitClassAssignment(CSoftParser.ClassAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#ident}.
	 * @param ctx the parse tree
	 */
	void enterIdent(CSoftParser.IdentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#ident}.
	 * @param ctx the parse tree
	 */
	void exitIdent(CSoftParser.IdentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#arrayElementAssign}.
	 * @param ctx the parse tree
	 */
	void enterArrayElementAssign(CSoftParser.ArrayElementAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#arrayElementAssign}.
	 * @param ctx the parse tree
	 */
	void exitArrayElementAssign(CSoftParser.ArrayElementAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(CSoftParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(CSoftParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#print_statement}.
	 * @param ctx the parse tree
	 */
	void enterPrint_statement(CSoftParser.Print_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#print_statement}.
	 * @param ctx the parse tree
	 */
	void exitPrint_statement(CSoftParser.Print_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#read_statement}.
	 * @param ctx the parse tree
	 */
	void enterRead_statement(CSoftParser.Read_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#read_statement}.
	 * @param ctx the parse tree
	 */
	void exitRead_statement(CSoftParser.Read_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#arrayAssign}.
	 * @param ctx the parse tree
	 */
	void enterArrayAssign(CSoftParser.ArrayAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#arrayAssign}.
	 * @param ctx the parse tree
	 */
	void exitArrayAssign(CSoftParser.ArrayAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(CSoftParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(CSoftParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#condXorStm}.
	 * @param ctx the parse tree
	 */
	void enterCondXorStm(CSoftParser.CondXorStmContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#condXorStm}.
	 * @param ctx the parse tree
	 */
	void exitCondXorStm(CSoftParser.CondXorStmContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#condStmAnd}.
	 * @param ctx the parse tree
	 */
	void enterCondStmAnd(CSoftParser.CondStmAndContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#condStmAnd}.
	 * @param ctx the parse tree
	 */
	void exitCondStmAnd(CSoftParser.CondStmAndContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#condStmRel}.
	 * @param ctx the parse tree
	 */
	void enterCondStmRel(CSoftParser.CondStmRelContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#condStmRel}.
	 * @param ctx the parse tree
	 */
	void exitCondStmRel(CSoftParser.CondStmRelContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void enterAddExpr(CSoftParser.AddExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void exitAddExpr(CSoftParser.AddExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#multExpr}.
	 * @param ctx the parse tree
	 */
	void enterMultExpr(CSoftParser.MultExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#multExpr}.
	 * @param ctx the parse tree
	 */
	void exitMultExpr(CSoftParser.MultExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#negFactor}.
	 * @param ctx the parse tree
	 */
	void enterNegFactor(CSoftParser.NegFactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#negFactor}.
	 * @param ctx the parse tree
	 */
	void exitNegFactor(CSoftParser.NegFactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CSoftParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CSoftParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#ifStm}.
	 * @param ctx the parse tree
	 */
	void enterIfStm(CSoftParser.IfStmContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#ifStm}.
	 * @param ctx the parse tree
	 */
	void exitIfStm(CSoftParser.IfStmContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#blockIf}.
	 * @param ctx the parse tree
	 */
	void enterBlockIf(CSoftParser.BlockIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#blockIf}.
	 * @param ctx the parse tree
	 */
	void exitBlockIf(CSoftParser.BlockIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#repeatStm}.
	 * @param ctx the parse tree
	 */
	void enterRepeatStm(CSoftParser.RepeatStmContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#repeatStm}.
	 * @param ctx the parse tree
	 */
	void exitRepeatStm(CSoftParser.RepeatStmContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#repNum}.
	 * @param ctx the parse tree
	 */
	void enterRepNum(CSoftParser.RepNumContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#repNum}.
	 * @param ctx the parse tree
	 */
	void exitRepNum(CSoftParser.RepNumContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#blockRepeat}.
	 * @param ctx the parse tree
	 */
	void enterBlockRepeat(CSoftParser.BlockRepeatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#blockRepeat}.
	 * @param ctx the parse tree
	 */
	void exitBlockRepeat(CSoftParser.BlockRepeatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(CSoftParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(CSoftParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#blockFun}.
	 * @param ctx the parse tree
	 */
	void enterBlockFun(CSoftParser.BlockFunContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#blockFun}.
	 * @param ctx the parse tree
	 */
	void exitBlockFun(CSoftParser.BlockFunContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(CSoftParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(CSoftParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#blockClass}.
	 * @param ctx the parse tree
	 */
	void enterBlockClass(CSoftParser.BlockClassContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#blockClass}.
	 * @param ctx the parse tree
	 */
	void exitBlockClass(CSoftParser.BlockClassContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#method}.
	 * @param ctx the parse tree
	 */
	void enterMethod(CSoftParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#method}.
	 * @param ctx the parse tree
	 */
	void exitMethod(CSoftParser.MethodContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#blockMethod}.
	 * @param ctx the parse tree
	 */
	void enterBlockMethod(CSoftParser.BlockMethodContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#blockMethod}.
	 * @param ctx the parse tree
	 */
	void exitBlockMethod(CSoftParser.BlockMethodContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#methodType}.
	 * @param ctx the parse tree
	 */
	void enterMethodType(CSoftParser.MethodTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#methodType}.
	 * @param ctx the parse tree
	 */
	void exitMethodType(CSoftParser.MethodTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#methodName}.
	 * @param ctx the parse tree
	 */
	void enterMethodName(CSoftParser.MethodNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#methodName}.
	 * @param ctx the parse tree
	 */
	void exitMethodName(CSoftParser.MethodNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#className}.
	 * @param ctx the parse tree
	 */
	void enterClassName(CSoftParser.ClassNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#className}.
	 * @param ctx the parse tree
	 */
	void exitClassName(CSoftParser.ClassNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void enterMethodCall(CSoftParser.MethodCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void exitMethodCall(CSoftParser.MethodCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#classAssign}.
	 * @param ctx the parse tree
	 */
	void enterClassAssign(CSoftParser.ClassAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#classAssign}.
	 * @param ctx the parse tree
	 */
	void exitClassAssign(CSoftParser.ClassAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(CSoftParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(CSoftParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(CSoftParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(CSoftParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#structDecl}.
	 * @param ctx the parse tree
	 */
	void enterStructDecl(CSoftParser.StructDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#structDecl}.
	 * @param ctx the parse tree
	 */
	void exitStructDecl(CSoftParser.StructDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#blockStruct}.
	 * @param ctx the parse tree
	 */
	void enterBlockStruct(CSoftParser.BlockStructContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#blockStruct}.
	 * @param ctx the parse tree
	 */
	void exitBlockStruct(CSoftParser.BlockStructContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#structVarDecl}.
	 * @param ctx the parse tree
	 */
	void enterStructVarDecl(CSoftParser.StructVarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#structVarDecl}.
	 * @param ctx the parse tree
	 */
	void exitStructVarDecl(CSoftParser.StructVarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#structAssign}.
	 * @param ctx the parse tree
	 */
	void enterStructAssign(CSoftParser.StructAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#structAssign}.
	 * @param ctx the parse tree
	 */
	void exitStructAssign(CSoftParser.StructAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#structFieldAssign}.
	 * @param ctx the parse tree
	 */
	void enterStructFieldAssign(CSoftParser.StructFieldAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#structFieldAssign}.
	 * @param ctx the parse tree
	 */
	void exitStructFieldAssign(CSoftParser.StructFieldAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#structFieldAccess}.
	 * @param ctx the parse tree
	 */
	void enterStructFieldAccess(CSoftParser.StructFieldAccessContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#structFieldAccess}.
	 * @param ctx the parse tree
	 */
	void exitStructFieldAccess(CSoftParser.StructFieldAccessContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#arrayAccess}.
	 * @param ctx the parse tree
	 */
	void enterArrayAccess(CSoftParser.ArrayAccessContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#arrayAccess}.
	 * @param ctx the parse tree
	 */
	void exitArrayAccess(CSoftParser.ArrayAccessContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#funcCall}.
	 * @param ctx the parse tree
	 */
	void enterFuncCall(CSoftParser.FuncCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#funcCall}.
	 * @param ctx the parse tree
	 */
	void exitFuncCall(CSoftParser.FuncCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(CSoftParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(CSoftParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(CSoftParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(CSoftParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#funType}.
	 * @param ctx the parse tree
	 */
	void enterFunType(CSoftParser.FunTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#funType}.
	 * @param ctx the parse tree
	 */
	void exitFunType(CSoftParser.FunTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#funName}.
	 * @param ctx the parse tree
	 */
	void enterFunName(CSoftParser.FunNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#funName}.
	 * @param ctx the parse tree
	 */
	void exitFunName(CSoftParser.FunNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSoftParser#structName}.
	 * @param ctx the parse tree
	 */
	void enterStructName(CSoftParser.StructNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSoftParser#structName}.
	 * @param ctx the parse tree
	 */
	void exitStructName(CSoftParser.StructNameContext ctx);
}