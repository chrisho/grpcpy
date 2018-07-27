# coding:utf8
import grpcpy

from proto import hello_pb2
from proto import hello_pb2_grpc
import os

if __name__ == "__main__":
    # cert_file = os.getcwd() + "/server.pem"
    # key_file = os.getcwd() + "/server-key.pem"
    # ca_file = os.getcwd() + "/ca.pem"

    # channel = grpcpy.get_client_channel(host, cert_file=cert_file, key_file=key_file, root_file=ca_file)
    channel = grpcpy.get_client_channel_local(ssl=False)
    stub = hello_pb2_grpc.DemoStub(channel)
    response = stub.PrintHello(hello_pb2.HelloRequest(name='u'))

    print(response.message)