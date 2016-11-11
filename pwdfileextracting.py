#!/usr/bin/env python
import os
list_users=[]
if (os.access("/etc/passwd", os.F_OK)):
	
	if(os.access("/etc/passwd", os.R_OK)) :
		try:
			with open('/etc/passwd') as fp:
				for line in fp:
    #if "/bin/bash" in line:	  
      #print line
      #if "home" in line:
					arr=line.split(':')
					list_users.append(arr[5])
			#print list_users

		except Exception, e:
			pass
			#print 'Not able to read the file'
