import socket
import threading


class Server:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Serveur démarré sur {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Nouvelle connexion : {client_address}")

            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    self.clients.remove(client)

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    print(f"Message reçu : {message.decode('utf-8')}")
                    self.broadcast(message, client_socket)
                else:
                    self.clients.remove(client_socket)
                    client_socket.close()
                    break
            except:
                self.clients.remove(client_socket)
                client_socket.close()
                break
