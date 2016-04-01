from daemon import Daemon
import PythonServer

class CtpServer(Daemon):
    def run(self):
        # Do stuff
        PythonServer.StartServer()

ctpServer = CtpServer('./ctpserver.pid')
ctpServer.start()
