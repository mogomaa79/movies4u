import pandas
from recommender2 import movies, get_recommendations,embeddings,search
import numpy as np

watched_list = [12,1]
#print(embeddings[11])


#print(movies.iloc[get_recommendations(watched_list), 1])

print(movies.iloc[search("john wick"), 1])