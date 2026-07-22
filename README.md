# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Summary of my music recommender simulation: Takes information about certain songs in the csv file and determines the similarity to what a user's preferences are and outputs a list of the most similar songs that a user may like based on their preferences. There is a unique scoring rule that takes many aspects into account. My system gets right most of the comparisons but when it comes to genre's, I believe it is limited since there could be similar genre's that have different names and should be annointed some similarity points for being similar genres. For the most part my system does annoint points well and creates a list with reasons as to why each song is matched with the user's preferences. This mirrors real world AI recommenders since it uses a similar process of comparing user's data and song data to determine whether a user may be compatible with or like a song due to similarities in their preferences.

---

## How The System Works

Explain your design in plain language.

My understanding of how real-world recommendations work is that there are several types of ways to filter data to match similarities. The main ones being looked at are collaborative vs content-based filtering. In collaborative filtering it filters using the behaviors of different user's and comparing them to each other. In content-based filtering, it uses the attributes of the songs rather than the users to compare songs attributes and match them to suitable users based on how similar songs are to each other. In the real-world spotify uses a mix of both. 
I will prioritze a mix of both to accurately determine songs that will match a user's taste. The ranking rule would check the songs with the highest score from scoring rule in order to make a ranking of the highest scoring songs to recommend them to the user.
In my system, a user will input their preferences of genre,mood, energy, and whether they like acoustic, my system will judge each song in songs.csv to determine which has the highest match and it would output the top K recommendations.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
  Each Song in my system has these features for sorting in order by importance: Mood, energy, genre, and acousticness.
- What information does your `UserProfile` store
Each user in my UserProfile will store the following information in order by importance: favorite genre, favorite mood, target energy, and whether they like acoustic or not.
- How does your `Recommender` compute a score for each song
My Recommender computes a score for each song by checking whether the mood of a song matches the users favorite mood and adds 40 points, checks how close a song's energy is compared to the user's target energy and annoints points, checks if the genre matches the user's favorite genre and adds 20 points, if the song is accousitc and the user likes accoustic then add 10 points.
- How do you choose which songs to recommend
I choose which songs to recommend based on the amount of points a song gets when put through the Recommender. A higher number means the higher likelihood that a user would like the song. I would only recommend songs that have a high number of points since those would fit the criteria of what a user would like best.


A potential bias that can be expected with my system is an overprioritization on a user's mood rather than genre and acoustic and energy since the mood grants a substantial amount of points more than the rest, but I would assume that in the real-world a person's mood would affect whether they like a song more or not.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

~~~Sample Recommendation Output
============================================
   🎵  Your Top Music Recommendations  🎵
============================================

#1  Sunrise City — Neon Echo
    Score : 99.4 / 100
    Why   : mood matches 'happy', energy match (29.4/30 pts), genre matches 'pop', low acousticness fits your preference

#2  Rooftop Lights — Indigo Parade
    Score : 68.8 / 100
    Why   : mood matches 'happy', energy match (28.8/30 pts)

#3  Gym Hero — Max Pulse
    Score : 56.1 / 100
    Why   : energy match (26.1/30 pts), genre matches 'pop', low acousticness fits your preference

#4  Neon Sermon — Static Monk
    Score : 39.7 / 100
    Why   : energy match (29.7/30 pts), low acousticness fits your preference

#5  Voltage Drop — Circuit Breaker
    Score : 38.8 / 100
    Why   : energy match (28.8/30 pts), low acousticness fits your preference
~~~

~~~
Here's what each edge case reveals:

Sad Hyperdancer — mood sad never fires for high-energy songs. Top picks are pop/energy matches at ~57 pts, but the one actual sad song (Broken Strings) scores lower (52 pts) because its energy is ~0.37, far from 0.9. Quirk exposed: a correct mood match can still lose to wrong-mood songs with better energy fit.

Acoustic Intense — intense rock songs are almost never acoustic, so the likes_acoustic bonus never stacks with mood/genre bonuses. Storm Runner wins at 88 but skips the acoustic bonus (acousticness=0.10). Quirk exposed: two desired traits are structurally incompatible in the dataset, so the acoustic preference is wasted.

Middle-of-the-Road — target_energy=0.5 gives every song 15–27 pts of energy score; nothing gets zeroed out but nothing gets maxed either. jazz + melancholic exist in dataset but rarely together, so genre and mood bonuses almost never both fire. Quirk exposed: when genre/mood are rare combos, energy noise fully controls ranking.

~~~

