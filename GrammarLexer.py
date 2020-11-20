# Generated from Grammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("m\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\16\6\16^\n\16\r\16\16\16_\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\6\17h\n\17\r\17\16\17i\3\20\3\20\2\2\21\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\2\3\2\4\5\2\13\f\17\17\"\"\5\2\62;C\\c|\2o\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\3!\3\2\2\2\5-\3\2\2\2\7/\3\2\2\2\t\61")
        buf.write("\3\2\2\2\138\3\2\2\2\r:\3\2\2\2\17A\3\2\2\2\21F\3\2\2")
        buf.write("\2\23L\3\2\2\2\25P\3\2\2\2\27W\3\2\2\2\31Z\3\2\2\2\33")
        buf.write("]\3\2\2\2\35g\3\2\2\2\37k\3\2\2\2!\"\7K\2\2\"#\7P\2\2")
        buf.write("#$\7U\2\2$%\7G\2\2%&\7T\2\2&\'\7V\2\2\'(\7\"\2\2()\7K")
        buf.write("\2\2)*\7P\2\2*+\7V\2\2+,\7Q\2\2,\4\3\2\2\2-.\7*\2\2.\6")
        buf.write("\3\2\2\2/\60\7+\2\2\60\b\3\2\2\2\61\62\7X\2\2\62\63\7")
        buf.write("C\2\2\63\64\7N\2\2\64\65\7W\2\2\65\66\7G\2\2\66\67\7U")
        buf.write("\2\2\67\n\3\2\2\289\7.\2\29\f\3\2\2\2:;\7U\2\2;<\7G\2")
        buf.write("\2<=\7N\2\2=>\7G\2\2>?\7E\2\2?@\7V\2\2@\16\3\2\2\2AB\7")
        buf.write("H\2\2BC\7T\2\2CD\7Q\2\2DE\7O\2\2E\20\3\2\2\2FG\7Y\2\2")
        buf.write("GH\7J\2\2HI\7G\2\2IJ\7T\2\2JK\7G\2\2K\22\3\2\2\2LM\7C")
        buf.write("\2\2MN\7X\2\2NO\7I\2\2O\24\3\2\2\2PQ\7O\2\2QR\7G\2\2R")
        buf.write("S\7F\2\2ST\7K\2\2TU\7C\2\2UV\7P\2\2V\26\3\2\2\2WX\7P\2")
        buf.write("\2XY\7Q\2\2Y\30\3\2\2\2Z[\7?\2\2[\32\3\2\2\2\\^\t\2\2")
        buf.write("\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2")
        buf.write("ab\b\16\2\2b\34\3\2\2\2ch\5\37\20\2dh\7a\2\2ef\7^\2\2")
        buf.write("fh\7$\2\2gc\3\2\2\2gd\3\2\2\2ge\3\2\2\2hi\3\2\2\2ig\3")
        buf.write("\2\2\2ij\3\2\2\2j\36\3\2\2\2kl\t\3\2\2l \3\2\2\2\6\2_")
        buf.write("gi\3\b\2\2")
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
    T__11 = 12
    WHITESPACE = 13
    IDENTIFIER = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'INSERT INTO'", "'('", "')'", "'VALUES'", "','", "'SELECT'", 
            "'FROM'", "'WHERE'", "'AVG'", "'MEDIAN'", "'NO'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WHITESPACE", "IDENTIFIER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "WHITESPACE", 
                  "IDENTIFIER", "NUM_LETTER" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


