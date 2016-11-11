#!/usr/bin/env python
import sys
import re
import os
hostnamesoutput_etc=[]
#file = open('/etc/hosts')
#myfile=file.read()
#print myfile

#for line in myfile :
#	if line[0].isdigit() :
#		regex=re.compile("\s+[a-z|.]+\s+")
		#line=(re.search(regex,line)).group(0)
#		print((re.search(regex,line)).group(0))

#print line,
#with open('abhi.txt') as fp:
# for line in fp:
#  if line[0].isdigit():
#   regex=re.compile("\s+[a-zA-z|.|-]+\s+")
#   result=re.search(regex,line)
#   if result :
#    print result.group(0)
if (os.access("/etc/hosts", os.F_OK)):
	if(os.access("/etc/hosts", os.R_OK)) :
		
		try:
			with open('/etc/hosts') as fp:
				for line in fp:
					line=line.strip()
					
					if len(line)>0:
						linearr=line.split()
					else:
						continue
					if line[0]=="#":
						continue
							
					for i in range(1, len(linearr)):
						#print linearr[i]
						hostnamesoutput_etc.append(linearr[i])
						 
				
		except Exception, e:
			pass
			#print 'Not able to read the file'
		  

