import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("SERVER")

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

while True:
    message = socket.recv()
    print("Received request: %s" % str(int.from_bytes(message, byteorder='big')))

    time.sleep(1)
    resposta = fibonacci(int.from_bytes(message, byteorder='big'))
    
    socket.send(resposta.to_bytes(100, byteorder='big'))