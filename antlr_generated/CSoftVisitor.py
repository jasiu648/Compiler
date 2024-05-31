# Generated from CSoft.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSoftParser import CSoftParser
else:
    from CSoftParser import CSoftParser

# This class defines a complete generic visitor for a parse tree produced by CSoftParser.

class CSoftVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSoftParser#type.
    def visitType(self, ctx:CSoftParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#prog.
    def visitProg(self, ctx:CSoftParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#print.
    def visitPrint(self, ctx:CSoftParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#read.
    def visitRead(self, ctx:CSoftParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#exprression.
    def visitExprression(self, ctx:CSoftParser.ExprressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#assign.
    def visitAssign(self, ctx:CSoftParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#elementAssign.
    def visitElementAssign(self, ctx:CSoftParser.ElementAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#arrAssign.
    def visitArrAssign(self, ctx:CSoftParser.ArrAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#repeatStatement.
    def visitRepeatStatement(self, ctx:CSoftParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#ifStatement.
    def visitIfStatement(self, ctx:CSoftParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#whileLoop.
    def visitWhileLoop(self, ctx:CSoftParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#funcDecl.
    def visitFuncDecl(self, ctx:CSoftParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structDeclaration.
    def visitStructDeclaration(self, ctx:CSoftParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structFieldAssignment.
    def visitStructFieldAssignment(self, ctx:CSoftParser.StructFieldAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structAssignmet.
    def visitStructAssignmet(self, ctx:CSoftParser.StructAssignmetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CSoftParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#classAssignment.
    def visitClassAssignment(self, ctx:CSoftParser.ClassAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#ident.
    def visitIdent(self, ctx:CSoftParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#assignment.
    def visitAssignment(self, ctx:CSoftParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#print_statement.
    def visitPrint_statement(self, ctx:CSoftParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#read_statement.
    def visitRead_statement(self, ctx:CSoftParser.Read_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#arrayAssign.
    def visitArrayAssign(self, ctx:CSoftParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#expr.
    def visitExpr(self, ctx:CSoftParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#condXorStm.
    def visitCondXorStm(self, ctx:CSoftParser.CondXorStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#condStmAnd.
    def visitCondStmAnd(self, ctx:CSoftParser.CondStmAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#condStmRel.
    def visitCondStmRel(self, ctx:CSoftParser.CondStmRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#addExpr.
    def visitAddExpr(self, ctx:CSoftParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#multExpr.
    def visitMultExpr(self, ctx:CSoftParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#negFactor.
    def visitNegFactor(self, ctx:CSoftParser.NegFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#factor.
    def visitFactor(self, ctx:CSoftParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#ifStm.
    def visitIfStm(self, ctx:CSoftParser.IfStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockIf.
    def visitBlockIf(self, ctx:CSoftParser.BlockIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#repeatStm.
    def visitRepeatStm(self, ctx:CSoftParser.RepeatStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#repNum.
    def visitRepNum(self, ctx:CSoftParser.RepNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockRepeat.
    def visitBlockRepeat(self, ctx:CSoftParser.BlockRepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#whileL.
    def visitWhileL(self, ctx:CSoftParser.WhileLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockWhile.
    def visitBlockWhile(self, ctx:CSoftParser.BlockWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#function.
    def visitFunction(self, ctx:CSoftParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockFun.
    def visitBlockFun(self, ctx:CSoftParser.BlockFunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#classDecl.
    def visitClassDecl(self, ctx:CSoftParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockClass.
    def visitBlockClass(self, ctx:CSoftParser.BlockClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#method.
    def visitMethod(self, ctx:CSoftParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockMethod.
    def visitBlockMethod(self, ctx:CSoftParser.BlockMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#methodType.
    def visitMethodType(self, ctx:CSoftParser.MethodTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#methodName.
    def visitMethodName(self, ctx:CSoftParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#className.
    def visitClassName(self, ctx:CSoftParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#methodCall.
    def visitMethodCall(self, ctx:CSoftParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#classAssign.
    def visitClassAssign(self, ctx:CSoftParser.ClassAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#parameters.
    def visitParameters(self, ctx:CSoftParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#parameter.
    def visitParameter(self, ctx:CSoftParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structDecl.
    def visitStructDecl(self, ctx:CSoftParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#blockStruct.
    def visitBlockStruct(self, ctx:CSoftParser.BlockStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structVarDecl.
    def visitStructVarDecl(self, ctx:CSoftParser.StructVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structAssign.
    def visitStructAssign(self, ctx:CSoftParser.StructAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structFieldAssign.
    def visitStructFieldAssign(self, ctx:CSoftParser.StructFieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structFieldAccess.
    def visitStructFieldAccess(self, ctx:CSoftParser.StructFieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#arrayAccess.
    def visitArrayAccess(self, ctx:CSoftParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#funcCall.
    def visitFuncCall(self, ctx:CSoftParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#funType.
    def visitFunType(self, ctx:CSoftParser.FunTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#funName.
    def visitFunName(self, ctx:CSoftParser.FunNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSoftParser#structName.
    def visitStructName(self, ctx:CSoftParser.StructNameContext):
        return self.visitChildren(ctx)



del CSoftParser