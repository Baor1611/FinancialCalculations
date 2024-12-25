from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

class AST(ABC):
    @abstractmethod
    def accept(self, v):
        pass

@dataclass
class Prog(AST):
    statements: List[AST]

    def __str__(self):
        return f"Prog({self.statements})"

    def accept(self, v):
        return v.visitProg(self)

@dataclass
class Assign(AST):
    name: str
    value: AST

    def __str__(self):
        return f"Assign({self.name}, {self.value})"

    def accept(self, v):
        return v.visitAssign(self)

@dataclass
class BinOp(AST):
    op: str
    left: AST
    right: AST

    def __str__(self):
        return f"BinOp(\"{self.op}\", {self.left}, {self.right})"

    def accept(self, v):
        return v.visitBinOp(self)

@dataclass
class Float(AST):
    value: float

    def __str__(self):
        return f"Float({self.value})"

    def accept(self, v):
        return v.visitFloat(self)

@dataclass
class Var(AST):
    name: str

    def __str__(self):
        return f"Var(\"{self.name}\")"

    def accept(self, v):
        return v.visitVar(self)

@dataclass
class Parens(AST):
    expr: AST

    def __str__(self):
        return f"Parens({self.expr})"

    def accept(self, v):
        return v.visitParens(self)

