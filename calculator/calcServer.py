from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        response = calculator_pb2.AddResponse()
        response.result = request.number1 + request.number2
        return response

    def Multiply(self, request, context):
        response = calculator_pb2.MultiplyResponse()
        response.result = request.number1 * request.number2
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()