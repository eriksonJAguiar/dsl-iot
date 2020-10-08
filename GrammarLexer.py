# Generated from Grammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\6\r")
        buf.write("\\\n\r\r\r\16\r]\3\r\3\r\3\16\3\16\3\16\3\16\6\16f\n\16")
        buf.write("\r\16\16\16g\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\2\3\2\4\5\2")
        buf.write("\13\f\17\17\"\"\5\2\62;C\\c|\2m\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\37\3\2\2\2\5+\3\2")
        buf.write("\2\2\7-\3\2\2\2\t/\3\2\2\2\13\66\3\2\2\2\r8\3\2\2\2\17")
        buf.write("?\3\2\2\2\21D\3\2\2\2\23J\3\2\2\2\25N\3\2\2\2\27X\3\2")
        buf.write("\2\2\31[\3\2\2\2\33e\3\2\2\2\35i\3\2\2\2\37 \7K\2\2 !")
        buf.write("\7P\2\2!\"\7U\2\2\"#\7G\2\2#$\7T\2\2$%\7V\2\2%&\7\"\2")
        buf.write("\2&\'\7K\2\2\'(\7P\2\2()\7V\2\2)*\7Q\2\2*\4\3\2\2\2+,")
        buf.write("\7*\2\2,\6\3\2\2\2-.\7+\2\2.\b\3\2\2\2/\60\7X\2\2\60\61")
        buf.write("\7C\2\2\61\62\7N\2\2\62\63\7W\2\2\63\64\7G\2\2\64\65\7")
        buf.write("U\2\2\65\n\3\2\2\2\66\67\7.\2\2\67\f\3\2\2\289\7U\2\2")
        buf.write("9:\7G\2\2:;\7N\2\2;<\7G\2\2<=\7E\2\2=>\7V\2\2>\16\3\2")
        buf.write("\2\2?@\7H\2\2@A\7T\2\2AB\7Q\2\2BC\7O\2\2C\20\3\2\2\2D")
        buf.write("E\7Y\2\2EF\7J\2\2FG\7G\2\2GH\7T\2\2HI\7G\2\2I\22\3\2\2")
        buf.write("\2JK\7C\2\2KL\7X\2\2LM\7I\2\2M\24\3\2\2\2NO\7J\2\2OP\7")
        buf.write("K\2\2PQ\7U\2\2QR\7V\2\2RS\7Q\2\2ST\7I\2\2TU\7T\2\2UV\7")
        buf.write("C\2\2VW\7O\2\2W\26\3\2\2\2XY\7?\2\2Y\30\3\2\2\2Z\\\t\2")
        buf.write("\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2")
        buf.write("\2_`\b\r\2\2`\32\3\2\2\2af\5\35\17\2bf\7a\2\2cd\7^\2\2")
        buf.write("df\7$\2\2ea\3\2\2\2eb\3\2\2\2ec\3\2\2\2fg\3\2\2\2ge\3")
        buf.write("\2\2\2gh\3\2\2\2h\34\3\2\2\2ij\t\3\2\2j\36\3\2\2\2\6\2")
        buf.write("]eg\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    WHITESPACE = 12
    IDENTIFIER = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'INSERT INTO'", "'('", "')'", "'VALUES'", "','", "'SELECT'", 
            "'FROM'", "'WHERE'", "'AVG'", "'HISTOGRAM'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WHITESPACE", "IDENTIFIER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "WHITESPACE", "IDENTIFIER", 
                  "NUM_LETTER" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


