# Generated from Sample.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5%\n\5\f\5")
        buf.write("\16\5(\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\60\n\6\f\6\16")
        buf.write("\6\63\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7;\n\7\f\7\16\7>")
        buf.write("\13\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bF\n\b\3\b\2\5\b\n\f\t")
        buf.write("\2\4\6\b\n\f\16\2\4\3\2\7\b\3\2\t\n\2G\2\21\3\2\2\2\4")
        buf.write("\27\3\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n)\3\2\2\2\f\64")
        buf.write("\3\2\2\2\16E\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\23")
        buf.write("\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\30")
        buf.write("\5\6\4\2\26\30\5\b\5\2\27\25\3\2\2\2\27\26\3\2\2\2\30")
        buf.write("\5\3\2\2\2\31\32\7\f\2\2\32\33\7\3\2\2\33\34\5\b\5\2\34")
        buf.write("\35\7\4\2\2\35\7\3\2\2\2\36\37\b\5\1\2\37 \5\n\6\2 &\3")
        buf.write("\2\2\2!\"\f\4\2\2\"#\t\2\2\2#%\5\n\6\2$!\3\2\2\2%(\3\2")
        buf.write("\2\2&$\3\2\2\2&\'\3\2\2\2\'\t\3\2\2\2(&\3\2\2\2)*\b\6")
        buf.write("\1\2*+\5\f\7\2+\61\3\2\2\2,-\f\4\2\2-.\t\3\2\2.\60\5\f")
        buf.write("\7\2/,\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\13\3\2\2\2\63\61\3\2\2\2\64\65\b\7\1\2\65\66\5\16")
        buf.write("\b\2\66<\3\2\2\2\678\f\4\2\289\7\13\2\29;\5\16\b\2:\67")
        buf.write("\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\r\3\2\2\2><\3")
        buf.write("\2\2\2?@\7\5\2\2@A\5\b\5\2AB\7\6\2\2BF\3\2\2\2CF\7\f\2")
        buf.write("\2DF\7\r\2\2E?\3\2\2\2EC\3\2\2\2ED\3\2\2\2F\17\3\2\2\2")
        buf.write("\b\23\27&\61<E")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ADD", "SUB", "MUL", "DIV", "POW", "ID", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_atom = 6

    ruleNames =  [ "program", "statement", "assignment", "expression", "term", 
                   "factor", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ADD=5
    SUB=6
    MUL=7
    DIV=8
    POW=9
    ID=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampleParser.StatementContext)
            else:
                return self.getTypedRuleContext(SampleParser.StatementContext,i)


        def getRuleIndex(self):
            return SampleParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SampleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__2) | (1 << SampleParser.ID) | (1 << SampleParser.NUMBER))) != 0)):
                    break

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

        def assignment(self):
            return self.getTypedRuleContext(SampleParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SampleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expression(0)
                pass


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
            return self.getToken(SampleParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SampleParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(SampleParser.ID)
            self.state = 24
            self.match(SampleParser.T__0)
            self.state = 25
            self.expression(0)
            self.state = 26
            self.match(SampleParser.T__1)
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

        def term(self):
            return self.getTypedRuleContext(SampleParser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


        def ADD(self):
            return self.getToken(SampleParser.ADD, 0)

        def SUB(self):
            return self.getToken(SampleParser.SUB, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SampleParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SampleParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 31
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 32
                    _la = self._input.LA(1)
                    if not(_la==SampleParser.ADD or _la==SampleParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 33
                    self.term(0) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(SampleParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(SampleParser.TermContext,0)


        def MUL(self):
            return self.getToken(SampleParser.MUL, 0)

        def DIV(self):
            return self.getToken(SampleParser.DIV, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SampleParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SampleParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 42
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 43
                    _la = self._input.LA(1)
                    if not(_la==SampleParser.MUL or _la==SampleParser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 44
                    self.factor(0) 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(SampleParser.AtomContext,0)


        def factor(self):
            return self.getTypedRuleContext(SampleParser.FactorContext,0)


        def POW(self):
            return self.getToken(SampleParser.POW, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SampleParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SampleParser.FactorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 53
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 54
                    self.match(SampleParser.POW)
                    self.state = 55
                    self.atom() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def NUMBER(self):
            return self.getToken(SampleParser.NUMBER, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SampleParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SampleParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(SampleParser.T__2)
                self.state = 62
                self.expression(0)
                self.state = 63
                self.match(SampleParser.T__3)
                pass
            elif token in [SampleParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(SampleParser.ID)
                pass
            elif token in [SampleParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.match(SampleParser.NUMBER)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        self._predicates[4] = self.term_sempred
        self._predicates[5] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




