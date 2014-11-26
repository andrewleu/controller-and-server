import web
import json
import time
import urllib, urllib2
import ping
import paravalues
from datetime import datetime
test_on=0
suppress=0
stat_and_cap=paravalues.stat_and_cap
urls= (
 "/ma/config", "config",
 "/ma/ins", "ins",
 "/ma/cap", "cap",
 "/ma/rep", "rep"
 )
class rep:
   def POST(self) :
     data=web.data()
     web.header('Content-Type', 'application/json')
     print data
class cap:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return stat_and_cap
class ins:
     global test_on
     global suppress 
     
     def POST(self):
          data=web.data()
          web.header('Content-Type', 'application/json')
          print data
          data=json.loads(data); #print data[u'ma-instruction'].keys()
          try:
                 keys= data[u'ma-instruction'].keys();
          	 if u'ma-instruction-tasks' in keys:
          	    self.process_task(data)
          	 elif u'ma-suppression' in keys :
                   if  data[u'ma-instruction'][u'ma-suppression'][u'ma-suppression-enabled']:
                     print 'Suppression';self.suppression()
          except Exception, e :
         	  print e
     def process_task(self,data):
        global test_on, suppress
        
        if test_on :
          return
        else :
          if suppress==1:
            suppress=0
          test_on=1
        
        #print data[u'ma-instruction'][u'ma-instruction-tasks'][0]
        if data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-name'].lower()==u'ping' :
         i=0; parastring=''; 
         for  i in range(len(data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-options'])) :
           #print data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-options'][i];print parastring
           if data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-options'][i][u'name']!='destination-ip' :
             if i==0 :
               parastring=str(data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-options'][i][u'value'])
             else :
              parastring=parastring+','+str(data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-options'][i][u'value'])
           else :
              parastring=parastring+','+str(data[u'ma-instruction'][u'ma-instruction-tasks'][0][u'ma-task-options'][i][u'value'][u'ip-address'])
         parastring=parastring.split(',');#print parastring
         while suppress==0 :
          testresult=list(ping.verbose_ping(parastring[2]));
          report=paravalues.rep
          report[u'ma-report'][u'ma-report-date']=str(datetime.now())
          report[u'ma-report'][u'ma-report-tasks'][0][u'ma-report-task-config']=data[u'ma-instruction'][u'ma-instruction-tasks'][0]
          rep_url=data[u'ma-instruction'][u'ma-report-channels'][0][u'ma-channel-target'];
          report[u'ma-report'][u'ma-report-tasks'][0][u'ma-report-task-rows']=testresult;
          report=json.dumps(report);
          #rep_url="http://172.24.20.185:8080/ma/rep"
          req=urllib2.Request(rep_url, report);
          response=urllib2.urlopen(req)
          thepage=response.read();
          time.sleep(20)
        suppression=0;
     def suppression(self):
        global test_on,suppress
        test_on=0;suppress=1;  
        
class config:
    def PUT(self):
       web.header('Content-Type', 'application/json')
       data=web.data()
       print data

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

