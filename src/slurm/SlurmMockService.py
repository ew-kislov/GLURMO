from threading import Thread
from random import randint
from time import sleep

import json

from .SlurmService import SlurmService
from .EJobState import EJobState
from .EEvent import EEvent
from .Event import Event

class SlurmMockService(SlurmService):
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

        self.__queued_jobs = [
            {
                'id': 3,
                'user': 501,
                'group': 0,
                'nodes_required': 2
            },
            {
                'id': 8,
                'user': 100,
                'group': 1,
                'nodes_required': 5
            }
        ]
        self.__partitions = ['debug', 'batch']
        self.__idle_nodes = [12, 35, 2, 18, 3, 54, 24, 12]

        self.__subscribers = []

    def queue_job(self, job):
        job_id = list(map(lambda m_job: m_job['id'], self.__queued_jobs)) + 1
        job['id'] = job_id

        self.__queued_jobs.append(job)
        for subscriber in self.__subscribers:
            subscriber(Event(EEvent.JobQueued, job))

    def start_job(self, job):
        # remove job from queued
        self.__queued_jobs = list(filter(lambda m_job: m_job['id'] != job['id'], self.__queued_jobs))

        job_thread = Thread(target=self.__start_job_in_thread, args=[job])
        job_thread.start()

    def get_jobs(self, time=None):
        return self.__queued_jobs

    def get_partitions(self):
        return self.__partitions

    def get_idle_nodes(self):
        return self.__idle_nodes

    def set_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def __start_job_in_thread(self, job):
        # job start emitation
        time_to_start = randint(1, 2)
        sleep(time_to_start)

        required_nodes_num = job['nodes_required']

        if (required_nodes_num > len(self.__idle_nodes)):
            # notify subscrubers of job decline(due to lack of needed nodes)
            for subscriber in self.__subscribers:
                subscriber(Event(EEvent.JobDeclined, job['id']))

            return

        used_nodes = self.__idle_nodes[0:required_nodes_num]
        self.__idle_nodes = self.__idle_nodes[required_nodes_num:]

        # notify subscrubers of job start
        for subscriber in self.__subscribers:
            subscriber(Event(EEvent.JobStarted, job['id']))

        # job work emitation
        work_time = randint(2, 3)
        sleep(work_time)

        self.__idle_nodes += used_nodes

        # notify subscrubers of job end
        for subscriber in self.__subscribers:
            subscriber(Event(EEvent.JobDone, job['id']))
