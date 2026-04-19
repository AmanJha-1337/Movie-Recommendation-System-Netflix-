import io
import re
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

SAMPLE_DATA_PATH = Path("sample_movies.csv")


def normalize_text(value: str) -> str:
    value = str(value or "").lower()
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def build_features(df: pd.DataFrame) -> pd.Series:
    cols = [c for c in ["title", "genres", "description"] if c in df.columns]
    if not cols:
        raise ValueError("Dataset must include at least one of: title, genres, description")
    return df[cols].fillna("").astype(str).agg(" ".join, axis=1).map(normalize_text)


def recommend(df: pd.DataFrame, movie_title: str, top_n: int = 10) -> pd.DataFrame:
    if "title" not in df.columns:
        raise ValueError("Dataset must contain a 'title' column.")

    features = build_features(df)
    tfidf = TfidfVectorizer(stop_words="english", min_df=1)
    matrix = tfidf.fit_transform(features)

    title_series = df["title"].fillna("").astype(str)
    lookup = {t.lower(): i for i, t in enumerate(title_series)}
    idx = lookup.get(movie_title.lower())
    if idx is None:
        matches = title_series[title_series.str.lower().str.contains(movie_title.lower(), na=False)]
        if matches.empty:
            raise ValueError(f"Movie '{movie_title}' not found in dataset.")
        idx = matches.index[0]

    sim_scores = linear_kernel(matrix[idx], matrix).flatten()
    ranked = np.argsort(-sim_scores)
    ranked = [i for i in ranked if i != idx][:top_n]

    out = df.iloc[ranked].copy()
    out.insert(0, "similarity", sim_scores[ranked])
    return out


def load_default_data() -> pd.DataFrame:
    if SAMPLE_DATA_PATH.exists():
        return pd.read_csv(SAMPLE_DATA_PATH)

    fallback_csv = """title,genres,description,rating
Inception,Sci-Fi|Thriller,A thief enters dreams to steal secrets and plant ideas.,8.8
The Matrix,Sci-Fi|Action,A hacker discovers reality is a simulation and joins a rebellion.,8.7
Interstellar,Sci-Fi|Drama,A team travels through a wormhole to save humanity.,8.6
The Dark Knight,Action|Crime,Batman faces the Joker in Gotham City.,9.0
The Social Network,Drama,A story of Facebook's rise and its founder's conflicts.,7.7
Parasite,Thriller|Drama,A poor family infiltrates a rich household with unexpected consequences.,8.5
Whiplash,Drama|Music,A young drummer pushes himself under a demanding instructor.,8.5
Mad Max: Fury Road,Action|Adventure,Survivors race across a wasteland to escape a tyrant.,8.1
La La Land,Romance|Musical,Two artists fall in love while pursuing their dreams in Los Angeles.,8.0
The Godfather,Crime|Drama,The aging patriarch transfers control of his empire to his son.,9.2
"""
    return pd.read_csv(io.StringIO(fallback_csv))


def main() -> None:
    st.set_page_config(page_title="Netflix Recommender", page_icon="🎬", layout="wide")
    st.title("🎬 Netflix-style Movie Recommender")
    st.caption("Use bundled sample data or upload your own CSV.")

    with st.sidebar:
        st.header("Data source")
        uploaded = st.file_uploader("Upload CSV", type=["csv"])
        top_n = st.slider("Recommendations", min_value=3, max_value=20, value=10)

    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.success("Custom dataset loaded.")
    else:
        df = load_default_data()
        st.info("Using sample dataset from `sample_movies.csv`.")

    st.write(f"Dataset columns: {', '.join(df.columns)}")
    st.caption("Required: `title`. Recommended: `genres`, `description`, and optional `rating`.")

    if "title" not in df.columns:
        st.error("CSV must contain a 'title' column.")
        st.stop()

    movie = st.selectbox("Pick a movie", sorted(df["title"].dropna().astype(str).unique()))

    if st.button("Recommend", type="primary"):
        try:
            recs = recommend(df, movie, top_n)
            show_cols: List[str] = [c for c in ["similarity", "title", "genres", "rating", "description"] if c in recs.columns]
            st.subheader(f"Top {top_n} recommendations for: {movie}")
            st.dataframe(recs[show_cols], use_container_width=True, hide_index=True)
        except Exception as exc:
            st.error(str(exc))


if __name__ == "__main__":
    main()
