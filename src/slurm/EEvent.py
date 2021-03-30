from enum import Enum

class EEvent(Enum):
    JobQueued = 1
    JobStarted = 2
    JobDeclined = 3
    JobDone = 4