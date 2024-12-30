from CompiledFiles.SampleVisitor import SampleVisitor
from CompiledFiles.SampleParser import SampleParser
from ASTUtils import *

class ASTGeneration(SampleVisitor):
    def visitProgram(self, ctx: SampleParser.ProgramContext):
        statements = [stmt.accept(self) for stmt in ctx.statement()]
        return Prog(statements)

    def visitStatement(self, ctx: SampleParser.StatementContext):
        return ctx.assignment().accept(self)

    def visitAssignment(self, ctx: SampleParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = ctx.expression().accept(self)
        return Assign(var_name, value)

    def visitExpression(self, ctx: SampleParser.ExpressionContext):
        if ctx.expression():
            op = "+" if ctx.ADD() else "-"
            return BinOp(op, ctx.expression().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: SampleParser.TermContext):
        if ctx.term():
            op = "*" if ctx.MUL() else "/"
            return BinOp(op, ctx.term().accept(self), ctx.factor().accept(self))
        else:
            return ctx.factor().accept(self)
        
    def visitFactor(self, ctx: SampleParser.FactorContext):
        if ctx.factor():
            return BinOp("^", ctx.factor().accept(self), ctx.atom().accept(self))
        else:
            return ctx.atom().accept(self)
         
    def visitAtom(self, ctx: SampleParser.FactorContext):
        if ctx.expression():
            return Parens(ctx.expression().accept(self))
        elif ctx.ID():
            return Var(ctx.ID().getText())
        elif ctx.NUMBER():
            return Float(float(ctx.NUMBER().getText()))

