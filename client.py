class Client:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connecté au serveur {self.host}:{self.port}")

        threading.Thread(target=self.receive_messages).start()

        while True:
            message = input("Vous : ")
            if message.lower() == "quit":
                self.client_socket.close()
                break
            self.client_socket.send(message.encode("utf-8"))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message:
                    print(f"\n{message}")
                else:
                    break
            except:
                print("Déconnecté du serveur.")
                self.client_socket.close()
                break

if __name__ == "__main__":
    choice = input("Démarrer le serveur ou le client ? (serveur/client) : ").strip().lower()

    if choice == "serveur":
        server = Server()
        server.start()
    elif choice == "client":
        client = Client()
        client.start()
    else:
        print("Choix invalide. Veuillez relancer le programme.")