#!/usr/bin/env python
import re
import traceback
import os
hostnamesoutput_authokeys=[]
from pwdfileextracting import list_users
for user in list_users:
	try:
		hostnamelist=[]
		if (os.access("%s/.ssh/authorized_keys"%user, os.F_OK)):
			
			if(os.access("%s/.ssh/authorized_keys"%user, os.R_OK)):
				
				with open('%s/.ssh/authorized_keys'%user) as fp:
				#with open('exampleauthorizedkeys.txt') as fp:
					
					for line in fp:
						if  "#" in line[0]:
							continue
						elif "permitopen" in line:
							linearr=line.split()
							hostnames=linearr[0].split(",")
							for extract in hostnames:
								extract=extract[12:]
								if ":" in extract:
									extract=extract.split(":")
									match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
							
									result=re.search(match,extract[0])
							
									if not result :
										if not extract[0].startswith('!'):
											#print extract[0]
											hostnamesoutput_authokeys.append(extract[0])
								else :
									extract=extract[:-1]
									match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
									result=re.search(match,extract[0])
									if not result :
										if not extract.startswith('!'):
											#print extract
											hostnamesoutput_authokeys.append(extract)
								
							if "ssh-rsa" in line:
								ind=line.index("@")
								line=line[ind+1:]
								line=line[:-1]
								if line not in hostnamelist :
									match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
									result=re.search(match,line)
									if not result :
										if not line.startswith('!'):
											hostnamelist.append(line)
							
							
						elif "from" in line :
							linearr=line.split()
							extract=linearr[0]
							extract=extract[6:-1]
							extractnames=extract.split(",")
							match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
							for out in extractnames:
								result=re.search(match,out)
								if not result :
									if not out.startswith('!'):
										#print out
										hostnamesoutput_authokeys.append(out)
							if "ssh-rsa" in line:
								ind=line.index("@")
								line=line[ind+1:]
								line=line[:-1]
								if line not in hostnamelist :
									match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
									result=re.search(match,line)
									if not result :
										if not line.startswith('!'):
											hostnamelist.append(line)
							
					
						elif "ssh-rsa" in line:
							ind=line.index("@")
							line=line[ind+1:]
							line=line[:-1]
							if line not in hostnamelist :
								match = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
								result=re.search(match,line)
								if not result :
									if not line.startswith('!'):
										hostnamelist.append(line)
						
						
				
						else :
					
							continue
					
			#print hostnamelist		
					for hostnames in hostnamelist:
						#print hostnames
						hostnamesoutput_authokeys.append(hostnames)
					
	except Exception, e:
		pass
		#print 'Not able to read the file'	
		#print traceback.print_exec()			
					
						
						
					
    
