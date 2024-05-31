# Generated from ./antlr_generated/CSoft.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSoftParser import CSoftParser
else:
    from CSoftParser import CSoftParser

# This class defines a complete listener for a parse tree produced by CSoftParser.
class CSoftListener(ParseTreeListener):

    # Enter a parse tree produced by CSoftParser#type.
    def enterType(self, ctx:CSoftParser.TypeContext):
        pass

    # Exit a parse tree produced by CSoftParser#type.
    def exitType(self, ctx:CSoftParser.TypeContext):
        pass


    # Enter a parse tree produced by CSoftParser#prog.
    def enterProg(self, ctx:CSoftParser.ProgContext):
        pass

    # Exit a parse tree produced by CSoftParser#prog.
    def exitProg(self, ctx:CSoftParser.ProgContext):
        pass


    # Enter a parse tree produced by CSoftParser#print.
    def enterPrint(self, ctx:CSoftParser.PrintContext):
        pass

    # Exit a parse tree produced by CSoftParser#print.
    def exitPrint(self, ctx:CSoftParser.PrintContext):
        pass


    # Enter a parse tree produced by CSoftParser#read.
    def enterRead(self, ctx:CSoftParser.ReadContext):
        pass

    # Exit a parse tree produced by CSoftParser#read.
    def exitRead(self, ctx:CSoftParser.ReadContext):
        pass


    # Enter a parse tree produced by CSoftParser#exprression.
    def enterExprression(self, ctx:CSoftParser.ExprressionContext):
        pass

    # Exit a parse tree produced by CSoftParser#exprression.
    def exitExprression(self, ctx:CSoftParser.ExprressionContext):
        pass


    # Enter a parse tree produced by CSoftParser#assign.
    def enterAssign(self, ctx:CSoftParser.AssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#assign.
    def exitAssign(self, ctx:CSoftParser.AssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#elementAssign.
    def enterElementAssign(self, ctx:CSoftParser.ElementAssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#elementAssign.
    def exitElementAssign(self, ctx:CSoftParser.ElementAssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#arrAssign.
    def enterArrAssign(self, ctx:CSoftParser.ArrAssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#arrAssign.
    def exitArrAssign(self, ctx:CSoftParser.ArrAssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#repeatStatement.
    def enterRepeatStatement(self, ctx:CSoftParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by CSoftParser#repeatStatement.
    def exitRepeatStatement(self, ctx:CSoftParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by CSoftParser#ifStatement.
    def enterIfStatement(self, ctx:CSoftParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CSoftParser#ifStatement.
    def exitIfStatement(self, ctx:CSoftParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CSoftParser#funcDecl.
    def enterFuncDecl(self, ctx:CSoftParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by CSoftParser#funcDecl.
    def exitFuncDecl(self, ctx:CSoftParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by CSoftParser#structDeclaration.
    def enterStructDeclaration(self, ctx:CSoftParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by CSoftParser#structDeclaration.
    def exitStructDeclaration(self, ctx:CSoftParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by CSoftParser#structFieldAssignment.
    def enterStructFieldAssignment(self, ctx:CSoftParser.StructFieldAssignmentContext):
        pass

    # Exit a parse tree produced by CSoftParser#structFieldAssignment.
    def exitStructFieldAssignment(self, ctx:CSoftParser.StructFieldAssignmentContext):
        pass


    # Enter a parse tree produced by CSoftParser#structAssignmet.
    def enterStructAssignmet(self, ctx:CSoftParser.StructAssignmetContext):
        pass

    # Exit a parse tree produced by CSoftParser#structAssignmet.
    def exitStructAssignmet(self, ctx:CSoftParser.StructAssignmetContext):
        pass


    # Enter a parse tree produced by CSoftParser#classDeclaration.
    def enterClassDeclaration(self, ctx:CSoftParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by CSoftParser#classDeclaration.
    def exitClassDeclaration(self, ctx:CSoftParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by CSoftParser#classAssignment.
    def enterClassAssignment(self, ctx:CSoftParser.ClassAssignmentContext):
        pass

    # Exit a parse tree produced by CSoftParser#classAssignment.
    def exitClassAssignment(self, ctx:CSoftParser.ClassAssignmentContext):
        pass


    # Enter a parse tree produced by CSoftParser#ident.
    def enterIdent(self, ctx:CSoftParser.IdentContext):
        pass

    # Exit a parse tree produced by CSoftParser#ident.
    def exitIdent(self, ctx:CSoftParser.IdentContext):
        pass


    # Enter a parse tree produced by CSoftParser#assignment.
    def enterAssignment(self, ctx:CSoftParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CSoftParser#assignment.
    def exitAssignment(self, ctx:CSoftParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CSoftParser#print_statement.
    def enterPrint_statement(self, ctx:CSoftParser.Print_statementContext):
        pass

    # Exit a parse tree produced by CSoftParser#print_statement.
    def exitPrint_statement(self, ctx:CSoftParser.Print_statementContext):
        pass


    # Enter a parse tree produced by CSoftParser#read_statement.
    def enterRead_statement(self, ctx:CSoftParser.Read_statementContext):
        pass

    # Exit a parse tree produced by CSoftParser#read_statement.
    def exitRead_statement(self, ctx:CSoftParser.Read_statementContext):
        pass


    # Enter a parse tree produced by CSoftParser#arrayAssign.
    def enterArrayAssign(self, ctx:CSoftParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#arrayAssign.
    def exitArrayAssign(self, ctx:CSoftParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#expr.
    def enterExpr(self, ctx:CSoftParser.ExprContext):
        pass

    # Exit a parse tree produced by CSoftParser#expr.
    def exitExpr(self, ctx:CSoftParser.ExprContext):
        pass


    # Enter a parse tree produced by CSoftParser#condXorStm.
    def enterCondXorStm(self, ctx:CSoftParser.CondXorStmContext):
        pass

    # Exit a parse tree produced by CSoftParser#condXorStm.
    def exitCondXorStm(self, ctx:CSoftParser.CondXorStmContext):
        pass


    # Enter a parse tree produced by CSoftParser#condStmAnd.
    def enterCondStmAnd(self, ctx:CSoftParser.CondStmAndContext):
        pass

    # Exit a parse tree produced by CSoftParser#condStmAnd.
    def exitCondStmAnd(self, ctx:CSoftParser.CondStmAndContext):
        pass


    # Enter a parse tree produced by CSoftParser#condStmRel.
    def enterCondStmRel(self, ctx:CSoftParser.CondStmRelContext):
        pass

    # Exit a parse tree produced by CSoftParser#condStmRel.
    def exitCondStmRel(self, ctx:CSoftParser.CondStmRelContext):
        pass


    # Enter a parse tree produced by CSoftParser#addExpr.
    def enterAddExpr(self, ctx:CSoftParser.AddExprContext):
        pass

    # Exit a parse tree produced by CSoftParser#addExpr.
    def exitAddExpr(self, ctx:CSoftParser.AddExprContext):
        pass


    # Enter a parse tree produced by CSoftParser#multExpr.
    def enterMultExpr(self, ctx:CSoftParser.MultExprContext):
        pass

    # Exit a parse tree produced by CSoftParser#multExpr.
    def exitMultExpr(self, ctx:CSoftParser.MultExprContext):
        pass


    # Enter a parse tree produced by CSoftParser#negFactor.
    def enterNegFactor(self, ctx:CSoftParser.NegFactorContext):
        pass

    # Exit a parse tree produced by CSoftParser#negFactor.
    def exitNegFactor(self, ctx:CSoftParser.NegFactorContext):
        pass


    # Enter a parse tree produced by CSoftParser#factor.
    def enterFactor(self, ctx:CSoftParser.FactorContext):
        pass

    # Exit a parse tree produced by CSoftParser#factor.
    def exitFactor(self, ctx:CSoftParser.FactorContext):
        pass


    # Enter a parse tree produced by CSoftParser#ifStm.
    def enterIfStm(self, ctx:CSoftParser.IfStmContext):
        pass

    # Exit a parse tree produced by CSoftParser#ifStm.
    def exitIfStm(self, ctx:CSoftParser.IfStmContext):
        pass


    # Enter a parse tree produced by CSoftParser#blockIf.
    def enterBlockIf(self, ctx:CSoftParser.BlockIfContext):
        pass

    # Exit a parse tree produced by CSoftParser#blockIf.
    def exitBlockIf(self, ctx:CSoftParser.BlockIfContext):
        pass


    # Enter a parse tree produced by CSoftParser#repeatStm.
    def enterRepeatStm(self, ctx:CSoftParser.RepeatStmContext):
        pass

    # Exit a parse tree produced by CSoftParser#repeatStm.
    def exitRepeatStm(self, ctx:CSoftParser.RepeatStmContext):
        pass


    # Enter a parse tree produced by CSoftParser#repNum.
    def enterRepNum(self, ctx:CSoftParser.RepNumContext):
        pass

    # Exit a parse tree produced by CSoftParser#repNum.
    def exitRepNum(self, ctx:CSoftParser.RepNumContext):
        pass


    # Enter a parse tree produced by CSoftParser#blockRepeat.
    def enterBlockRepeat(self, ctx:CSoftParser.BlockRepeatContext):
        pass

    # Exit a parse tree produced by CSoftParser#blockRepeat.
    def exitBlockRepeat(self, ctx:CSoftParser.BlockRepeatContext):
        pass


    # Enter a parse tree produced by CSoftParser#function.
    def enterFunction(self, ctx:CSoftParser.FunctionContext):
        pass

    # Exit a parse tree produced by CSoftParser#function.
    def exitFunction(self, ctx:CSoftParser.FunctionContext):
        pass


    # Enter a parse tree produced by CSoftParser#blockFun.
    def enterBlockFun(self, ctx:CSoftParser.BlockFunContext):
        pass

    # Exit a parse tree produced by CSoftParser#blockFun.
    def exitBlockFun(self, ctx:CSoftParser.BlockFunContext):
        pass


    # Enter a parse tree produced by CSoftParser#classDecl.
    def enterClassDecl(self, ctx:CSoftParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by CSoftParser#classDecl.
    def exitClassDecl(self, ctx:CSoftParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by CSoftParser#blockClass.
    def enterBlockClass(self, ctx:CSoftParser.BlockClassContext):
        pass

    # Exit a parse tree produced by CSoftParser#blockClass.
    def exitBlockClass(self, ctx:CSoftParser.BlockClassContext):
        pass


    # Enter a parse tree produced by CSoftParser#method.
    def enterMethod(self, ctx:CSoftParser.MethodContext):
        pass

    # Exit a parse tree produced by CSoftParser#method.
    def exitMethod(self, ctx:CSoftParser.MethodContext):
        pass


    # Enter a parse tree produced by CSoftParser#blockMethod.
    def enterBlockMethod(self, ctx:CSoftParser.BlockMethodContext):
        pass

    # Exit a parse tree produced by CSoftParser#blockMethod.
    def exitBlockMethod(self, ctx:CSoftParser.BlockMethodContext):
        pass


    # Enter a parse tree produced by CSoftParser#methodType.
    def enterMethodType(self, ctx:CSoftParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by CSoftParser#methodType.
    def exitMethodType(self, ctx:CSoftParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by CSoftParser#methodName.
    def enterMethodName(self, ctx:CSoftParser.MethodNameContext):
        pass

    # Exit a parse tree produced by CSoftParser#methodName.
    def exitMethodName(self, ctx:CSoftParser.MethodNameContext):
        pass


    # Enter a parse tree produced by CSoftParser#className.
    def enterClassName(self, ctx:CSoftParser.ClassNameContext):
        pass

    # Exit a parse tree produced by CSoftParser#className.
    def exitClassName(self, ctx:CSoftParser.ClassNameContext):
        pass


    # Enter a parse tree produced by CSoftParser#methodCall.
    def enterMethodCall(self, ctx:CSoftParser.MethodCallContext):
        pass

    # Exit a parse tree produced by CSoftParser#methodCall.
    def exitMethodCall(self, ctx:CSoftParser.MethodCallContext):
        pass


    # Enter a parse tree produced by CSoftParser#classAssign.
    def enterClassAssign(self, ctx:CSoftParser.ClassAssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#classAssign.
    def exitClassAssign(self, ctx:CSoftParser.ClassAssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#parameters.
    def enterParameters(self, ctx:CSoftParser.ParametersContext):
        pass

    # Exit a parse tree produced by CSoftParser#parameters.
    def exitParameters(self, ctx:CSoftParser.ParametersContext):
        pass


    # Enter a parse tree produced by CSoftParser#parameter.
    def enterParameter(self, ctx:CSoftParser.ParameterContext):
        pass

    # Exit a parse tree produced by CSoftParser#parameter.
    def exitParameter(self, ctx:CSoftParser.ParameterContext):
        pass


    # Enter a parse tree produced by CSoftParser#structDecl.
    def enterStructDecl(self, ctx:CSoftParser.StructDeclContext):
        pass

    # Exit a parse tree produced by CSoftParser#structDecl.
    def exitStructDecl(self, ctx:CSoftParser.StructDeclContext):
        pass


    # Enter a parse tree produced by CSoftParser#blockStruct.
    def enterBlockStruct(self, ctx:CSoftParser.BlockStructContext):
        pass

    # Exit a parse tree produced by CSoftParser#blockStruct.
    def exitBlockStruct(self, ctx:CSoftParser.BlockStructContext):
        pass


    # Enter a parse tree produced by CSoftParser#structVarDecl.
    def enterStructVarDecl(self, ctx:CSoftParser.StructVarDeclContext):
        pass

    # Exit a parse tree produced by CSoftParser#structVarDecl.
    def exitStructVarDecl(self, ctx:CSoftParser.StructVarDeclContext):
        pass


    # Enter a parse tree produced by CSoftParser#structAssign.
    def enterStructAssign(self, ctx:CSoftParser.StructAssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#structAssign.
    def exitStructAssign(self, ctx:CSoftParser.StructAssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#structFieldAssign.
    def enterStructFieldAssign(self, ctx:CSoftParser.StructFieldAssignContext):
        pass

    # Exit a parse tree produced by CSoftParser#structFieldAssign.
    def exitStructFieldAssign(self, ctx:CSoftParser.StructFieldAssignContext):
        pass


    # Enter a parse tree produced by CSoftParser#structFieldAccess.
    def enterStructFieldAccess(self, ctx:CSoftParser.StructFieldAccessContext):
        pass

    # Exit a parse tree produced by CSoftParser#structFieldAccess.
    def exitStructFieldAccess(self, ctx:CSoftParser.StructFieldAccessContext):
        pass


    # Enter a parse tree produced by CSoftParser#arrayAccess.
    def enterArrayAccess(self, ctx:CSoftParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by CSoftParser#arrayAccess.
    def exitArrayAccess(self, ctx:CSoftParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by CSoftParser#funcCall.
    def enterFuncCall(self, ctx:CSoftParser.FuncCallContext):
        pass

    # Exit a parse tree produced by CSoftParser#funcCall.
    def exitFuncCall(self, ctx:CSoftParser.FuncCallContext):
        pass


    # Enter a parse tree produced by CSoftParser#arguments.
    def enterArguments(self, ctx:CSoftParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by CSoftParser#arguments.
    def exitArguments(self, ctx:CSoftParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by CSoftParser#argument.
    def enterArgument(self, ctx:CSoftParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CSoftParser#argument.
    def exitArgument(self, ctx:CSoftParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CSoftParser#funType.
    def enterFunType(self, ctx:CSoftParser.FunTypeContext):
        pass

    # Exit a parse tree produced by CSoftParser#funType.
    def exitFunType(self, ctx:CSoftParser.FunTypeContext):
        pass


    # Enter a parse tree produced by CSoftParser#funName.
    def enterFunName(self, ctx:CSoftParser.FunNameContext):
        pass

    # Exit a parse tree produced by CSoftParser#funName.
    def exitFunName(self, ctx:CSoftParser.FunNameContext):
        pass


    # Enter a parse tree produced by CSoftParser#structName.
    def enterStructName(self, ctx:CSoftParser.StructNameContext):
        pass

    # Exit a parse tree produced by CSoftParser#structName.
    def exitStructName(self, ctx:CSoftParser.StructNameContext):
        pass



del CSoftParser