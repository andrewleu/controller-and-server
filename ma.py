import web 
from time import sleep
stat_and_cap='''
{
  "ma-status-and-capabilities": {
    "ma-agent-id": "550e8400-e29b-41d4-a716-446655440000",
    "ma-device-id": "urn:dev:mac:0024befffe804ff1",
    "ma-hardware": "mfr-home-gateway-v10",
    "ma-firmware": "25637748-rev2a",
    "ma-version": "ispa-v1.01",
    "ma-interfaces": [
      {
        "ma-interface-name": "broadband",
        "ma-interface-type": "PPPoE"
      }
    ],
    "ma-last-measurement": "",
    "ma-last-report": "",
    "ma-last-instruction": "",
    "ma-last-configuration": "2014-06-08T22:47:31+00:00",
    "ma-supported-tasks": [
       {
           "ma-task-name": "Controller configuration",
           "ma-task-registry": "urn:ietf:lmap:control:http_controller_configuration"
       },      
       {
           "ma-task-name": "Controller status and capabilities",
           "ma-task-registry": "urn:ietf:lmap:control:http_controller_status_and_capabilities"
       },
       {
          "ma-task-name": "Controller instruction",
          "ma-task-registry": "urn:ietf:lmap:control:http_controller_instruction"
       },
       {
          "ma-task-name": "Report",
          "ma-task-registry": "urn:ietf:lmap:report:http_report"
       },
       {
           "ma-task-name": "UDP Latency",
           "ma-task-registry": "urn:ietf:ippm:measurement:UDPLatency-Poisson-XthPercentileMean"
       }
   ]
  }
}
'''
urls= (
 "/ma/config", "config",
 "/ma/ins", "ins",
 "/ma/cap", "cap"
 )
 
class cap:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return stat_and_cap
class ins:
     def POST(self):
	  	 data=web.data()
                 web.header('Content-Type', 'application/json')
	  	 print data 
class config:
    def PUT(self):
       web.header('Content-Type', 'application/json')
       data=web.data()
       print data
def my_loadhook():
    print "my load hook"

def my_unloadhook():
    print "my unload hook"; sleep(10)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.add_processor(web.loadhook(my_loadhook))
    app.add_processor(web.unloadhook(my_unloadhook))
    app.run()
	  	
