import grpc
import math_pb2_grpc
import math_pb2

def run():
    channel = grpc.insecure_channel("127.0.0.1:50051")
    stub = math_pb2_grpc.evaluatorStub(channel)
    response = stub.evaluate(math_pb2.strRequest(expression="100 * 100_000"))
    print(response.number)

if __name__ == "__main__":
    run()