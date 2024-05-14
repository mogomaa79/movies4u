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
    """Uses Nearest Neighbor Algorithm to Recommend Movies"""
    if not liked_list: return []
    similars = set()
    
    for idx in liked_list:
        similars.update(nn.kneighbors([embeddings[idx - 1]], n_neighbors=10, return_distance=False)[0])

    # Future Design Planned
    return list(similars - set([l - 1 for l in liked_list]))