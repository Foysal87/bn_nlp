from bn_nlp.tokenizer import wordTokenizer
from bn_nlp.preprocessing import ban_processing
from bn_nlp.Stemmer import stemmerOP
stemmer=stemmerOP()
tokenizer=wordTokenizer()
bp=ban_processing()
dict={}
class postag:
    def __init__(self):
        for word in open('bn_nlp/dataset/postag.txt','r'):
            word=word.replace('\n','')
            tokens=tokenizer.basic_tokenizer(word)
            wd=tokens[0]
            val=tokens[-1]
            dict[wd]=val

    def tag(self,sent):
        tokens=tokenizer.basic_tokenizer(sent)
        ans=[]
        for word in tokens:
            if dict.get(word):
               ans.append((word,dict[word]))
               continue
            word=stemmer.stem(word)
            if dict.get(word):
               ans.append((word,dict[word]))
               continue
            if dict.get(bp.word_normalize(word)):
                ans.append((word, dict[word]))
                continue
            ans.append((word,'unk'))
        return ans