~~~

==================================================
  Profile: High-Energy Pop
==================================================

#1  Sunrise City — Neon Echo
    Score : 97.6 / 100
    Why   : mood matches 'happy', energy match (27.6/30 pts), genre matches 'pop', low acousticness fits your preference

#2  Rooftop Lights — Indigo Parade
    Score : 65.8 / 100
    Why   : mood matches 'happy', energy match (25.8/30 pts)

#3  Gym Hero — Max Pulse
    Score : 59.1 / 100
    Why   : energy match (29.1/30 pts), genre matches 'pop', low acousticness fits your preference

#4  Storm Runner — Voltline
    Score : 39.7 / 100
    Why   : energy match (29.7/30 pts), low acousticness fits your preference

#5  Carnival Lights — Los Ritmos
    Score : 39.4 / 100
    Why   : energy match (29.4/30 pts), low acousticness fits your preference

==================================================
  Profile: Chill Lofi
==================================================

#1  Library Rain — Paper Lanterns
    Score : 98.5 / 100
    Why   : mood matches 'chill', energy match (28.5/30 pts), genre matches 'lofi', high acousticness fits your preference

#2  Midnight Coding — LoRoom
    Score : 96.4 / 100
    Why   : mood matches 'chill', energy match (26.4/30 pts), genre matches 'lofi', high acousticness fits your preference

#3  Spacewalk Thoughts — Orbit Bloom
    Score : 79.4 / 100
    Why   : mood matches 'chill', energy match (29.4/30 pts), high acousticness fits your preference

#4  Focus Flow — LoRoom
    Score : 57.0 / 100
    Why   : energy match (27.0/30 pts), genre matches 'lofi', high acousticness fits your preference

#5  Broken Strings — Ember Vale
    Score : 39.7 / 100
    Why   : energy match (29.7/30 pts), high acousticness fits your preference

==================================================
  Profile: Deep Intense Rock
==================================================

#1  Storm Runner — Voltline
    Score : 98.8 / 100
    Why   : mood matches 'intense', energy match (28.8/30 pts), genre matches 'rock', low acousticness fits your preference

#2  Frozen Tundra — Pale Signal
    Score : 79.7 / 100
    Why   : mood matches 'intense', energy match (29.7/30 pts), low acousticness fits your preference

#3  Gym Hero — Max Pulse
    Score : 79.4 / 100
    Why   : mood matches 'intense', energy match (29.4/30 pts), low acousticness fits your preference

#4  Carnival Lights — Los Ritmos
    Score : 37.9 / 100
    Why   : energy match (27.9/30 pts), low acousticness fits your preference

#5  Voltage Drop — Circuit Breaker
    Score : 36.7 / 100
    Why   : energy match (26.7/30 pts), low acousticness fits your preference

==================================================
  Profile: Sad Hyperdancer
==================================================

#1  Gym Hero — Max Pulse
    Score : 59.1 / 100
    Why   : energy match (29.1/30 pts), genre matches 'pop', low acousticness fits your preference

#2  Sunrise City — Neon Echo
    Score : 57.6 / 100
    Why   : energy match (27.6/30 pts), genre matches 'pop', low acousticness fits your preference

#3  Broken Strings — Ember Vale
    Score : 52.3 / 100
    Why   : mood matches 'sad', energy match (12.3/30 pts)

#4  Storm Runner — Voltline
    Score : 39.7 / 100
    Why   : energy match (29.7/30 pts), low acousticness fits your preference

#5  Carnival Lights — Los Ritmos
    Score : 39.4 / 100
    Why   : energy match (29.4/30 pts), low acousticness fits your preference

==================================================
  Profile: Acoustic Intense
==================================================

#1  Storm Runner — Voltline
    Score : 88.2 / 100
    Why   : mood matches 'intense', energy match (28.2/30 pts), genre matches 'rock'

#2  Gym Hero — Max Pulse
    Score : 67.6 / 100
    Why   : mood matches 'intense', energy match (27.6/30 pts)

#3  Frozen Tundra — Pale Signal
    Score : 66.7 / 100
    Why   : mood matches 'intense', energy match (26.7/30 pts)

#4  Desert Mirage — Dune Drift
    Score : 31.0 / 100
    Why   : energy match (21.0/30 pts), high acousticness fits your preference

#5  Voltage Drop — Circuit Breaker
    Score : 29.7 / 100
    Why   : energy match (29.7/30 pts)

==================================================
  Profile: Middle-of-the-Road
==================================================

