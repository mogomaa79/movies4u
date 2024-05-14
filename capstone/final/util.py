from django.conf import settings
import os
import pickle

# Construct the file paths using os.path.join() and settings.BASE_DIR
embeddings_path = os.path.join(settings.BASE_DIR, 'final', 'static', 'final','embeddings.pkl')
model_path = os.path.join(settings.BASE_DIR, 'final', 'static', 'final','recommender_model.pkl')

# Open the files
with open(embeddings_path, 'rb') as f:
    embeddings = pickle.load(f)

with open(model_path, 'rb') as f:
    nn = pickle.load(f)


def get_recommendations(liked_list:list) -> list:
    if not liked_list: return []
    total_sim_scores = {}
    
    for idx in liked_list:
        similars = nn.kneighbors([embeddings[idx - 1]], n_neighbors=500, return_distance=False)[0]

        for i in similars:
            total_sim_scores[i] = total_sim_scores.get(i, 0.0) + 1

    movie_indices = sorted(total_sim_scores, key=total_sim_scores.get, reverse=True)
    
    return [m + 1 for m in movie_indices][len(liked_list):]