import math_pb2
import math_pb2_grpc
import grpc
from concurrent import futures

class Evaluator(math_pb2_grpc.evaluatorServicer):
    def evaluate(self, request, context):
        res = eval(request.expression)
        return math_pb2.doubleResponse(number=res)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_pb2_grpc.add_evaluatorServicer_to_server(Evaluator(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()