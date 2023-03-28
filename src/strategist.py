from action import Action


class Strategist:
    def __init__(self, game_manager):
        self._game_manager = game_manager
    
    def execute(self, action: Action):
        print(f"I would be executing {action.direction}")
        pass