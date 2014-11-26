import socket
import urllib
import urllib2
import paravalues
timeout=5
socket.setdefaulttimeout(timeout)
url = 'http://172.24.20.185:8080/ma/ins'
values = paravalues.ins
print values;
try:
  req = urllib2.Request(url, values)
  response = urllib2.urlopen(req)
except Exception,e:
  pass
raw_input('Anykey to continue')
values= paravalues.sup
try:
  req = urllib2.Request(url, values)
  response = urllib2.urlopen(req)
except Exception,e :
  pass

