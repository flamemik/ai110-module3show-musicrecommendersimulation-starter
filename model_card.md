# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Musicalizer Extravaganza

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

My recommender is designed to take the data from songs and recommend which songs are the most likely compatible with the persons interests based on the persons favorite genre, mood, energy, and more. It outputs a list of songs recommended and why. It assumes the user has data about what they like. This is for classroom exploration but it is not really suitable for real users since real users do not typically have data like whether they likee a certain energy or not.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

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

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are 20 songs in the catalog with varying genres or moods such as: classical, r&b for genres and mysterious, confident, and so on for moods. I simply added data. There are some aspects of musical taste missing in the dataset since it is hard to capture every single detail but things like words that come up frequently in songs, beats per minute, etc. are missing from my dataset since I did not include them.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

My system seems to work well in scoring and I even took a look at edge cases with my AI companion to find ways to mismatch the output. It also works well for parts where data is consistent like a high energy pop song or a low energy classical song.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

There are certain edge cases I created which shows how the system struggles or behaves unfairly. 
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

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I posted the output in the README file but I tested several different user profiles and looked for what each profile gets recommended based on what their preferences are. It surprised me that when I tried to create edge cases, it helped reveal some flaws in my system and things I can improve. I picked a sad mood but made a profile have high energy. This caused a user's mood to be ignored if the mood didn't fit but the energy fit. In the recommendations I made sure to look at the scoring of what was being recomended, the reason why its being recomended, energy match, and the acousticness.


---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

To improve the model next I would create more ways to further refine and categorize the genres, mood, and more and create more data points to further filter songs to make sure the songs are more accurately recommended. There are better ways of explaining recommendations but it would involve having to make more data points to make it make more sense. To improve diversity among the top results, having a way to change a user's mood for the current moment and favorite genre for the time being can improve diversity among top results.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

It was very interesting learning how AI was able to determine how to create, manipulate, and test data to determine valid responses for musical data despite music being somewhat of an emotional artistic thing. Having an AI scan a song and find data that can match it to other songs without needing to actually hear the song is interesting. This changed the way I think about music recommendation apps because it helps explain to me why certain songs that are recommended to me sound similar to ones I've heard before or use the same lyrics too. Recommender systems user various algorithms and ways to determine which songs to recommend to users but the main thing is finding patterns in songs that contain data that shows a user is more likely to enjoy a song based on aspects that a computer can analyze to recommend other songs.