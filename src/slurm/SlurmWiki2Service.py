import socket
import os;
import time;

from .SlurmService import SlurmService

from .EEvent import EEvent
from .Event import Event

class SlurmWiki2Service(SlurmService):
    def __init__(self):
        self.__subscribers = []

        self.__host = os.getenv("WIKI2_HOST")
        self.__wiki2_port = os.getenv("WIKI2_PORT")
        self.__port_for_wiki2 = os.getenv("PORT_FOR_WIKI2")

        self.__init_connection()

    def __init_connection(self):
        print(int(self.__port_for_wiki2))
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, int(self.__port_for_wiki2)))
        self.__socket.listen(10)

    def set_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def run(self):
        while True:
            conn, addr = self.__socket.accept()
            print('Connected by', addr)
            while True:
                data = conn.recv(4).decode()
                if not data:
                    break

                if data.strip() == '1234':
                    jobs = self.__get_jobs()

                    for subscriber in self.__subscribers:
                        subscriber(Event(EEvent.JobDone, jobs[-1]))

    def __get_jobs(self):
        client_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_fd.connect((self.__host, int(self.__wiki2_port)))
        
        command = f'AUTH=slurm DT=SC=-300 TS={round(time.time())} CMD=GETJOBS ARG=0:ALL\n'
        header = str(len(command) - 1).zfill(8)

        print(f'Running command: header "{header}" body "{command}"')

        client_fd.send(str.encode(header));
        client_fd.send(str.encode(command))

        header = int(client_fd.recv(8).decode())
        jobsRaw = client_fd.recv(header).decode()

        jobs = self.__parse_jobs(jobsRaw)

        client_fd.close()

        return jobs

    def __parse_jobs(self, jobsRaw):
        jobsRawList = jobsRaw.split('#')

        jobsRawList.pop(0)

        jobs = []

        for jobRaw in jobsRawList:
            pairs = jobRaw[(jobRaw.find(':') + 1):].split(';')
            job = dict()
            job['id'] = jobRaw[0:(jobRaw.find(':'))]
            for pair in pairs:
                pairArr = pair.split('=')
                if len(pairArr) != 2:
                    continue
                job[pairArr[0]] = pairArr[1]
            jobs.append(job)

        return jobs