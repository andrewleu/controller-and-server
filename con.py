import urllib
import urllib2
url = 'http://172.24.20.185:8080/ma/cap'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
raw_input('Anykey to continue')

