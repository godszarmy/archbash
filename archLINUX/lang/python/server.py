import socket
import select

hote = ''
port = 12800

clownServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clownServer.bind((hote, port))
clownServer.listen(3)
print("server is running successfully on port {}".format(port))
clownStart = True

clients_connectes = []

while clownStart:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la clownServer en lecture
    # On attend maximum 50ms
    connexions_demandees, wlist, xlist = select.select([clownServer],
        [], [], 0.05)
    
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        print("Client conecté: {}".format(infos_connexion))
        clients_connectes.append(connexion_avec_client)
    
    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            # on reçoi le message "hello world"
            msg_recu = client.recv(1024)
            msg_recu = msg_recu.decode()
            print("Client dit: {}".format(msg_recu))
#==========================================================================
            if msg_recu =="upload":
               client.send(b"preparing upload...")
               f = open('torecv.png','wb')
               print ("Receiving...")
               l = client.recv(1024)
               msg_rec = client.recv(1024)
               msg_rec = msg_rec.decode()
               print("Client dit: {}".format(msg_rec))
               while (msg_rec!="done"):
               	  print ("uploading...")
                  f.write(l)
               	  l = client.recv(1024)
                  msg_rec = client.recv(1024)
                  msg_rec = msg_rec.decode()
                  print("Client dit: {}".format(msg_rec))
               f.close()
               print ("Done Receiving")
#==========================================================================
            client.send(b"5/5")
            if msg_recu == "fin":
               clownStart = False		
print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

clownServer.close()
