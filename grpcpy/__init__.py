# coding:utf8
from concurrent import futures
import grpc
import time

__ONE_DAY_IN_SECONDS = 60 * 60 * 24

__server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


def get_server(host="[::]:50051", cert_file="", key_file="", ssl=True):

    if ssl == True:
        __server.add_secure_port(host, __server_with_ssl(cert_file, key_file))
    else:
        __server.add_insecure_port(host)
    print("ready to listen " + host)

    return __server


def start():
    __server.start()
    try:
        while True:
            print("start to listen")
            time.sleep(__ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        __server.stop(0)


def get_client_channel(host, root_file="", server_name=""):
    host = __convert_underline_to_whippletree(host)  # k8s不支持下划线，需要转成横杠

    root_certificates = __read_file(root_file)

    credentials = grpc.ssl_channel_credentials(root_certificates=root_certificates)
    channel = grpc.secure_channel(
        host,
        credentials,
        options=[('grpc.ssl_target_name_override', server_name)],
    )
    return channel


def get_client_channel_local(root_file="", port="50051", server_name=""):
    host = "127.0.0.1:"+port
    channel = get_client_channel(host=host, root_file=root_file, server_name=server_name)
    return channel


def __server_with_ssl(cert_file, key_file):

    private_key = __read_file(key_file)
    certificate_chain = __read_file(cert_file)

    server_credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)])

    return server_credentials


def __read_file(file):
    with open(file) as f:
        c = f.read().encode()
    return c

def __convert_underline_to_whippletree(str):
    return str.replace('_', '-')