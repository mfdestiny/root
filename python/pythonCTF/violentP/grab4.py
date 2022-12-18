import socket
import re

#parse server response for forwarding port information
def msg_parse(msg):
   entries = re.findall(r"\d+",msg)
   return int(entries[1])

   
def s_connection(add,port):
   try:
      s = socket.socket()
      s.settimeout(2)
      s.connect((add, port))
      msg = s.recv(1024).decode()
      s.close()
      return msg
   except socket.error as err:
      print(err)

#inital target
add = 'target1.bowneconsulting.com'
port = 22010

resp = s_connection(add,port)
new_port = msg_parse(resp)
flag = s_connection(add,new_port)
print(flag)