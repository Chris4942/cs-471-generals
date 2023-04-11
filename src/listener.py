from abc import ABC, abstractmethod
from time import sleep
import speech_recognition as sr

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
        print("setting up")
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            while True:
                print("listening...")
                try:
                    audio = self.r.listen(
                        source,
                        timeout=3,
                        phrase_time_limit=3,
                    )
                    text = self.r.recognize_google(audio)
                    print(f"got text: {text}")
                    yield text
                except Exception as e:
                    print('could not recognize text')
                    print(e)