import time
import zmq
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
#Gerencia os recursos e configurações para as sockets que serão criadas dentro dele.
context = zmq.Context()

#Cria um socket usando o Objeto context e é do Tipo "response"
socket = context.socket(zmq.REP)

#Associa qualquer endereço local ao socket na porta 5555 usando TPC(Confiabilidade)
socket.bind("tcp://*:5555")
logging.info("Servidor iniciado e aguardando conexões...")


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


while True:
    try:
        #Escuta o socket
        message = socket.recv()
        logging.info(
            f"Requisição recebida: {str(int.from_bytes(message, byteorder='big'))}"
        )

        time.sleep(1)
        #Decodifica o valor recebido em um inteiro
        resposta = fibonacci(int.from_bytes(message, byteorder="big"))

        #Transforma o número em bytes, com o MSB no ínicio com um número máximo de 100 bytes
        #Comunicação baixo nível necessita de envio de dados binários
        socket.send(resposta.to_bytes(100, byteorder="big"))
    except Exception as e:
        logging.error(f"Erro ao processar a requisição: {e}")
        message = "Houve um erro na requisição"
        #Codificação de string em bytes
        socket.send(message.encode('utf-8'))