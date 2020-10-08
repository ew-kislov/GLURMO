from pathlib import Path

def join(iterator, seperator):
    it = map(str, iterator)
    seperator = str(seperator)
    string = next(it, '')
    for s in it:
        string += seperator + s
    return string

def get_root_path():
    path = Path().resolve().parent
    return path