from enum import Enum

class EJobState(Enum):
    Queued = 1
    Running = 2
    Done = 3
    Declined = 4
    Aborted = 5