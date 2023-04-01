from TestVagrant import RecentlyPlayedSongs
# Create a new store with capacity 3
store = RecentlyPlayedSongs(3)

# User 1 plays songs S1, S2, and S3
store.play_song(1, "S1")
store.play_song(1, "S2")
store.play_song(1, "S3")

# Get the recently played songs for User 1
print(store.get_recently_played_songs(1))  # Output: ['S1', 'S2', 'S3']

# User 1 plays song S4
store.play_song(1, "S4")

# Get the recently played songs for User 1
print(store.get_recently_played_songs(1))  # Output: ['S2', 'S3', 'S4']

# User 1 plays song S2 again
store.play_song(2, "S2")

# Get the recently played songs for User 1
print(store.get_recently_played_songs(1))  # Output: ['S3', 'S4', 'S2']

# User 1 plays song S1 again
store.play_song(1, "S1")

# Get the recently played songs for User 1
print(store.get_recently_played_songs(1))  # Output: ['S4', 'S2', 'S1']