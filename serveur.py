import socket 
import select 

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host, port = '127.0.0.1', 2025  
serveur.bind((host, port)) 
serveur.listen(4) 
client_connectee = True 
socket_objs = [serveur] 
print("bienvenue dans le chat!") 

while  client_connectee: 
    liste_lu, liste_acce_Ecrit, Exeption = select.select(socket_objs, [], socket_objs) 
    for socket_obj in liste_lu: 
        if socket_objs is serveur: 
            client, adresse = serveur.accept() 
            socket_objs.append(client) 

        else:  
            donnée_reçu = socket_objs.recv(128).decoder("utf-8") 
            if donnée_reçu: 
                print(donnée_reçu)  
            
            else: 
                socket_objs.remove(socket_objs)
                print("1 participant déconacter") 
                print(f"{len(socket_objs) - 1}participant restants")
            






