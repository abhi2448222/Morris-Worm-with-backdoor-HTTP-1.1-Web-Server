#!/usr/bin/env python
import re
import traceback
import os
hostnamesoutput_usrknownhosts=[]
from pwdfileextracting import list_users

for user in list_users:
	try:
		if (os.access("%s/.ssh/known_hosts"%user, os.F_OK)):
			if(os.access("%s/.ssh/known_hosts"%user, os.R_OK)) :
				with open('%s/.ssh/known_hosts'%user) as fp:
				#with open("/home/abhishek/Downloads/known_hosts") as fp:
					for line in fp:

						if "@" in line[0]:
							linearr=line.split()
							hostnames=linearr[1].split(",")
							match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
							for out in hostnames:
								result=re.search(match,out)
								if not result:
									#print out
									hostnamesoutput_usrknownhosts.append(out)
						elif "|" in line[0] or "#" in line[0]:
							continue	
			
				
						else:
				
							linearr=line.split()
							if "[" in linearr[0] :
								ind=linearr[0].index("]")
								linearry=linearr[0]
								linearry=linearry[1:ind]
								linearr[0]=linearry
					
							hostnames=linearr[0].split(",")
				#REGEX to remove IP--start
							match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
							for out in hostnames:
				#for i in range(0,len(hostnames)):	
				#	
								result=re.search(match,out)
				
					
								if not result :
									#print out 
									hostnamesoutput_usrknownhosts.append(out)
				#Regex to remove IP --end
	
	except Exception, e:
		pass
		#print 'Not able to read the file'	
		#print traceback.print_exc()
