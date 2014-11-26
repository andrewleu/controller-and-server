import urllib
import urllib2
values='''
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
    ]
    "ma-control-channels": [
      {
        "ma-channel-name": "Controller instruction",
        "ma-channel-target": "http://www.example.com/lmap/controller",
        "ma-channel-credientials": { } // structure of certificate ommitted for brevity
      }
    ]
    "ma-control-schedules": [
      {
        "ma-schedule-name": "Controller schedule",
        "ma-schedule-tasks": {
          {
            "ma-schedule-task-name": "Controller configuration",
            "ma-schedule-task-datasets": [
              {
                "ma-schedule-task-channel-names": ["Controller channel"]
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
          }
        }
        "ma-schedule-timing": {
          "ma-timing-name": "hourly randomly",
          "ma-timing-calendar": {
            "ma-calendar-minutes": ["00"],
            "ma-calendar-seconds": ["00"]
          }
          "ma-timing-random-spread": "3600000"
        }
      }
    ]
    "ma-credentials": { } // structure of certificate ommitted for brevity
  }
}
'''
url='http://172.24.20.185:8080/ma/config'
req=urllib2.Request(url,values)
req.get_method = lambda:"PUT"  
request=urllib2.urlopen(req) 
