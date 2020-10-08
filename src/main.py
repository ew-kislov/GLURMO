import datetime

from service.SlurmWiki2Service import SlurmWiki2Service

# test slurm get jobs
slurm_service = SlurmWiki2Service()
slurm_service.get_jobs(datetime.datetime.now(), (43, 45, 3))