
from action import Location, Point
from client import Client
import os
import threading
from time import sleep
from queue import SimpleQueue
from listener import Listener

from strategist import Strategist
from voice_pipeline import VoicePipeline

class GameManager:
    def __init__(self,
                 update_handler,
                 listener: Listener,
        ):
        game = os.environ['GAME_ID']
        self._client, update_generator = self.setup_client(game)
        self.action_queue = SimpleQueue()
        updates_thread = threading.Thread(target = self.setup_update_thread(update_generator, update_handler))
        strategist = Strategist(self.attack, self.find_all_owned_territory_coords) # TODO this is a gross way to do this, but I'm not sure what would be better

        self.voice_pipeline = VoicePipeline(
            strategist=strategist,
            listener=listener,
        )

        updates_thread.start()

        sleep(0.5)
        self._client.set_force_start(game)

    def setup_client(self, game):
        client = Client()
        updates_generator = client.get_updates()
        client.set_username(os.environ['USER_ID'], os.environ['USERNAME'])
        client.join_game(game)
        return client, updates_generator

    def find_all_owned_territory_coords(self):
        owned_territory = []
        grid = self._client._map.grid

        for r in range(self._client._map.rows):
            for c in range(self._client._map.cols):
                if grid[r][c].isSelf() and grid[r][c].army > 1:
                    owned_territory.append(Location(Point(r, c), grid[r][c].army))

        return owned_territory
    
    def setup_update_thread(self, update_generator, update_handler):
        def thread():
            print('executing update thread')
            for update in update_generator:
                print(self._client._map)
                if self._client._map != None:
                    print('breaking!')
                    break
            self.voice_pipeline_thread = threading.Thread(target=self.voice_pipeline.run)
            self.voice_pipeline_thread.start()
            for update in update_generator:
                print(f"{self._client._map}")
                update_handler(self._client._map)
                if not self.action_queue.empty():
                    action = self.action_queue.get()
                    start = action[0]
                    dest = action[1]
                    self._client.attack(start.r, start.c, dest.r, dest.c)


        return thread
    
    def attack(self, start, destination):
        self.action_queue.put((start, destination))