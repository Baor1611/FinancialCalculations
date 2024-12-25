# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("D\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\7\n,\n\n\f\n\16\n/\13\n\3\13\6\13\62\n\13\r\13")
        buf.write("\16\13\63\3\13\3\13\6\138\n\13\r\13\16\139\5\13<\n\13")
        buf.write("\3\f\6\f?\n\f\r\f\16\f@\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\6\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2H\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3")
        buf.write("\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r#\3\2\2\2\17%\3\2\2\2")
        buf.write("\21\'\3\2\2\2\23)\3\2\2\2\25\61\3\2\2\2\27>\3\2\2\2\31")
        buf.write("\32\7?\2\2\32\4\3\2\2\2\33\34\7=\2\2\34\6\3\2\2\2\35\36")
        buf.write("\7*\2\2\36\b\3\2\2\2\37 \7+\2\2 \n\3\2\2\2!\"\7-\2\2\"")
        buf.write("\f\3\2\2\2#$\7/\2\2$\16\3\2\2\2%&\7,\2\2&\20\3\2\2\2\'")
        buf.write("(\7\61\2\2(\22\3\2\2\2)-\t\2\2\2*,\t\3\2\2+*\3\2\2\2,")
        buf.write("/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\24\3\2\2\2/-\3\2\2\2\60")
        buf.write("\62\t\4\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64;\3\2\2\2\65\67\7\60\2\2\668\t\4\2\2")
        buf.write("\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2")
        buf.write("\2;\65\3\2\2\2;<\3\2\2\2<\26\3\2\2\2=?\t\5\2\2>=\3\2\2")
        buf.write("\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\b\f\2\2C")
        buf.write("\30\3\2\2\2\b\2-\639;@\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ADD = 5
    SUB = 6
    MUL = 7
    DIV = 8
    ID = 9
    NUMBER = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ADD", "SUB", "MUL", "DIV", 
                  "ID", "NUMBER", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


