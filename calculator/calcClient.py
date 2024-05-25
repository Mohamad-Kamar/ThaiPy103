import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        add_response = stub.Add(calculator_pb2.AddRequest(number1=5, number2=3))
        print(f"5 + 3 = {add_response.result}")
        
        multiply_response = stub.Multiply(calculator_pb2.MultiplyRequest(number1=4, number2=6))
        print(f"4 * 6 = {multiply_response.result}")

if __name__ == '__main__':
    run()