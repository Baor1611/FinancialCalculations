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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\7\13\60\n\13\f\13\16\13\63\13")
        buf.write("\13\3\f\6\f\66\n\f\r\f\16\f\67\3\f\3\f\6\f<\n\f\r\f\16")
        buf.write("\f=\5\f@\n\f\3\r\6\rC\n\r\r\r\16\rD\3\r\3\r\2\2\16\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2L\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3")
        buf.write("\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3")
        buf.write("\2\2\2\r%\3\2\2\2\17\'\3\2\2\2\21)\3\2\2\2\23+\3\2\2\2")
        buf.write("\25-\3\2\2\2\27\65\3\2\2\2\31B\3\2\2\2\33\34\7?\2\2\34")
        buf.write("\4\3\2\2\2\35\36\7=\2\2\36\6\3\2\2\2\37 \7*\2\2 \b\3\2")
        buf.write("\2\2!\"\7+\2\2\"\n\3\2\2\2#$\7-\2\2$\f\3\2\2\2%&\7/\2")
        buf.write("\2&\16\3\2\2\2\'(\7,\2\2(\20\3\2\2\2)*\7\61\2\2*\22\3")
        buf.write("\2\2\2+,\7`\2\2,\24\3\2\2\2-\61\t\2\2\2.\60\t\3\2\2/.")
        buf.write("\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\26")
        buf.write("\3\2\2\2\63\61\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\66")
        buf.write("\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28?\3\2\2\29;\7\60")
        buf.write("\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2")
        buf.write(">@\3\2\2\2?9\3\2\2\2?@\3\2\2\2@\30\3\2\2\2AC\t\5\2\2B")
        buf.write("A\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2FG\b")
        buf.write("\r\2\2G\32\3\2\2\2\b\2\61\67=?D\3\b\2\2")
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
    POW = 9
    ID = 10
    NUMBER = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "POW", "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ADD", "SUB", "MUL", "DIV", 
                  "POW", "ID", "NUMBER", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


