# coding:utf8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grpcpy",
    version="0.0.1",
    author="Chris Ho",
    author_email="cenne1986@qq.com",
    description="easy to use tls for grpc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisho/grpcpy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
    ),
)