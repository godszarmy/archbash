import socket
#server_main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host=socket.gethostbyname(socket.getfqdn())
#server_main_socket.bind((host,port))
#server_main_socket.close()

            #msg_recu = client.recv(1024)
            #msg_a_envoye = msg_recu.encode()
            #msg_recu = msg_recu.decode()
            #print("Client dit: {}".format(msg_recu))
            #client.send(b"preparing upload...")
            
#f = open('torecv.png','wb')
#f.write(x)
#x = client.recv(1024)
#===================================================================
import select
#server_main_socket_start =  True
#server_main_socket.listen(3)
#clients_list = []

    #connexions_demandees, wlist, xlist = select.select([clownServer], [], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)
        #print("Client conecté: {}".format(infos_connexion))
    #clients_a_lire = []
    #try:
        #clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
    #except select.error:
        #pass
    #else:
       # for client in clients_a_lire:
             #client.close
#=================================================================
import random
#port=random.randint(11999,13999)
import requests
#print(requests.get("http://ip.42.pl/new").text)
import time
#time.sleep(5)
import sys
# except:
#       print ("Unexpected error N: {}".format(if_loop)), sys.exc_info()[0]
        #raise

class server_luncher():        
        def __init__(self):
                global port
                print ("> port {} and host_ip {{}}".format(port).format(host))
                while end_loop==False:
                        if loop!=0:
                                try:
                                        #that
                                except errorType:
                                        #this
        def return_main_socket():
                return server_main_socket
        return_main_socket()
