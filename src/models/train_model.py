from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import pickle


# Function to train the model
def train_cmodel(df):
    optimal_clusters = 5 
    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    
    kmeans.fit(df)
    
    with open('models/Kmodel.pkl', 'wb') as f:
        pickle.dump(kmeans, f)

    return kmeans, df

