#!/usr/bin/env python
import socket
import sys
import os
import subprocess
import traceback
import urllib
import sys
import signal
import time

global conn
global sock

def signal_handler(signum, frame):
	#print 'sigint called'
	sock.close()
	conn.close()
	sys.exit(0)
	
signal.signal(signal.SIGINT, signal_handler)
	
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print sock
#print 'sock done'
try:
	port=int(sys.argv[1])
	sock.bind(('',port))
	
except socket.error,mess:
	#print 'binding failed'+ str(mess[0]) + str(mess[1])
	sys.exit(0)
#print 'sock bind complete'
	

sock.listen(5)
#print 'sock listening'
while 1:
	
	
	try:
		#signal.signal(signal.SIGINT, signal_handler)
		conn , addr = sock.accept()
		#print 'connected -' + addr[0] + str(addr[1])
		#conn.send("welcome to Python")
		
		data=conn.recv(500000)
		data=urllib.unquote(data)
		
			
			
		print 'data', data	
		allines=data.splitlines()

		firstline=allines[0]
		#print "firstline------",firstline
		splitdata=firstline.split()
		#print splitdata
		length=len(splitdata)
		if splitdata[0]=="GET" and "/exec" in splitdata[1] and splitdata[length - 1]=="HTTP/1.1":
			
			command = ' '.join(splitdata[1:-1])
			#command=splitdata[1]
			command=command[6:]
			#print "command====" , command
			
			try:
				result = subprocess.check_output(command, shell=True)
				#print 'Result-------' , result
				reslen=len(result)
				#print reslen
				content_header="HTTP/1.1 200 OK"

				content_length="Content-Length: " + str(reslen)
				
				resend= content_header + '\n' + content_length + '\n' + '\n' + result
				#print 'resend--------',resend
				
			except Exception , e :
				#print 'in exception bloack'
				content_header="HTTP/1.1 200 OK "
				content_length="Content-Length: " + "0"
				resend=content_header + '\n' + content_length + '\n' + '\n' + ""
				#print 'resend--------',resend
			
			print 'resend------'
			print resend	
			conn.send(resend)
			
		else:
			content_header="HTTP/1.1 404 Not found "
			content_length="Content-Length: " + "9"
			resend=content_header + '\n' + content_length + '\n' + '\n' + "NOT FOUND "
			conn.send(resend)
			print 'resend--------'
			print resend
		#break

		#break
	#conn.close()
	except Exception, e:
	
	#print "Exception occured"
		#content_header="HTTP/1.1 404 Not found "
		#content_length="Content-Length: " + "9"
		#resend=content_header + '\n' + content_length + '\n' + '\n' + "Not Found"
		#conn.send(resend)
		pass
	#print 'resend--------',resend
	#print traceback.print_exec()
	#sock.close()
	#conn.close()
	#sys.exit(0)
		
#sock.close()

	
	

	


