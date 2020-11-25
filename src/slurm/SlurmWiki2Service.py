import yaml
import socket
import datetime

from slurm.SlurmService import SlurmService

class SlurmWiki2Service(SlurmService):
    def __init__(self, config):
        self.__init_connection(config)

    def __init_connection(self, config):
        host = config.get('host')
        port = config.get('wiki2_port')

        self.__socket = socket.socket()
        self.__socket.connect((host, port))