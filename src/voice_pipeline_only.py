from voice_pipeline import VoicePipeline
from strategist import DoNothingStrategist
from listener import SpeechRecognitionListener
voice_pipeline = VoicePipeline(
    strategist=DoNothingStrategist(),
    listener=SpeechRecognitionListener(),
).run()