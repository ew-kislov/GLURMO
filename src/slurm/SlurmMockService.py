from threading import Thread
from random import randint
from time import sleep

import requests
import json

from slurm.SlurmService import SlurmService
from helper.JsonSerializer import JsonSerializer
from model.EJobState import EJobState


class SlurmMockService(SlurmService):
    def __init__(self):
        self.__jobs = [{
            'id': 3,
            'user': 0,
            'group': 0,
            'state': EJobState.RUNNING
        }, {
            'id': 8,
            'user': 1,
            'group': 1,
            'state': EJobState.RUNNING
        }]
        self.__partitions = ['debug', 'batch']

        self.__hooks = []

    def start_job(self, job):
        job_thread = Thread(target=self.__start_job_in_thread, args=[job])
        job_thread.start()

    def get_jobs(self, time=None):
        return self.__jobs

    def get_partitions(self):
        return self.__partitions

    def set_event_hook(self, url):
        self.__hooks.append(url)

    def __start_job_in_thread(self, job):
        # job work emitation
        job_running_time = randint(5, 15)
        sleep(job_running_time)
        # notify all application by http route
        for hook in self.__hooks:
            requests.post(url=hook, json=JsonSerializer().encode(job))
