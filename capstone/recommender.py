import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


movies = pd.read_csv("movies.csv")
# feed = movies["description"].fillna('') + movies["genre"].fillna('') + movies["director"].fillna('') + movies["stars"]

# tf = TfidfVectorizer(analyzer="word", ngram_range=(1, 2), min_df=0.0, stop_words="english")

# tfidf_matrix = tf.fit_transform(feed)

# with open('tfidf_matrix.pkl', 'wb') as f:
#     pickle.dump(tfidf_matrix, f)

with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

# tfidf_matrix = np.load("tfidf_matrix.npy", allow_pickle=True)

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
names = movies['name']
indices = pd.Series(movies.index, index=movies['name'])

def get_recommendations(liked_list): 
    if not liked_list: return []
    total_sim_scores = {}

    for idx in liked_list:
        sim_scores = cosine_sim[idx - 1]

        for i, score in enumerate(sim_scores):
            total_sim_scores[i] = total_sim_scores.get(i, 0.0) + score

    movie_indices = sorted(total_sim_scores, key=total_sim_scores.get, reverse=True)

    return movie_indices[len(liked_list):]

print(indices["The Godfather"])
print(names.iloc[get_recommendations([2])].head(20))