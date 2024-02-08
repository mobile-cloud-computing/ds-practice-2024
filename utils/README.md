# Utils

This folder contains protocol specification files such as OpenAPI, gRPC, etc.

## OpenAPI

OpenAPI specification example files are located in the `api` folder. The specification is written in YAML format. You can use [Swagger Editor](https://editor.swagger.io/) to view or edit the specification. The specification is usually used to generate API client code and documentation for various languages. Check the practice session guide for more information on how to proceed.

## gRPC

gRPC protocol specification example files are located in the `pb` folder. The specification is written in Protocol Buffers format (`.proto`). Read more about it [here](https://grpc.io/docs/languages/python/quickstart/). 
To generate the grpc Python code from the `.proto` file, first you need to install the gRPC tools:

```bash
python -m pip install grpcio-tools
```

Then, you can generate the gRPC Python code using the following command:

```bash
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./yourprotofile.proto
```

It should generate 3 files: `yourprotofile_pb2.py`, `yourprotofile_pb2_grpc.py` and `yourprotofile_pb2.pyi`. The generated code will be located in the same folder as the `.proto` file. You can use the generated code to implement the gRPC server and client code. Check the example app code (f.e. the orchestrator app) and the practice session guide for more information.

Note: The generated code is not meant to be edited manually. If you need to make changes to the protocol, edit the `.proto` file and regenerate the code. The generated code will be overwritten. When importing the generated code from the current folder, the folder should contain an empty `__init__.py` file. Check the example app code (f.e. the orchestrator app) to see how to import the generated gRPC code.