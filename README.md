🎬 Movie Recommendation System
A content-based movie recommendation system built using the TMDB 5000 Movie Dataset, designed to recommend movies similar to a given title based on genres, cast, crew, keywords, and overview metadata.

🔗 Live Demo: get-movies-sdm1.onrender.com
📁 GitHub Repo: Movie-Recommender-System

📌 Project Highlights
Built a content-based recommendation engine using cosine similarity.

Preprocessed and merged movie metadata from TMDB.

Extracted key features: genres, cast, crew (director), keywords, and overview.

Created unified feature tags and vectorized text using CountVectorizer.

Developed and deployed a responsive web app with Streamlit.

Integrated TMDB API to fetch and display movie posters.

Deployed on Render.com for public access.

🧩 Dataset Description
The project uses two datasets from TMDB 5000 Movie Dataset:

tmdb_5000_movies.csv – Contains movie information: title, genres, keywords, overview, etc.

tmdb_5000_credits.csv – Contains cast and crew data.

⚙️ Workflow and Architecture
1. Data Loading & Exploration
Imported CSVs into pandas DataFrames.

Explored data shape, missing values, and key features.

2. Data Preprocessing
Merged movies and credits on the title.

Selected useful columns: movie_id, title, overview, genres, keywords, cast, crew.

Converted JSON strings into Python lists.

Extracted top 3 actors and the director.

Removed missing/null entries.

Created a consolidated tags column by merging overview, genres, keywords, cast, and crew.

3. Feature Engineering
Converted the tags column into lowercase and cleaned spaces.

Joined the list items into a single string for each movie.

4. Text Vectorization
Used CountVectorizer with:

max_features=5000

stop_words='english'

Created a word frequency matrix for all movie tags.

5. Cosine Similarity
Computed cosine similarity between vectorized movie tags.

Constructed a similarity matrix where higher values indicate closer movie similarity.

6. Recommendation Function
recommend(movie_name) returns the top 5 most similar movies.

Skips the input movie and sorts others based on similarity scores.

7. Model Saving
Saved the movies_dict and similarity matrix using pickle.

Avoids recomputation and speeds up deployment.

8. Poster Fetching (Bonus Feature)
Integrated TMDB API to fetch movie poster URLs.

Used requests to query movie IDs and generate image URLs.

9. Web App Development
Built using Streamlit and deployed via Render.com.

Allows users to:

Input a movie title.

Get recommended titles + poster visuals.

Enjoy a clean UI powered by real-time API calls.

🛠️ Tech Stack
Component	Tools Used
Language	Python
Libraries	Pandas, NumPy, Scikit-learn, Pickle, Streamlit
Model Type	Content-Based Filtering
Vectorization	CountVectorizer (Bag of Words)
Similarity	Cosine Similarity
Deployment	Render.com
API	TMDB API
IDE	PyCharm
Hosting Dataset	Kaggle
