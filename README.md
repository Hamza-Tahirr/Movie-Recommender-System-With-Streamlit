# Movie Recommender System

A content-based movie recommender built on the TMDB 5000 movies dataset. The notebook turns each movie's plot, genres, keywords, cast and director into a text profile and compares movies with cosine similarity. A Streamlit app then lets you pick a movie and shows five similar ones with their posters.

## Screenshots

Movie selection:

![Movie selection](https://user-images.githubusercontent.com/90556877/189056984-88a14357-0841-4445-83d6-a67b5f33d341.png)

Recommendations:

![Recommendations](https://user-images.githubusercontent.com/90556877/189071544-4adf599f-a0c9-4796-813c-ce0ceb675512.png)

## How it works

The notebook (`Movie Recommendation System .ipynb`) does the following:

1. Loads `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv.zip` and merges them on the movie title (4,809 rows).
2. Keeps only `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast` and `crew`, and drops the 3 movies with no overview, leaving 4,806 movies.
3. Parses the JSON-style columns with `ast.literal_eval` to get genre names, keywords, the top 3 cast members and the director.
4. Removes spaces inside names (for example `Sam Worthington` becomes `SamWorthington`) so each person or genre is a single token, then joins everything into one lowercase `tags` string per movie.
5. Applies Porter stemming from NLTK so words like "loved" and "loving" map to the same token.
6. Converts the tags into bag-of-words vectors with `CountVectorizer` (5,000 most frequent words, English stop words removed), giving a 4,806 x 5,000 matrix.
7. Computes the cosine similarity between every pair of movies and recommends the 5 most similar ones.
8. Saves the processed data (`movie_dict.pkl`, `movies.pkl`) and the similarity matrix (`similarity.pkl`) for the app.

For example, `recommend('John Carter')` in the notebook returns Riddick, Krrish, The Other Side of Heaven, The Legend of Hercules and Get Carter.

## Web app

`app.py` is a Streamlit app that:

- lists all 4,806 movies in a dropdown,
- shows the 5 most similar movies when you click **Recommend**,
- fetches each recommended movie's poster from the TMDB API.

`similarity.pkl` is about 185 MB, so it is not stored in the repository. If the file is present (for example after running the notebook) the app loads it; otherwise it rebuilds the matrix from the tags in `movie_dict.pkl` on first start and caches it.

Posters need a TMDB API key. Without one, the app still works and shows only the movie titles.

## Tech stack

Python, pandas, NumPy, NLTK, scikit-learn, Streamlit, Requests, Jupyter Notebook

## Project structure

```
├── Movie Recommendation System .ipynb   # data preparation, vectorization and similarity
├── app.py                               # Streamlit app
├── movie_dict.pkl                       # processed movies (id, title, tags) used by the app
├── movies.pkl                           # the same data saved as a pandas DataFrame
├── tmdb_5000_movies.csv                 # movie metadata
├── tmdb_5000_credits.csv.zip            # cast and crew
├── requirements.txt
└── .env.example
```

## Setup

```bash
git clone https://github.com/Hamza-Tahirr/Movie-Recommender-System-With-Streamlit.git
cd Movie-Recommender-System-With-Streamlit

python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
```

To show posters, copy `.env.example` to `.env` and set your key (you can get one from your account settings on [themoviedb.org](https://www.themoviedb.org/settings/api)):

```
TMDB_API_KEY=your_tmdb_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

To run the notebook, install Jupyter (`pip install notebook`) and open `Movie Recommendation System .ipynb`. Running it end to end recreates the three pickle files.

## Dataset

[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`). The credits file is kept zipped in this repo because of its size; pandas reads the zip directly.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
