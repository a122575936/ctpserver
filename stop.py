from daemon import Daemon

class CtpServer(Daemon):
    def run(self):
        # Do stuff
        pass

ctpServer = CtpServer('./ctpserver.pid')
ctpServer.stop()
