"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


PROFILES = {
    # Standard profiles
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.3,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "likes_acoustic": False,
    },
    # Edge cases — designed to expose scoring quirks
    "Sad Hyperdancer": {
        # High energy + sad mood: energy score will be high but mood never matches
        # happy/chill songs. Scores cluster around 30 pts max with no mood bonus.
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.9,
        "likes_acoustic": False,
    },
    "Acoustic Intense": {
        # Wants acoustic AND intense — most acoustic songs are chill/lofi.
        # Genre/mood bonuses will rarely stack; acousticness bonus may offset.
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.85,
        "likes_acoustic": True,
    },
    "Middle-of-the-Road": {
        # target_energy=0.5 gives every song ~15/30 energy pts.
        # Mood/genre still decide ranking, but energy never differentiates.
        "favorite_genre": "jazz",
        "favorite_mood": "melancholic",
        "target_energy": 0.5,
        "likes_acoustic": False,
    },
}


def run_profile(name: str, prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(prefs, songs, k=k)
    print("\n" + "=" * 50)
    print(f"  Profile: {name}")
    print("=" * 50)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score : {score:.1f} / 100")
        print(f"    Why   : {explanation}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    for name, prefs in PROFILES.items():
        run_profile(name, prefs, songs)


if __name__ == "__main__":
    main()
