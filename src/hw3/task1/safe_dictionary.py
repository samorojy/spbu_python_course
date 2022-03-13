from contextlib import contextmanager
from threading import Lock


class SafeDictionary:
    def __init__(self):
        self._dict = {}
        self._lock = Lock()

    @contextmanager
    def modify(self):
        self._lock.acquire()
        yield self._dict
        self._lock.release()
