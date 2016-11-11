#!/usr/bin/env python
import sys
import re
import os
import traceback
hostnamesoutput_config=[]
if (os.access("/etc/ssh/ssh_config", os.F_OK)):
	if(os.access("/etc/ssh/ssh_config", os.R_OK)) :
		try:
			with open('/etc/ssh/ssh_config') as fp:
			#with open('/home/abhishek/.ssh/config') as fp:
			#with open('/home/abhishek/Downloads/files/ssh_config') as fp:
				for line in fp:
					if "#" in line[0]:
						continue
					elif "=" in line:
						line=line.strip()
						ind=line.index("=")
						line=line[ind+1:]
						match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
						result=re.search(match,line)
						if not result:
							#print line
							hostnamesoutput_config.append(line)
						
					elif "HostName" in line or "hostname" in line or "HOSTNAME" in line:    
        #print line # a complete line including hostname
						 
						line=line.strip()
						if line[:8]=="HostName" or line[:8]=="hostname" or line[:8]=="HOSTNAME" :
							out=line.split() 
							
							#out=trim[8:]
						
							for i in range(1,len(out)):
								match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
								result=re.search(match,out[i])
								if not result:
									#print out[i]
									hostnamesoutput_config.append(out[i])
							   #Printing only output 
							
					elif "Host" in line or "host" in line or "HOST" in line:
						
						line=line.strip()
						
						if line[:4]=="Host" or line[:4]=="host" or line[:4]=="HOST" :
							out=line.split()
							#out=trim[4:]
							for i in range(1,len(out)):
								match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
								result=re.search(match,out[i])
								if not result:
									#print out[i]
									hostnamesoutput_config.append(out[i])
							
					else:
						continue
					
		except Exception, e:
			pass
			#print 'Not able to read the file'	
			#print traceback.print_exc()	 
	 
	 
