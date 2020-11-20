import grpc
from concurrent import futures
import time

# import the generated classes
import test_pb2
import test_pb2_grpc

# import the original calculator.py
import test

from diff_piv import Diff_priv

from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarListener import GrammarListener
from GrammarParser import GrammarParser
import sys
import gettext

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer

###########################################################################

class SenderServicer(test_pb2_grpc.SenderServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def Input(self, request, context):
        # response = test_pb2.Text()
        # response.value = test.output(request.value)
        # return response

        lexer = GrammarLexer(InputStream(str(request.value)))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.start()
        #printer = GrammarPrintListener()
        printer = GrammarListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

        output = open("output.txt", "r")
        
        string_out = test_pb2.Text()
        string_out.value = output.read()

        return string_out

###########################################################################

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
test_pb2_grpc.add_SenderServicer_to_server(
        SenderServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)