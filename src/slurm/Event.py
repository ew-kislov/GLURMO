class Event(object):
    def __init__(self, type, payload):
        self.__type = type
        self.__payload = payload

    def get_type(self):
        return self.__type

    def get_payload(self):
        return self.__payload