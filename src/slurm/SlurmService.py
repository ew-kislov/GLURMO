from abc import ABCMeta, abstractmethod


class SlurmService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_job(self, job):
        raise NotImplementedError

    @abstractmethod
    def get_jobs(self, time):
        raise NotImplementedError

    @abstractmethod
    def get_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def get_partitions(self):
        raise NotImplementedError

    @abstractmethod
    def set_subscriber(self, subscriber):
        raise NotImplementedError