# Generated from Grammar.g4 by ANTLR 4.8
# encoding: utf-8
import os
from distutils.util import strtobool
import opendp.whitenoise.core as wn
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\5\2\'")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\7\4\66\n\4\f\4\16\49\13\4\3\5\3\5\3\5\7\5>\n\5\f\5")
        buf.write("\16\5A\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7")
        buf.write("\7M\n\7\f\7\16\7P\13\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36\2\3\3\2\13\f\2]\2&\3\2\2\2\4(\3\2\2\2\6\62")
        buf.write("\3\2\2\2\b:\3\2\2\2\nB\3\2\2\2\fI\3\2\2\2\16Q\3\2\2\2")
        buf.write("\20V\3\2\2\2\22X\3\2\2\2\24Z\3\2\2\2\26^\3\2\2\2\30`\3")
        buf.write("\2\2\2\32b\3\2\2\2\34d\3\2\2\2\36f\3\2\2\2 !\5\n\6\2!")
        buf.write("\"\7\2\2\3\"\'\3\2\2\2#$\5\4\3\2$%\7\2\2\3%\'\3\2\2\2")
        buf.write("& \3\2\2\2&#\3\2\2\2\'\3\3\2\2\2()\7\3\2\2)*\5\32\16\2")
        buf.write("*+\7\4\2\2+,\5\6\4\2,-\7\5\2\2-.\7\6\2\2./\7\4\2\2/\60")
        buf.write("\5\b\5\2\60\61\7\5\2\2\61\5\3\2\2\2\62\67\5\26\f\2\63")
        buf.write("\64\7\7\2\2\64\66\5\26\f\2\65\63\3\2\2\2\669\3\2\2\2\67")
        buf.write("\65\3\2\2\2\678\3\2\2\28\7\3\2\2\29\67\3\2\2\2:?\5\30")
        buf.write("\r\2;<\7\7\2\2<>\5\30\r\2=;\3\2\2\2>A\3\2\2\2?=\3\2\2")
        buf.write("\2?@\3\2\2\2@\t\3\2\2\2A?\3\2\2\2BC\7\b\2\2CD\5\f\7\2")
        buf.write("DE\7\t\2\2EF\5\22\n\2FG\7\n\2\2GH\5\24\13\2H\13\3\2\2")
        buf.write("\2IN\5\16\b\2JK\7\7\2\2KM\5\16\b\2LJ\3\2\2\2MP\3\2\2\2")
        buf.write("NL\3\2\2\2NO\3\2\2\2O\r\3\2\2\2PN\3\2\2\2QR\5\20\t\2R")
        buf.write("S\7\4\2\2ST\5\34\17\2TU\7\5\2\2U\17\3\2\2\2VW\t\2\2\2")
        buf.write("W\21\3\2\2\2XY\5\36\20\2Y\23\3\2\2\2Z[\5\34\17\2[\\\7")
        buf.write("\r\2\2\\]\7\17\2\2]\25\3\2\2\2^_\7\17\2\2_\27\3\2\2\2")
        buf.write("`a\7\17\2\2a\31\3\2\2\2bc\7\17\2\2c\33\3\2\2\2de\7\17")
        buf.write("\2\2e\35\3\2\2\2fg\7\17\2\2g\37\3\2\2\2\6&\67?N")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'INSERT INTO'", "'('", "')'", "'VALUES'", 
                     "','", "'SELECT'", "'FROM'", "'WHERE'", "'AVG'", "'HISTOGRAM'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WHITESPACE", "IDENTIFIER" ]

    RULE_start = 0
    RULE_insert1 = 1
    RULE_columns_list = 2
    RULE_values_list = 3
    RULE_select1 = 4
    RULE_set_list = 5
    RULE_pair = 6
    RULE_function = 7
    RULE_from_list = 8
    RULE_condition = 9
    RULE_column = 10
    RULE_value = 11
    RULE_table_name = 12
    RULE_attribute = 13
    RULE_relation = 14

    ruleNames =  [ "start", "insert1", "columns_list", "values_list", "select1", 
                   "set_list", "pair", "function", "from_list", "condition", 
                   "column", "value", "table_name", "attribute", "relation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    WHITESPACE=12
    IDENTIFIER=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select1(self):
            return self.getTypedRuleContext(GrammarParser.Select1Context,0)


        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def insert1(self):
            return self.getTypedRuleContext(GrammarParser.Insert1Context,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = GrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.select1()
                self.state = 31
                self.match(GrammarParser.EOF)
                pass
            elif token in [GrammarParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.insert1()
                self.state = 34
                self.match(GrammarParser.EOF)
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


    class Insert1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(GrammarParser.Table_nameContext,0)


        def columns_list(self):
            return self.getTypedRuleContext(GrammarParser.Columns_listContext,0)


        def values_list(self):
            return self.getTypedRuleContext(GrammarParser.Values_listContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_insert1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert1" ):
                listener.enterInsert1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert1" ):
                listener.exitInsert1(self)




    def insert1(self):

        localctx = GrammarParser.Insert1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_insert1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(GrammarParser.T__0)
            self.state = 39
            self.table_name()
            self.state = 40
            self.match(GrammarParser.T__1)
            self.state = 41
            self.columns_list()
            self.state = 42
            self.match(GrammarParser.T__2)
            self.state = 43
            self.match(GrammarParser.T__3)
            self.state = 44
            self.match(GrammarParser.T__1)
            self.state = 45
            self.values_list()
            self.state = 46
            self.match(GrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Columns_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ColumnContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ColumnContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_columns_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumns_list" ):
                listener.enterColumns_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumns_list" ):
                listener.exitColumns_list(self)




    def columns_list(self):

        localctx = GrammarParser.Columns_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_columns_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.column()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__4:
                self.state = 49
                self.match(GrammarParser.T__4)
                self.state = 50
                self.column()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Values_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ValueContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ValueContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_values_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues_list" ):
                listener.enterValues_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues_list" ):
                listener.exitValues_list(self)




    def values_list(self):

        localctx = GrammarParser.Values_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_values_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.value()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__4:
                self.state = 57
                self.match(GrammarParser.T__4)
                self.state = 58
                self.value()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_list(self):
            return self.getTypedRuleContext(GrammarParser.Set_listContext,0)


        def from_list(self):
            return self.getTypedRuleContext(GrammarParser.From_listContext,0)


        def condition(self):
            return self.getTypedRuleContext(GrammarParser.ConditionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_select1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect1" ):
                listener.enterSelect1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect1" ):
                listener.exitSelect1(self)




    def select1(self):

        localctx = GrammarParser.Select1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_select1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(GrammarParser.T__5)
            self.state = 65
            self.set_list()
            self.state = 66
            self.match(GrammarParser.T__6)
            self.state = 67
            self.from_list()
            self.state = 68
            self.match(GrammarParser.T__7)
            self.state = 69
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.PairContext)
            else:
                return self.getTypedRuleContext(GrammarParser.PairContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_set_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_list" ):
                listener.enterSet_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_list" ):
                listener.exitSet_list(self)




    def set_list(self):

        localctx = GrammarParser.Set_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_set_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.pair()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__4:
                self.state = 72
                self.match(GrammarParser.T__4)
                self.state = 73
                self.pair()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(GrammarParser.FunctionContext,0)


        def attribute(self):
            return self.getTypedRuleContext(GrammarParser.AttributeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = GrammarParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.function()
            self.state = 80
            self.match(GrammarParser.T__1)
            self.state = 81
            self.attribute()
            self.state = 82
            self.match(GrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = GrammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==GrammarParser.T__8 or _la==GrammarParser.T__9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation(self):
            return self.getTypedRuleContext(GrammarParser.RelationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_from_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_list" ):
                listener.enterFrom_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_list" ):
                listener.exitFrom_list(self)




    def from_list(self):

        localctx = GrammarParser.From_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_from_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.relation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(GrammarParser.AttributeContext,0)


        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = GrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.attribute()
            self.state = 89
            self.match(GrammarParser.T__10)
            self.state = 90
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = GrammarParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = GrammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)




    def table_name(self):

        localctx = GrammarParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = GrammarParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)




    def relation(self):

        localctx = GrammarParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





