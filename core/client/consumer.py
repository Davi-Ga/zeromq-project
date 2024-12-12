import zmq
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Gerencia os recursos e configurações para as sockets que serão criadas dentro dele.
context = zmq.Context()

#Cria um socket usando o Objeto context e é do Tipo "request"
socket = context.socket(zmq.REQ)
#Faz uma conexão com o servidor usando protocolo TCP(Confiabilidade)
socket.connect("tcp://localhost:5555")
logging.info("Cliente conectado e pronto para enviar requisições...")

try:
    for request in range(10):
        logging.info(f"Enviando requisição {request} …")
        
        numero = random.randint(1, 1000)
        
        #Transforma o número em bytes, com o MSB no ínicio com um número máximo de 100 bytes
        #Comunicação baixo nível necessita de envio de dados binários
        socket.send(numero.to_bytes(100, byteorder='big'))

        #Escuta o socket
        message = socket.recv()
        
        logging.info(f"Para: {numero} Fibonacci: {int.from_bytes(message, byteorder='big')}")
        
except zmq.ZMQError as e:
    logging.error(f"ZMQ Error: {e}")
    
except Exception as e:
    logging.error(f"General Error: {e}")
    
finally:
    #Finaliza a conexão socket
    socket.close()
    #Libera todos os recursos associados ao contexto
    context.term()
