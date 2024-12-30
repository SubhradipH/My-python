import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import tkinter as tk
from tkinter import messagebox

# Load datasets
try:
    movies = pd.read_csv(r'D:\projects\Movie reco\archive\tmdb_5000_movies.csv')
    credits = pd.read_csv(r'D:\projects\Movie reco\archive\tmdb_5000_credits.csv')
except FileNotFoundError as e:
    messagebox.showerror("Error", f"File not found: {e}")
    exit()

# Check the columns in the datasets
print("Movies Columns:", movies.columns)
print("Credits Columns:", credits.columns)

# Merge datasets on a common column
# Ensure that the column names are correct (e.g., 'id' and 'movie_id')
if 'id' not in movies.columns or 'movie_id' not in credits.columns:
    messagebox.showerror("Error", "Column names do not match for merging.")
    exit()

movies = movies.merge(credits, left_on='id', right_on='movie_id')

# Check the first few rows to verify merge
print(movies.head())

# Combine features for similarity calculations (ensure columns exist)
required_columns = ['genres', 'keywords', 'overview']
for col in required_columns:
    if col not in movies.columns:
        messagebox.showerror("Error", f"Column '{col}' not found in the dataset.")
        exit()

# Handling missing values and combining features
movies['combined_features'] = (
    movies['genres'].fillna('') + ' ' +
    movies['keywords'].fillna('') + ' ' +
    movies['overview'].fillna('')
)

# Vectorize the combined features
vectorizer = CountVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(movies['combined_features'])

# Calculate cosine similarity
similarity_matrix = cosine_similarity(feature_matrix)

# Create a similarity DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=movies['title'], columns=movies['title'])

def recommend_movies(movie_title, num_recommendations=5):
    """Recommend movies similar to the given movie."""
    if movie_title not in similarity_df.index:
        return None
    similar_movies = similarity_df[movie_title].sort_values(ascending=False)[1:num_recommendations + 1]
    return similar_movies

# GUI Application
def get_recommendations():
    """Fetch movie recommendations based on user input."""
    movie_title = entry.get()
    if not movie_title:
        messagebox.showerror("Error", "Please enter a movie title.")
        return

    recommendations = recommend_movies(movie_title)
    if recommendations is None:
        messagebox.showerror("Error", f"Movie '{movie_title}' not found in the database.")
    else:
        result = "\n".join(recommendations.index)
        messagebox.showinfo("Recommendations", f"Movies similar to '{movie_title}':\n{result}")

# Create main GUI window
root = tk.Tk()
root.title("Movie Recommendation System")

# Add GUI elements
label = tk.Label(root, text="Enter Movie Title:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Get Recommendations", command=get_recommendations, font=("Arial", 12))
button.pack(pady=20)

# Run the GUI loop
root.mainloop()
