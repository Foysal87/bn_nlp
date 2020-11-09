from tokenizer import wordTokenizer,sentenceTokenizer
from word2vec_embedding import word2vec
import math

w2v = word2vec()
token = wordTokenizer()

class sent2sent:

    def __init__(self):
        pass
    def dist(self,sent1,sent2):
        tokens1=token.normalize_tokenizer(sent1)
        tokens2=token.normalize_tokenizer(sent2)
        d=0
        for i in tokens1:
            mn=math.inf
            for j in tokens2:
                mn=min(mn,w2v.dist(i,j))
            d+=mn
        return d
    def sent2sent_dist(self,vec):
        ans=[]
        mx=0
        for sent1 in vec:
            temp=[]
            for sent2 in vec:
                temp.append(self.dist(sent1,sent2))
                mx=max(mx,self.dist(sent1,sent2))
            ans.append(temp)
        temp_ans=[]
        mx+=1.0
        for i in ans:
            temp=[]
            for j in i:
                temp.append((mx/(j+1.0)))
            temp_ans.append(temp)
        return temp_ans