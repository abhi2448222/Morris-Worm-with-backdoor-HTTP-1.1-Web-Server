#!/usr/bin/env python
from etcfileopening import hostnamesoutput_etc
from userknownhosts import hostnamesoutput_usrknownhosts
from knownhosts import hostnamesoutput_knownhosts
from authorizedkeys import hostnamesoutput_authokeys
from configfileopening import hostnamesoutput_config
from usersconfigfile import hostnamesoutput_usrconfig

for hostnames in hostnamesoutput_etc:
	print hostnames
for hostnames in hostnamesoutput_usrknownhosts:
	print hostnames
for hostnames in hostnamesoutput_knownhosts:
	print hostnames
for hostnames in hostnamesoutput_authokeys:
	print hostnames
for hostnames in hostnamesoutput_config:
	print hostnames
for hostnames in hostnamesoutput_usrconfig:
	print hostnames

#print hostnamesoutput_etc
#print hostnamesoutput_usrknownhosts
#print hostnamesoutput_knownhosts
#print hostnamesoutput_authokeys
#print hostnamesoutput_config
#print hostnamesoutput_usrconfig

