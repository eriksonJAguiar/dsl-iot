from flask import Flask, request
from flask_restful import Resource, Api
import json

from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarListener import GrammarListener
from GrammarParser import GrammarParser
import sys
import gettext


app = Flask(__name__)
api = Api(app)


@app.route('/api/query')
def query():
    lexer = GrammarLexer(InputStream(str(request.args.get("query"))))
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.start()
    #printer = GrammarPrintListener()
    printer = GrammarListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    output = open("output.txt", "r")
    stringona = output.read()
    return json.dumps(stringona)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=50051, debug=True)
