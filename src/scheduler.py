import os

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# from sqlalchemy import or_
# from sqlalchemy.sql.expression import true, false

# from .config.DbConfig import DbConfig

# from .model import User, JobRule, BoundJobRule

from .slurm.SlurmMockService import SlurmMockService
from .slurm.SlurmWiki2Service import SlurmWiki2Service
from .slurm import EEvent
from .slurm import Event

# init db

# db_config = DbConfig()
# session = db_config.sesson_factory()

# cache

prioritized_jobs = dict()

# scehduler logic functions

# def get_hard_priority(uid):
#     try:
#         bound_rules = list(
#             session
#                 .query(BoundJobRule)
#                 .join(User, isouter=True)
#                 .join(JobRule, isouter=True)
#                 .filter(JobRule.hard_priority != None)
#                 .filter(or_(User.uid == uid, BoundJobRule.is_default == true()))
#         )
#     except:
#         print('Error while processing database query. Please tru again later.')

#     uid_bound_rules = list(filter(lambda rule: rule.user and rule.user.uid == uid, bound_rules))

#     if uid_bound_rules and uid_bound_rules[0] != None:
#         return uid_bound_rules[0].job_rule.hard_priority

#     default_bound_rules = list(filter(lambda rule: rule.is_default == True, bound_rules))

#     if default_bound_rules and default_bound_rules[0] != None:
#         return default_bound_rules[0].job_rule.hard_priority

#     raise Exception('No priorities found for this job.')


# def queue_job(job):
#     hard_priority = get_hard_priority(job['user'])

#     if hard_priority not in prioritized_jobs:
#         prioritized_jobs[hard_priority] = [ job ]
#     else:
#         prioritized_jobs[hard_priority].append(job)


# def start_next_job():
#     if not prioritized_jobs.keys():
#         print("No jobs in queue")
#         return

#     # TODO: check for required nodes, preferences etc

#     first_hard_priority = min(prioritized_jobs.keys())
#     first_priority_job = prioritized_jobs[first_hard_priority].pop(0)

#     if not prioritized_jobs[first_hard_priority]:
#         del prioritized_jobs[first_hard_priority]

#     slurm_service.start_job(first_priority_job)

# define slurm job event handler

def process_slurm_event(event):
    # if (event.get_type() == EEvent.JobQueued):
    #     print(f"New job arrived")
    #     queue_job(event.get_payload())
    #     start_next_job()
    # elif (event.get_type() == EEvent.JobDone):
    #     print(f"Job with id #{event.get_payload()} done")
    #     start_next_job()
    # elif (event.get_type() == EEvent.JobDeclined):
    #     print(f"Job with id #{event.get_payload()} declined")
    # elif (event.get_type() == EEvent.JobStarted):
    #     print(f"Job with id #{event.get_payload()} started")

    if (event.get_type() == EEvent.JobDone):
        pprint(event.get_payload())


# init slurm service, set event handler, emit queued event on slurm waiting jobs

# slurm_service = SlurmMockService('127.0.0.1', 8080)

slurm_service = SlurmWiki2Service()

slurm_service.set_subscriber(process_slurm_event)

slurm_service.run()