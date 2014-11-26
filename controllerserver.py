import web 
reg=0
proc=0
insvalues= '''
{
  "ma-instruction": {
    "ma-instruction-tasks": [
      {
        "ma-task-name": "UDP Latency",
        "uri": "urn:ietf:ippm:measurement:UDPLatency-Poisson-XthPercentileMean",
        "ma-task-options": [
          {"name": "X", "value": "99"},
          {"name":"rate", "value": "5"},
          {"name":"duration", "value": "30.000"},
          {"name":"interface", "value": "broadband"},
          {"name":"destination-ip", "value": {"version":"ipv4", "ip-address":"192.168.2.54"}},
          {"name":"destination-port", "value": "50000"},
          {"name":"source-port", "value": "50000"}
        ],
        "ma-task-suppress-by-default": "TRUE"
      },
      {
        "ma-task-name": "Report",
        "uri": "urn:ietf:lmap:report:http_report",
        "ma-task-options": [
          {"name": "report-with-no-data", "value": "FALSE"}
        ],
        "ma-task-suppress-by-default": "FALSE"
      }
    ],
    "ma-report-channels": [
      {
        "ma-channel-name": "Collector A",
        "ma-channel-target": "http://www.example2.com/lmap/collector",
        "ma-channel-credientials": { } 
      }
    ],
    "ma-instruction-schedules": [
      {
        "ma-schedule-name": "4 times daily test UDP latency and report",
        "ma-schedule-tasks": [
          {
            "ma-schedule-task-name": "UDP Latency",
            "ma-schedule-task-datasets": [
              {
                "ma-schedule-task-output-task-names": "Report"
              }
            ]
          },
          {
            "ma-schedule-task-name": "Report",
            "ma-schedule-task-datasets": [
              {
                "ma-schedule-task-channel-names": "Collector A"
              }
            ]
          }
        ],
        "ma-schedule-timing": {
          "ma-timing-name": "once every 6 hours",
          "ma-timing-calendar": {
            "ma-calendar-hours": ["00", "06", "12", "18"],
            "ma-calendar-minutes": ["00"],
            "ma-calendar-seconds": ["00"]
          },
          "ma-timing-random-spread": "21600000"
        }
      }
    ]
  }
} '''
confvalues='''
{
  "ma-config": {
    "ma-agent-id": "550e8400-e29b-41d4-a716-446655440000",
    "ma-control-tasks": [
      {
        "ma-task-name": "Controller configuration",
        "uri": "urn:ietf:lmap:control:http_controller_configuration"
      },
      {
        "ma-task-name": "Controller status and capabilities",
        "uri": "urn:ietf:lmap:control:http_controller_status_and_capabilities"
      },
      {
        "ma-task-name": "Controller instruction",
        "uri": "urn:ietf:lmap:control:http_controller_instruction"
      }
    ],
    "ma-control-channels": [
      {
        "ma-channel-name": "Controller instruction",
        "ma-channel-target": "http://www.example.com/lmap/controller",
        "ma-channel-credientials": { } 
      }
    ],
    "ma-control-schedules": [
      {
        "ma-schedule-name": "Controller schedule",
        "ma-schedule-tasks": [
          {
            "ma-schedule-task-name": "Controller configuration",
            "ma-schedule-task-datasets": [
              {
                "ma-schedule-task-channel-names": ["Controller channel"]
              }
            ]
          }
        ]
      },
      {
            "ma-schedule-task-name": "Controller status and capabilities",
            "ma-schedule-task-datasets": [
              {
                "ma-schedule-task-channel-names": ["Controller channel"]
              }
            ]
          },
        {
            "ma-schedule-task-name": "Controller instruction",
            "ma-schedule-task-datasets": [
              {
                "ma-schedule-task-channel-names": ["Controller channel"]
              }
            ]
          },	
       {
        "ma-schedule-timing": [ 
         {
          "ma-timing-name": "hourly randomly",
          "ma-timing-calendar": {
            "ma-calendar-minutes": ["00"],
            "ma-calendar-seconds": ["00"]
          },
          "ma-timing-random-spread": "3600000"
         }
        ]
      }
    ],
    "ma-credentials": { } 
}
}
'''
suppression='''
{
     "ma-instruction": {
       "ma-suppression": {
          "ma-suppression-enabled": "TRUE"
       }
     }
}
'''
urls= (
 "/ma/config", "config",
 "/ma/ins", "ins",
 "/ma/cap", "cap"
 )
class cap:
    def POST(self):
        global reg
        web.header('Content-Type', 'application/json')
	data=web.data()
        print data ; 
	if reg==0 :
          reg=reg+1; 
          raise web.redirect('/ma/config')
class ins:
   def GET(self):
         global proc; global reg
         web.header('Content-Type', 'application/json')
         print proc
	 if (proc%5)==0 :
           proc=proc+1 ; return insvalues
         elif (proc%5)==4 :
	   proc=proc+1; reg=0
	   return suppression
         else :
           proc=proc+1; return 
class config:
    def GET(self):
       web.header('Content-Type', 'application/json')
       return confvalues
       

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

