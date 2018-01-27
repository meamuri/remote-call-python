template for client-server rpc deploy and communication:

see [here](https://github.com/ridha/grpc-streaming-demo) for stream communication python/golang.

## interface declaration:
see [./protobuf/primefactor.proto](protobuf/primefactor.proto) file
configure them in according with official docs

## pre requirements
```
pip3 install -U grpcio grpcio-tools
```
on both machines (client and server too)

## initialize protobuf files:
```
python3 -m grpc_tools.protoc -I protobuf/ --python_out=. --grpc_python_out=. protobuf/primefactor.proto
```

## launch
```
python3 server.py
python3 client.py
```