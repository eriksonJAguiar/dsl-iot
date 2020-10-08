from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarListener import GrammarListener
from GrammarParser import GrammarParser
import sys
import gettext

# SELECT AVG(age) FROM table WHERE year = 1995
# SELECT HISTOGRAM(age) FROM table WHERE year = 1995

def main():
    lexer = GrammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.start()
    #printer = GrammarPrintListener()
    printer = GrammarListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
