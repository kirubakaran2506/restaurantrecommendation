import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("Dataset.csv")

print("Columns in dataset:", list(df.columns))

df["Cuisines"] = df["Cuisines"].fillna(df["Cuisines"].mode()[0])
df["Average Cost for two"] = df["Average Cost for two"].fillna(df["Average Cost for two"].mean())
df["Price range"] = df["Price range"].fillna(df["Price range"].mode()[0])
df["Aggregate rating"] = df["Aggregate rating"].fillna(df["Aggregate rating"].mean())

le = LabelEncoder()
df["Cuisine_encoded"] = le.fit_transform(df["Cuisines"])

features = df[["Cuisine_encoded", "Price range", "Average Cost for two"]]

similarity_matrix = cosine_similarity(features)

user_cuisine = "Italian"
user_price_range = 2
user_cost = 300

user_cuisine_encoded = le.transform([user_cuisine])[0]

user_vector = np.array([[user_cuisine_encoded, user_price_range, user_cost]])

user_similarity = cosine_similarity(user_vector, features)[0]

df["Similarity"] = user_similarity

recommended = df.sort_values(by="Similarity", ascending=False).head(5)

print("\nTop 5 recommended restaurants:\n")
print(
    recommended[[
        "Restaurant Name",
        "Cuisines",
        "Average Cost for two",
        "Aggregate rating"
    ]].rename(columns={
        "Restaurant Name": "name",
        "Cuisines": "cuisine",
        "Average Cost for two": "price",
        "Aggregate rating": "rating"
    }).to_string(index=False)
)