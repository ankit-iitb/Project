🎥 CineMatch: My Movie Recommendation Engine
🌱 Seasons of Code 2025 · Machine Learning Project
👋 Introduction
Welcome to CineMatch — a content-based movie recommendation system built as part of my ML learning journey during Seasons of Code 2025.

This project isn’t just about building a working system — it’s about learning-by-doing. From understanding movie metadata to deploying a real-time ML model, this repo showcases everything I explored to make this project possible.
Hey folks! 👋
Welcome to my ML playground where I took on one of the most exciting beginner-to-intermediate projects out there: building a full-fledged movie recommendation system. This isn't just about coding — it's about learning through building, exploring machine learning fundamentals, playing with real-world data, and deploying a working product that actually helps people find great movies! 🍿✨

🔍 Why This Project?
We’ve all been there — scrolling endlessly trying to figure out what to watch next. I thought, why not build my own movie recommender that suggests similar titles based on your favorites?

Instead of relying on ratings or user behavior, I decided to go with a content-based filtering approach. It’s like training a bot that has read all the movie plots, learned about all the actors, and now gives you personalized suggestions based on movie DNA!

🧠 What I Learned
This wasn't just about finishing a project. Here's a look at the rich stack of concepts and tools I picked up:

🧩 Core Concepts Explored
Merging and preprocessing large datasets

Feature extraction from natural language (movie descriptions, keywords, cast, crew)

Vectorization techniques (CountVectorizer, BoW model)

Similarity metrics (cosine similarity)

Building recommenders based on content similarity

Saving and loading ML artifacts using Pickle

Integrating third-party APIs (TMDB)

Deploying ML apps using Streamlit & Render

📁 What’s Inside This Repo
Folder/File	Purpose
notebooks/	Jupyter experiments and data exploration
app.py	Streamlit app that powers the web interface
movies_dict.pkl	Serialized movie metadata
similarity.pkl	Serialized cosine similarity matrix
poster_urls.csv	Movie poster links fetched from TMDB
requirements.txt	All dependencies to get started
README.md	You’re reading it!

🎬 How It Works – From Metadata to Movie Magic
Here’s the simplified pipeline of what goes on under the hood:

1. 🧹 Data Cleaning & Merging
Combined tmdb_5000_movies.csv and tmdb_5000_credits.csv using the title field.

Selected only relevant columns: title, overview, genres, cast, crew, keywords.

2. 🛠️ Feature Engineering
Converted JSON strings to actual Python lists.

Extracted only top 3 actors and the director.

Flattened all text-based features into a single tags column.

3. 📐 Vectorization
Used CountVectorizer with max_features=5000 and removed English stop words.

Transformed textual tags into a numerical matrix of word counts.

4. 📏 Cosine Similarity
Applied cosine_similarity to compute pairwise similarity between all movies.

Stored the resulting similarity matrix for fast lookup.

5. 🧠 The Recommend Function
python
Copy
Edit
recommend('Inception')  # returns: Interstellar, The Matrix, Shutter Island, etc.
Finds index of the given movie.

Sorts similarity scores and returns the top 5 matches (excluding itself).

6. 🖼️ Movie Posters with TMDB API
Extracted poster links by calling TMDB’s API with movie IDs.

Constructed complete poster URLs and saved them in a CSV file.

7. 🌍 Deployment
Built a slick UI using Streamlit.

Deployed the app using Render.com.

Input a movie, get 5 similar movies with posters — it’s that simple!

🔗 Live App: get-movies-sdm1.onrender.com
📂 GitHub Repo: CineMatch - Movie Recommender

🛠️ Tools & Tech Stack
Language: Python

Libraries: pandas, NumPy, scikit-learn, pickle, requests

NLP: CountVectorizer, cosine similarity

Web UI: Streamlit

Hosting: Render.com

IDE: PyCharm

Dataset: TMDB 5000 Movie Dataset

🎯 Key Takeaways
✅ Learned how to clean, process, and merge real-world datasets
✅ Explored natural language techniques to convert text into vectors
✅ Built a real-time recommendation engine using cosine similarity
✅ Integrated a production-grade API for fetching dynamic content
✅ Packaged and deployed a working ML project end-to-end
✅ And most importantly… made movie night a lot more fun! 😄
