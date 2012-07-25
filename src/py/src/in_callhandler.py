#!/usr/bin/env python

import SocketServer
import logging
from ESL import *

class ESLRequestHandler(SocketServer.BaseRequestHandler ):
  def setup(self):
    logging.info("New incoming call. client address %s ", self.client_address)

    fd = self.request.fileno()
    logging.info("socket descriptor is %d", fd)

    con = ESLconnection(fd)
    logging.info("ESL connection status %s", con.connected())
    if con.connected():
      info = con.getInfo()

      uuid = info.getHeader("unique-id")
      logging.info("callinfo: uuid %s ", uuid)
      con.execute("answer", "", uuid)
      con.execute("playback", "/home/uvadmin/uvas/conf/prompts/welcome2vtweet.wav", uuid);
    else:
      logging.error("Could not get ESL connection for socket descriptor %d", fd)



