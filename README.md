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

You can include a simple diagram or bullet list if helpful.

A potential bias that can be expected with my system is an overprioritization on a user's mood rather than genre and acoustic and energy since the mood grants a substantial amount of points more than the rest, but I would assume that in the real-world a person's mood would affect whether they like a song more or not.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



