import grpc

#from diff_piv import Diff_priv

# import the generated classes
import test_pb2
import test_pb2_grpc

import matplotlib.pyplot as plt
from numpy import arange

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = test_pb2_grpc.SenderStub(channel)

#entry = input("Insert your query:\n")

entry = "SELECT NO(age) FROM table1 WHERE year = 2005"

aux = entry.split()[1]
aux2 = aux.split("(")[0]

# create a valid request message
#SELECT AVG(age) FROM table1 WHERE year = 2020
#
query = test_pb2.Text(value = str(entry))

# make the call
response = stub.Input(query)

# et voilà

if response.value == "error" :
	print("Wrong input, please try again")
else :
	print(response.value)

arqv = open("output.txt", "w")
arqv.write("error")
arqv.close()
