from abc import ABC, abstractmethod
from time import sleep

class Listener(ABC):
    @abstractmethod
    def listen(self):
        while False:
            yield None
    
class DumbListener(Listener):
    def listen(self):
        while True:
            sleep(1)
            yield 'some random giberish'