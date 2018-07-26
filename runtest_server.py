# coding:utf8

import grpcpy
from proto import hello_pb2_grpc, hello_pb2

server = "127.0.0.1:50051"

class Demo(hello_pb2_grpc.DemoServicer):
    def PrintHello(self, request, context):
        return hello_pb2.HelloReply(message="Hello, %s" % request.name)

if __name__ == "__main__":
    server = grpcpy.get_server(server, ssl=False)
    hello_pb2_grpc.add_DemoServicer_to_server(Demo(), server)
    grpcpy.start()