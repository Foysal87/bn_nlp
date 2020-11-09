import numpy as np
from scipy import spatial
path = "word2vec_model.txt"
embeddings_dict = {}
class word2vec:
    def __init__(self):
        with open(path, 'r') as f:
            for l in f:
                values = l.split()
                word = str(values[0])
                vec = np.asarray(values[1:], "float32")
                embeddings_dict[word] = vec
    def embedding_vec(self,word):
        if word in embeddings_dict:
           return embeddings_dict[word]
        return np.zeros(100)
    def dist(self,word1,word2):
        vec1=np.zeros(100)
        vec2=np.zeros(100)
        if word1 in embeddings_dict:
            vec1=embeddings_dict[word1]
        if word2 in embeddings_dict:
            vec2=embeddings_dict[word2]
        d = spatial.distance.euclidean(vec1,vec2)
        return d
    def closure_word(self,item,n):
        vec = []
        if item not in embeddings_dict:
            vec.append(item)
            return vec
        result=sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embeddings_dict[item]))

        j=0
        for i in result:
           if j==n:
             break
           vec.append(i)
           j+=1

        return vec

