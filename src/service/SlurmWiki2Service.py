import yaml
import socket
import datetime

from service.SlurmService import SlurmService

from util import join
from constants import slurm_config_path


class SlurmWiki2Service(SlurmService):
    def __init__(self):
        self.__init_connection()

    def get_jobs(self, time, jobs=None):
        timestamp = int(datetime.datetime.timestamp(time))
        jobs_string = join(jobs, ':') if jobs != None else 'ALL'
        argument_string = f'{timestamp}:{jobs_string}'
        request_string = f'CMD=GETJOBS ARG={argument_string}'

        self.__socket.send(request_string.encode())

        data = self.__socket.recv(1024)
        print(data)

    def __init_connection(self):
        config = yaml.load(open(slurm_config_path), Loader=yaml.FullLoader)
        host = config.get('host')
        port = config.get('wiki2_port')

        self.__socket = socket.socket()
        self.__socket.connect((host, port))