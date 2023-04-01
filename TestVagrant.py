from collections import defaultdict, deque

class RecentlyPlayedSongs:
    def __init__(self, capacity):
        self.capacity = capacity
        self.recently_played = defaultdict(deque)

    def play_song(self, user_id, song_id):
        if len(self.recently_played[user_id]) >= self.capacity:
            self.recently_played[user_id].popleft()
        self.recently_played[user_id].append(song_id)

    def get_recently_played_songs(self, user_id):
        return list(self.recently_played[user_id])