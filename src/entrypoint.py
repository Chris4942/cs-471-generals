#!/bin/python
from voice_pipeline import VoicePipeline
from game_manager import GameManager
from strategist import Strategist
from listener import DumbListener

game_manager = GameManager(
    update_handler = lambda i: (),
    listener=DumbListener(),
)