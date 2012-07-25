import logging
from genutils import *
from in_callhandler import *


def handle_setloglevel_signal(level):
  #logging.disable(level - 1);
  #logging.disable(0) #this makes all log levels will be printed
  pass

def main():
  init_logging("voiceapp.log")
  logging.info("Starting application uvas")
  #server host is a tuple ('host', port)
  sock_server = SocketServer.ThreadingTCPServer(('', 8040), ESLRequestHandler)
  sock_server.serve_forever()

if __name__=='__main__':
  main()
