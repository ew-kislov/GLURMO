from slurm.SlurmService import SlurmService


class SlurmRestService(SlurmService):
    def start_job(self, job):
        pass

    def get_jobs(self, time = None):
        pass

    def get_nodes(self):
        pass

    def get_partitions(self):
        pass

    def set_event_hook(self, url):
        pass
