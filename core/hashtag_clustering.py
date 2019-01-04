from gensim.models import Word2Vec
from nltk.cluster import KMeansClusterer
import nltk
import json
import sys

class hashtag_clustering():

    def clustering(self, modelpath, hashtag_cluster_path, num_clusters):

        #loading word2vec model
        model = Word2Vec.load(modelpath)
        X = model.wv.vectors

        #clustering
        num_clusters = int(num_clusters)
        kclusterer = KMeansClusterer(num_clusters, distance=nltk.cluster.util.cosine_distance, repeats=25)
        assigned_clusters = kclusterer.cluster(X, assign_clusters=True)

        #distributing hashtags into their respective clusters
        words = list(model.wv.vocab)
        cluster_distribution = {}
        for i, word in enumerate(words):
            try:
                cluster_distribution[str(assigned_clusters[i])].append(word)
            except:
                cluster_distribution[str(assigned_clusters[i])] = []
                cluster_distribution[str(assigned_clusters[i])].append(word)

        #save the cluster distribution
        with open(hashtag_cluster_path, "w") as write_file:
            json.dump(cluster_distribution, write_file)
        print('saved hashtag cluster.')

if __name__ == '__main__':
    object = hashtag_clustering()
    object.clustering(sys.argv[1], sys.argv[2], sys.argv[3])
