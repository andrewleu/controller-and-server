import web

urls = (
    '/ma', 'indx'
)
response= '''{
       "ma-status-and-capabilities": {
           "ma-agent-id": "", 
           "ma-device-id": "", 
           "ma-hardware": "", 
           "ma-firmware": "", 
           "ma-version": "", 
           "ma-interfaces": [
               {
                   "ma-interface-name": "", 
                   "ma-interface-type": ""
               }
           ], 
           "ma-last-measurement": "", 
           "ma-last-report": "", 
           "ma-last-instruction": "", 
           "ma-last-configuration": "", 
           "ma-supported-tasks": [
               {
                   "ma-task-name": "", 
                   "ma-task-registry": ""
               }, 
               {
                   "ma-task-name": "", 
                   "ma-task-registry": ""
               }, 
               {
                   "ma-task-name": "", 
                   "ma-task-registry": ""
               }, 
               {
                   "ma-task-name": "", 
                   "ma-task-registry": ""
               }, 
               {
                   "ma-task-name": "", 
                   "ma-task-registry": ""
               }
           ]
       }
   }'''
class indx:
    def GET(self):
        return response

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
