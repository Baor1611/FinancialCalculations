from ASTUtils import *
import math

class CodeRunner:
    def __init__(self):
        self.variables = {}

    def visitProg(self, ctx: Prog):
        for statement in ctx.statements:
            statement.accept(self)
        return self.variables

    def visitAssign(self, ctx: Assign):
        value = ctx.value.accept(self)
        self.variables[ctx.name] = value
        return value

    def visitBinOp(self, ctx: BinOp):
        left = ctx.left.accept(self)
        right = ctx.right.accept(self)

        if ctx.op == "+":
            return left + right
        elif ctx.op == "-":
            return left - right
        elif ctx.op == "*":
            return left * right
        elif ctx.op == "/":
            if right == 0:
                raise ZeroDivisionError("Division by zero.")
            return left / right
        elif ctx.op == "^":
            return math.pow(left, right)

    def visitFloat(self, ctx: Float):
        return ctx.value

    def visitVar(self, ctx: Var):
        if ctx.name in self.variables:
            return self.variables[ctx.name]
        else:
            raise NameError(f"Variable '{ctx.name}' is not defined.")

    def visitParens(self, ctx: Parens):
        return ctx.expr.accept(self)

