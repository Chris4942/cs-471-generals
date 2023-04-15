from abc import ABC, abstractmethod
from time import sleep
import speech_recognition as sr
import os

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
        
class SpeechRecognitionListener(Listener):
    def __init__(self):
        self.output_file = os.environ['WORDS_FILE']
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            while True:
                self.log("listening...")
                try:
                    audio = self.r.listen(
                        source,
                        timeout=6,
                        phrase_time_limit=6,
                    )
                    text = self.r.recognize_google(audio)
                    self.log(f"got text: {text}")
                    yield text
                except Exception as e:
                    self.log('could not recognize text')
                    self.log(e)
    
    def log(self, string):
        with open(self.output_file, 'a') as f:
            print(string, file=f)