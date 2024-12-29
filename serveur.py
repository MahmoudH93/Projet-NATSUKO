import socket 
import select 

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host, port = '127.0.0.1', 2025  
serveur.bind((host, port)) 
serveur.listen(4) 
client_connectee = True 
socket_objs = [serveur] 
print("bienvenue dans le chat!") 

while client_connectee:
    try:
        liste_lu, liste_acce_Ecrit, Exeption = select.select(socket_objs, [], socket_objs)
        
        for socket_obj in liste_lu:
            if socket_obj is serveur:
                client, adresse = serveur.accept()
                socket_objs.append(client)
                print(f"Nouvelle connexion de {adresse}")
            else:
                try:
                    donnée_reçu = socket_obj.recv(128).decode("utf-8")
                    if donnée_reçu:
                        print(donnée_reçu)
                    else:
                        raise ConnectionResetError
                except (ConnectionResetError, OSError):
                    socket_objs.remove(socket_obj)
                    socket_obj.close()
                    print("1 participant déconnecté")
                    print(f"{len(socket_objs) - 1} participants restants")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")


            






