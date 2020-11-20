# Generated from Grammar.g4 by ANTLR 4.8
import os
from distutils.util import strtobool
#import opendp.whitenoise.core as wn
#matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt
from numpy import arange

from diff_piv import Diff_priv

import pandas as pd
import numpy as np
import random
import statistics
from collections import Counter

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#start.
    def enterStart(self, ctx:GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by GrammarParser#start.
    def exitStart(self, ctx:GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by GrammarParser#insert1.
    def enterInsert1(self, ctx:GrammarParser.Insert1Context):
        pass

    # Exit a parse tree produced by GrammarParser#insert1.
    def exitInsert1(self, ctx:GrammarParser.Insert1Context):
        pass


    # Enter a parse tree produced by GrammarParser#columns_list.
    def enterColumns_list(self, ctx:GrammarParser.Columns_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#columns_list.
    def exitColumns_list(self, ctx:GrammarParser.Columns_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#values_list.
    def enterValues_list(self, ctx:GrammarParser.Values_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#values_list.
    def exitValues_list(self, ctx:GrammarParser.Values_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#select1.
    def enterSelect1(self, ctx:GrammarParser.Select1Context):
        pass

    # Exit a parse tree produced by GrammarParser#select1.
    def exitSelect1(self, ctx:GrammarParser.Select1Context):
        pass


    # Enter a parse tree produced by GrammarParser#set_list.
    def enterSet_list(self, ctx:GrammarParser.Set_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#set_list.
    def exitSet_list(self, ctx:GrammarParser.Set_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#pair.
    def enterPair(self, ctx:GrammarParser.PairContext):
        
        function = str(ctx.function().getText())

        output = open("output.txt","w")

        #priv = Diff_priv(path = data_path, columns_name = var_names)

        priv = Diff_priv(path="base_rc.csv", columns_name=["respiration"], epsilon = list(arange(0.005 , 0.105 , 0.005)))

        print("function: "+function+"\n")

        if function == 'AVG':
            output.write("Average >> "+str(priv.apply_privacy_avg()))


        elif function == 'MEDIAN':
            output.write("Median >> "+str(priv.apply_privacy_median()))

        elif function == 'NO':
            data = pd.read_csv("base_rc.csv")[:5000]
            original =  np.mean(data["respiration"])
            output.write("Original Average >> "+str(original))

        else :
            print("Invalid function")

        output.close()

    # Exit a parse tree produced by GrammarParser#pair.
    def exitPair(self, ctx:GrammarParser.PairContext):
        pass


    # Enter a parse tree produced by GrammarParser#function.
    def enterFunction(self, ctx:GrammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by GrammarParser#function.
    def exitFunction(self, ctx:GrammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by GrammarParser#from_list.
    def enterFrom_list(self, ctx:GrammarParser.From_listContext):
        pass

    # Exit a parse tree produced by GrammarParser#from_list.
    def exitFrom_list(self, ctx:GrammarParser.From_listContext):
        pass


    # Enter a parse tree produced by GrammarParser#condition.
    def enterCondition(self, ctx:GrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by GrammarParser#condition.
    def exitCondition(self, ctx:GrammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by GrammarParser#column.
    def enterColumn(self, ctx:GrammarParser.ColumnContext):
        pass

    # Exit a parse tree produced by GrammarParser#column.
    def exitColumn(self, ctx:GrammarParser.ColumnContext):
        pass


    # Enter a parse tree produced by GrammarParser#value.
    def enterValue(self, ctx:GrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by GrammarParser#value.
    def exitValue(self, ctx:GrammarParser.ValueContext):
        pass


    # Enter a parse tree produced by GrammarParser#table_name.
    def enterTable_name(self, ctx:GrammarParser.Table_nameContext):
        pass

    # Exit a parse tree produced by GrammarParser#table_name.
    def exitTable_name(self, ctx:GrammarParser.Table_nameContext):
        pass


    # Enter a parse tree produced by GrammarParser#attribute.
    def enterAttribute(self, ctx:GrammarParser.AttributeContext):
        pass

    # Exit a parse tree produced by GrammarParser#attribute.
    def exitAttribute(self, ctx:GrammarParser.AttributeContext):
        pass


    # Enter a parse tree produced by GrammarParser#relation.
    def enterRelation(self, ctx:GrammarParser.RelationContext):
        pass

    # Exit a parse tree produced by GrammarParser#relation.
    def exitRelation(self, ctx:GrammarParser.RelationContext):
        pass



del GrammarParser