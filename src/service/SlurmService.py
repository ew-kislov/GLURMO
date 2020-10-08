from abc import ABCMeta, abstractmethod


class SlurmService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_job(self, job, nodes):
        raise NotImplementedError

    @abstractmethod
    def get_jobs(self, time, jobs = None):
        raise NotImplementedError

    @abstractmethod
    def get_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def get_event_hook(self):
        raise NotImplementedError