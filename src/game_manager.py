
from client import Client
import os
import threading
from time import sleep

class GameManager:
    def __init__(self, update_handler):
        game = os.environ['GAME_ID']
        self._client, update_generator = self.setup_client(game)
        updates_thread = threading.Thread(target = self.setup_update_thread(update_generator, update_handler))

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
                    owned_territory.append(Location(r, c, grid[r][c].army))

        return owned_territory
    
    def setup_update_thread(self, update_generator, update_handler):
        def thread():
            print('executing update thread')
            for update in update_generator:
                update_handler(self._client._map)
        return thread

class Location:
    def __init__(self, r, c, n):
        self.row = r
        self.col = c
        self.n = n
    
    def __gt__(self, other):
        return self.n > other.n

    def __ge__(self, other):
        return self.n >= other.n
    
    def __lt__(self, other):
        return self.n < other.n

    def __lt__(self, other):
        return self.n <= other.n