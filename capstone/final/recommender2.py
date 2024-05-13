import pandas as pd
import pickle
import tensorflow_hub as hub
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
import numpy as np

movies = pd.read_csv("capstone/movies.csv")
feed = movies["name"].fillna('') + movies["description"].fillna('')  
#+ movies["genre"].fillna('') # + movies["director"].fillna('') + movies["stars"]

#preprocessor = hub.KerasLayer(
#    "https://kaggle.com/models/tensorflow/bert/TensorFlow2/en-uncased-preprocess/3")

#embed = hub.load("https://www.kaggle.com/models/google/universal-sentence-encoder/TensorFlow2/universal-sentence-encoder/2")
#tf.saved_model.save(embed, 'universal_sentence_encoder')

#embeddings = embed(feed)
#embeddings = np.array(embeddings)

# with open('capstone/embeddings.pkl', 'wb') as f:
#     pickle.dump(embeddings, f)

#nn = NearestNeighbors(n_jobs = -1, n_neighbors=9999)
#nn.fit(embeddings)

#with open('capstone/recommender_model.pkl', 'wb') as f:
#    pickle.dump(nn, f)

embed = hub.KerasLayer("capstone/universal_sentence_encoder/") 

with open('capstone/embeddings.pkl', 'rb') as f:
    embeddings = pickle.load(f)

with open('capstone/recommender_model.pkl', 'rb') as f:
    nn = pickle.load(f)

def get_recommendations(liked_list:list) -> list:
    if not liked_list: return []
    total_sim_scores = {}
    
    for idx in liked_list:
        similars = nn.kneighbors([embeddings[idx-1]], return_distance=False)[0]

        for i in similars:
            total_sim_scores[i] = total_sim_scores.get(i, 0.0) + 1

    movie_indices = sorted(total_sim_scores, key=total_sim_scores.get, reverse=True)
    
    return movie_indices

def search(text:str) -> list:
    emb = embed([text])
    return nn.kneighbors(emb, return_distance=False)[0]


