from action import Action
from action_classifier import classify_action
from strategist import Strategist

class VoicePipeline:
    def __init__(self, strategist: Strategist, listener):
        self._listener = listener
        self._strategist: Strategist = strategist
    
    def run(self):
        for uterance in self._listener.listen():
            action: Action = classify_action(uterance)
            self._strategist.execute(action)
            


