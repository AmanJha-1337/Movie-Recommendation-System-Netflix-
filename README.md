# 🎬 Netflix Movie Recommendation System

This repository now includes **two ways** to run recommendations:

1. **Streamlit app (`app.py`)** → works immediately in sandbox/cloud using bundled sample data.
2. **Original notebook (`Netflix_Movies_Recommendation.ipynb`)** → requires the large Netflix files in `Data/`.

## ✅ Fastest way (works in sandbox)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open: `http://localhost:8501`

### What changed

- Added `sample_movies.csv` so the app runs even when no external files are available.
- App also supports uploading your own CSV (`title` required; `genres` and `description` recommended).
- Added `.streamlit/config.toml` for cloud/container-friendly defaults.

## 🚀 Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. In Streamlit Cloud, create app from this repository.
3. Set:
   - **Main file path**: `app.py`
   - **Requirements file**: `requirements.txt`
4. Deploy.

## 📓 Notebook mode (optional)

If you want the original full workflow:

```bash
mkdir -p Data
jupyter notebook Netflix_Movies_Recommendation.ipynb
```

> The notebook expects Netflix raw files under `Data/` and may fail without them.
