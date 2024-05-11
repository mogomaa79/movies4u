import pickle
from sklearn.metrics.pairwise import linear_kernel

# with open("static/final/tfidf_matrix.pkl", "rb") as f:
#     tfidf_matrix = pickle.load(f)

# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# def get_recommendations(liked_list):
#     if not liked_list: return []
#     total_sim_scores = {}

#     for idx in liked_list:
#         sim_scores = cosine_sim[idx]

#         for i, score in enumerate(sim_scores):
#             total_sim_scores[i] = total_sim_scores.get(i, 0.0) + score

#     movie_indices = sorted(total_sim_scores, key=total_sim_scores.get, reverse=True)

#     return movie_indices[len(liked_list):]