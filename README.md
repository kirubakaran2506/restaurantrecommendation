Restaurant Recommendation System using Cosine Similarity
Project Overview

This project implements a content-based restaurant recommendation system using cosine similarity.
Based on a user’s preferred cuisine type, price range, and average cost, the system recommends the top 5 most similar restaurants from the dataset.

Objective

To build a recommendation system for restaurants

To preprocess real-world restaurant data

To encode categorical features

To compute similarity using cosine similarity

To recommend restaurants based on user preferences

Dataset

File name: Dataset.csv

Contains restaurant details such as:

Restaurant Name

Cuisines

Average Cost for two

Price range

Aggregate rating

Technologies Used

Python 3

Pandas – Data preprocessing

NumPy – Numerical operations

Scikit-learn – Label encoding and cosine similarity

Methodology

Load the restaurant dataset

Handle missing values:

Cuisines → Mode

Average cost → Mean

Price range → Mode

Aggregate rating → Mean

Encode cuisine names using Label Encoding

Select features:

Encoded cuisine

Price range

Average cost for two

Compute similarity using cosine similarity

Compare user preferences with all restaurants

Recommend the top 5 most similar restaurants
