from concurrent import futures
import time

import grpc

import primefactor_pb2
import primefactor_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Factors(primefactor_pb2_grpc.FactorsServicer):

    def PrimeFactors(self, request, context):
        return primefactor_pb2.Response(result=6)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    primefactor_pb2_grpc.add_FactorsServicer_to_server(Factors(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()