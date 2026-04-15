# 🎬 Netflix Movie Recommendation System

A hybrid movie recommendation system inspired by Netflix, built using collaborative filtering and machine learning techniques to predict user ratings and recommend movies.

---

## 📌 Business Problem

Netflix connects users with movies they love using its recommendation engine *Cinematch*.  
This project explores alternative approaches to improve recommendation accuracy using machine learning.

Even small improvements in prediction accuracy can significantly enhance user experience and business value.

Source: https://www.netflixprize.com/rules.html

---

## 🎯 Problem Statement

- Predict ratings for movies not yet watched by users  
- Improve recommendation accuracy  
- Minimize prediction error  

### 📊 Evaluation Metrics
- RMSE (Root Mean Squared Error)  
- MAPE (Mean Absolute Percentage Error)  

---

## 📂 Dataset Overview

- 17,770 unique movies  
- 480,189 unique users  
- Ratings from 1 to 5  
- Timestamped user interactions  

---

## ⚙️ Approach

### 🔹 Collaborative Filtering
- Implemented using the Surprise library  
- SVD and related models  

### 🔹 Machine Learning
- XGBoost used for regression-based prediction  

### 🔹 Data Processing
- Feature engineering on user-item interactions  
- Handling sparse data  

---

## 🚀 Features

- Personalized movie recommendations  
- Hybrid recommendation system (CF + ML)  
- Scalable approach for large datasets  
- Data visualization and insights  
- Model performance comparison  

---

## 🛠️ Tech Stack

- Python 3  
- Pandas, NumPy, SciPy  
- Scikit-learn  
- Surprise  
- XGBoost  
- Matplotlib, Seaborn  
- Jupyter Notebook  

---

## ▶️ Getting Started

### 🔹 Prerequisites
- Python 3  
- Anaconda (recommended)  

---

### 🔹 Installation

```bash
conda install -c conda-forge xgboost
pip install surprise
