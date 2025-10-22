# 🎬 Movie Recommendation App

A machine learning-based movie recommendation app built using TF-IDF, cosine similarity, and simple data structures.  
Frontend built with **Streamlit** — runs completely offline.

## 📂 Project Structure
- `app.py` — Streamlit app frontend
- `recommender.py` — ML + DSA logic
- `movies.csv` — cleaned dataset
- `requirements.txt` — Python dependencies

# Movie reccomender Project
# Recommender System

An engine that works on movielens dataset, and used for reccomending a unwatched movie and predicting its rating for a user. Handled the Cold start problem by using demographics like age, gender, location etc....Built a hybrid movie reccomender that combines Content based and collabarative filtering.


## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

