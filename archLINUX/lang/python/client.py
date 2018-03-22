import socket

hote = "localhost"
port = 12800
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
trigger_upload  = "upload"
trigger_done     = b"" #<<-------------------
trigger_continue=b""
safexit = 2

while msg_a_envoyer != b"fin":
    safexit=2
    msg_a_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
#________________________________________________________________
    #print (msg_a_envoyer)
    if msg_a_envoyer == trigger_upload:
               msg_a_envoyer = msg_a_envoyer.encode()
               # On envoie le message
               connexion_avec_serveur.send(msg_a_envoyer)
               msg_recu = connexion_avec_serveur.recv(1024)
               print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
               f = open('/home/bashel/Desktop/clowngum/GAME/tosend.png','rb')
               print ('Sending...')
               l = f.read(1024)
               while (l):
                  print ('uploading...')
                  connexion_avec_serveur.send(l)
                  trigger_continue = input("say c> ") #<-----
                  trigger_continue= trigger_continue.encode()
                  connexion_avec_serveur.send(trigger_continue) #-------
                  l = f.read(1024)
                  connexion_avec_serveur.send(l)
                  trigger_continue = input("say c> ") #<-----
                  trigger_continue= trigger_continue.encode()
                  connexion_avec_serveur.send(trigger_continue) #-------
                  l = f.read(1024)
               print ("Done Sending")
               f.close()
               safexit = 0
               trigger_done = input("say done> ")
               trigger_done= trigger_done.encode()
               connexion_avec_serveur.send(trigger_done)
               trigger_done = input("say done> ")
               trigger_done= trigger_done.encode()
               connexion_avec_serveur.send(trigger_done)
               #connexion_avec_serveur.shutdown(socket.SHUT_WR)
               #print  (connexion_avec_serveur.recv(1024))
#==============================================================
    if safexit==2:
      msg_a_envoyer = msg_a_envoyer.encode()
      # On envoie le message
      connexion_avec_serveur.send(msg_a_envoyer)
      msg_recu = connexion_avec_serveur.recv(1024)
      print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
    if safexit==0:
      msg_recu = connexion_avec_serveur.recv(1024)
      print(msg_recu.decode())
      safexit==2
#==============================================================
print("Fermeture de la connexion")
connexion_avec_serveur.close()
