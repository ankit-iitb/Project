# CineMatch: Your Personal Movie Recommendation Engine

## 👋 Introduction

Welcome to CineMatch, a **content-based movie recommendation system** I built as part of my machine learning journey during Seasons of Code 2025.

This project wasn't just about building a working system—it was about **learning by doing**. From understanding movie metadata and performing feature extraction to deploying a real-time ML model, this repository showcases everything I explored to make this project possible.

---
## 🔍 Why This Project?

We've all been there: scrolling endlessly, trying to figure out what to watch next. I thought, "Why not build my own movie recommender that suggests similar titles based on your favorites?"

Instead of relying on ratings or user behavior, I opted for a **content-based filtering approach**. It's like training a bot that has read all the movie plots and learned about the key actors and directors, then gives you personalized suggestions based on the movie's "DNA"\!

---

## 🧠 What I Learned

This project was a deep dive into the machine learning lifecycle. Here's a look at the key concepts and tools I picked up:

### **Core Concepts**

  * Merging and preprocessing large datasets.
  * Feature extraction from natural language (movie descriptions, keywords, cast, crew).
  * Vectorization techniques (**CountVectorizer**, Bag-of-Words model).
  * Similarity metrics (**cosine similarity**).
  * Building recommenders based on content similarity.
  * Saving and loading ML artifacts using **Pickle**.
  * Integrating third-party APIs (TMDB).
  * Deploying ML apps using **Streamlit** & **Render**.

---

## 📁 Repository Structure

| Folder/File         | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `notebooks/`        | Jupyter experiments and data exploration.                    |
| `app.py`            | The Streamlit app that powers the web interface.             |
| `movies_dict.pkl`   | Serialized movie metadata.                                   |
| `similarity.pkl`    | The serialized cosine similarity matrix for fast lookups.    |
| `poster_urls.csv`   | Movie poster links fetched from the TMDB API.                |
| `requirements.txt`  | All dependencies required to run the project.                |
| `README.md`         | The document you're reading now.                             |

---

## 🎬 How It Works: From Metadata to Movie Magic

Here's the simplified pipeline of what goes on under the hood:

### 1\. **Data Cleaning & Merging**

  * Combined `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` using the `title` field.
  * Selected only relevant columns: `title`, `overview`, `genres`, `cast`, `crew`, `keywords`.

### 2\. **Feature Engineering**

  * Converted JSON strings in columns like `genres`, `cast`, and `crew` into actual Python lists.
  * Extracted only the top 3 actors and the director.
  * Flattened all text-based features into a single `tags` column.

### 3\. **Vectorization**

  * Used **CountVectorizer** with `max_features=5000` and removed English stopwords.
  * Transformed the textual tags into a numerical matrix of word counts.

### 4\. **Cosine Similarity**

  * Applied `cosine_similarity` to compute the pairwise similarity between all movies.
  * Stored the resulting similarity matrix for efficient lookups.

### 5\. **The Recommend Function**

```python
recommend('Inception') # returns: Interstellar, The Matrix, Shutter Island, etc.
```

  * Finds the index of a given movie.
  * Sorts the similarity scores and returns the top 5 matches (excluding the movie itself).

### 6\. **Movie Posters with the TMDB API**

  * Extracted poster links by calling TMDB's API with movie IDs.
  * Constructed complete poster URLs and saved them in a CSV file for the front end.

### 7\. **Deployment**

  * Built an interactive UI using **Streamlit**.
  * Deployed the app using **Render.com**.

The result? You input a movie, and the app instantly provides five similar movies with posters—it's that simple\!

\<br\>

-----

## 🔗 Live App & GitHub Repo

  * **Live App:** [get-movies-sdm1.onrender.com](https://www.google.com/search?q=https://get-movies-sdm1.onrender.com)
  * **GitHub Repo:** [CineMatch - Movie Recommender](https://www.google.com/search?q=https://github.com/your-username/cinematch)

-----

\<br\>

## 🛠️ Tools & Tech Stack

  * **Language:** Python
  * **Libraries:** pandas, NumPy, scikit-learn, pickle, requests
  * **NLP:** CountVectorizer, cosine similarity
  * **Web UI:** Streamlit
  * **Hosting:** Render.com
  * **IDE:** PyCharm
  * **Dataset:** TMDB 5000 Movie Dataset

---

## 🎯 Key Takeaways

✅ Learned how to clean, process, and merge real-world datasets.

✅ Explored natural language techniques to convert text into vectors.

✅ Built a real-time recommendation engine using cosine similarity.

✅ Integrated a production-grade API for fetching dynamic content.

✅ Packaged and deployed a working ML project end-to-end.

✅ And most importantly… made movie night a lot more fun\! 😄