#1  Rainy Season — Fernweh
    Score : 61.6 / 100
    Why   : mood matches 'melancholic', energy match (21.6/30 pts)

#2  Coffee Shop Stories — Slow Stereo
    Score : 46.1 / 100
    Why   : energy match (26.1/30 pts), genre matches 'jazz'

#3  Night Drive Loop — Neon Echo
    Score : 32.5 / 100
    Why   : energy match (22.5/30 pts), low acousticness fits your preference

#4  Neon Sermon — Static Monk
    Score : 31.3 / 100
    Why   : energy match (21.3/30 pts), low acousticness fits your preference

#5  Sunrise City — Neon Echo
    Score : 30.4 / 100
    Why   : energy match (20.4/30 pts), low acousticness fits your preference

~~~

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I ran several different experiments which I mentioned in my model_card. I created several profiles that demonstrated the different songs recommended for each one and why each was being recommended. The profiles I created were: High-Energy Pop, Chill Lofi, Deep Intense Rock, Sad Hyperdancer, Acoustic Intense, and Middle-of-the-Road. The Middle-of-the-road profile was a great way of understanding more of how my recommended worked since it was a very middle-of-the-road or equal profile which highlighted what data I priorized over others.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

1. Mood is all-or-nothing (40 pts)

Binary match. A "sad" song vs "melancholic" song gets same 0 pts despite being semantically close. A perfect energy+genre+acoustic song loses badly to a mediocre song that just happens to match mood. 40 pts is nearly half the score — one field dominates everything.

2. Energy penalizes outliers asymmetrically at scale

(1 - abs(target - song_energy)) * 30 — a song with energy 0.0 against target 0.9 scores 3 pts. A song with energy 0.5 against target 0.9 scores 18 pts. The least relevant song still gets 3 pts just for existing. No floor at zero means every song gets some energy credit.

3. Acoustic is binary with a hard threshold

> 0.6 or < 0.3 — a song at 0.59 acousticness gets 0 bonus for an acoustic lover. A song at 0.61 gets full 10 pts. No gradient. The 0.3–0.6 dead zone (songs that are "somewhat acoustic") always scores 0 regardless of preference.

4. Genre is also binary (20 pts)

Same as mood — no partial credit for related genres. lofi and jazz both chill genres; system treats them as completely unrelated. Rare genres (jazz, melancholic) get punished because the bonus almost never fires.

5. Score range is unfair across datasets

Max possible = 100. But a user whose preferred genre/mood don't exist in the dataset can never score above ~60. The displayed /100 implies parity that doesn't exist — a 60/100 for jazz-melancholic user is actually their maximum, not a mediocre result.

6. No penalty for mismatches

Irrelevant songs still accumulate energy pts. A jazz lover asking for chill jazz gets pop-happy songs ranked high purely on energy proximity. The scorer never subtracts for wrong genre/mood — it just fails to add. Neutral ≠ penalized.

Biggest structural unfairness: users with niche or rare taste combinations (sad+high-energy, acoustic+intense) are silently under-served. The system returns results without indicating it found nothing that truly fits — a 55/100 looks like a decent recommendation when it's actually "best of bad options."
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

How Recommenders Turn Data Into Predictions

Music recommenders work by converting raw song attributes — genre, mood, energy, tempo — into numeric scores that proxy for "how much will this user enjoy this." Our system does this explicitly: each user preference maps to a weighted rule (mood match = 40 pts, energy proximity = up to 30 pts, etc.), and songs are ranked by total score. More sophisticated systems like Spotify or Netflix learn these weights automatically from millions of user interactions — clicks, skips, replays — using collaborative filtering or neural networks. The core idea is the same either way: observable data (what songs have, what users do) gets transformed into a single ranked list that predicts preference.

Where Bias and Unfairness Emerge

Bias enters wherever the data or the scoring rules reflect unequal treatment without justification. In our system, the 40-point mood bonus means a mediocre genre match with the right mood beats a perfect energy+genre+acoustic match with the wrong mood — one feature dominates unfairly. At scale this gets worse: if training data comes mostly from one demographic (e.g., English-speaking pop listeners), the model learns to recommend well for that group and poorly for everyone else. Niche genres like jazz or regional music get less data, fewer plays, and lower scores — not because users dislike them, but because the system was never trained to understand them. The deeper problem is that the system never signals when it has no good answer. It always returns k results with scores that look confident, hiding the fact that a user with rare tastes is being served the least-bad option rather than a genuine match.


