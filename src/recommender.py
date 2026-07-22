from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return list of dicts with typed numeric fields."""
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(dict(row))
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song 0–100 against user prefs; return (score, reason_list)."""
    score = 0.0
    reasons = []

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 40
        reasons.append(f"mood matches '{song['mood']}'")

    energy_score = (1 - abs(user_prefs["target_energy"] - song["energy"])) * 30
    score += energy_score
    reasons.append(f"energy match ({energy_score:.1f}/30 pts)")

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 20
        reasons.append(f"genre matches '{song['genre']}'")

    if user_prefs["likes_acoustic"] and song["acousticness"] > 0.6:
        score += 10
        reasons.append("high acousticness fits your preference")
    elif not user_prefs["likes_acoustic"] and song["acousticness"] < 0.3:
        score += 10
        reasons.append("low acousticness fits your preference")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return top-k songs sorted by score as (song, score, explanation) tuples."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [(song, score, ", ".join(reasons)) for song, score, reasons in scored[:k]]
