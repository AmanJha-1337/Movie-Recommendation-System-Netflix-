# 🎬 Netflix Movie Recommendation System

A hybrid movie recommendation system inspired by Netflix, built using collaborative filtering and machine learning techniques to predict user ratings and recommend movies.

## 📌 Business Problem

Netflix connects users with movies they love using its recommendation engine *Cinematch*. This project explores alternative approaches to improve recommendation accuracy using machine learning.

## 🎯 Problem Statement

- Predict ratings for movies not yet watched by users
- Improve recommendation accuracy
- Minimize prediction error

### 📊 Evaluation Metrics

- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

## 📂 Dataset Overview

- 17,770 unique movies
- 480,189 unique users
- Ratings from 1 to 5
- Timestamped user interactions

## ⚙️ Approach

- **Collaborative filtering** using `surprise` (SVD and related models)
- **Machine learning** using `xgboost` for regression-based prediction
- **Feature engineering** on user-item interactions
- **Sparse-matrix processing** for scalability

## 🛠️ Tech Stack

- Python 3
- Pandas, NumPy, SciPy
- Scikit-learn
- Surprise
- XGBoost
- Matplotlib, Seaborn
- Jupyter Notebook
- Streamlit

## ▶️ Quick Start (Sandbox-safe)

### 1) Create environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run the Streamlit app (recommended in sandbox)

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

The app works immediately with built-in sample data and also supports uploading your own CSV.

### 3) Run the notebook (optional)

The notebook uses a repository-local `Data/` folder.

```bash
mkdir -p Data
jupyter notebook Netflix_Movies_Recommendation.ipynb
```

> Note: the notebook expects the large Netflix raw files inside `Data/`, so it may fail if those files are not present.

## 🚀 Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and create a new app.
3. Select:
   - **Main file path**: `app.py`
   - **Python dependencies**: `requirements.txt`
4. Deploy.

