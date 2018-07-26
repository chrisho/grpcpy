# coding:utf8

import grpcpy

from proto import hello_pb2
from proto import hello_pb2_grpc


if __name__ == "__main__":
    channel = grpcpy.get_client_channel_local(ssl=False)
    stub = hello_pb2_grpc.DemoStub(channel)
    response = stub.PrintHello(hello_pb2.HelloRequest(name='u'))

    print(response.message)