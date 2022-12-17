import socket

#msg format in form of 'Add these numbers: 8 54'
def response_parse(msg):
  splice = reply.find(" ")
  #cut operator
  op = reply[:splice]
  #parse rest of message to seperate number part
  rem = reply[splice:]
  splice = rem.find("\n")
  rem = rem[:splice]
  splice = rem.find(":")
  rem = rem[splice:]
  splice = rem.find(" ")
  rem = rem[splice:]
  splice = rem.find(" ")
  rem = rem[splice:]
  rem_s = rem.strip()
  splice = rem_s.find(" ")
  #get numbers and convert str to int
  n1 = rem_s[:splice]
  n2 = rem_s[splice:].strip()
  return (op,int(n1),int(n2))

def math(sign,n1,n2):
  if sign == "Subtract":
    total = n1 - n2
    ans = str(total) + "\n"
  if sign == "Add":
    total = n1 + n2
    ans = str(total) + "\n"
  return ans

#create connection
s = socket.socket()
s.connect(("ad.samsclass.info", 10204))
#iterate through questions
for i in range(5):
  reply = s.recv(1024).decode()
  print(reply)
  #parse numbers
  nums = response_parse(reply)
  #calculate answer
  msg = math(nums[0],nums[1],nums[2])
  #send to server
  s.send(str(msg).encode())
  print(s.recv(1024).decode())
print(s.recv(1024).decode())
#close socket
s.close()




