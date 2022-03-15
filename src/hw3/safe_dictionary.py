from contextlib import contextmanager
from threading import Lock


class SafeDictionary:
    def __init__(self):
        self._dict = {}
        self._lock = Lock()

    @contextmanager
    def modify(self):
        with self._lock:
            yield self._dict
