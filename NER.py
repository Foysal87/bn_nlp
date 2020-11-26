
from tokenizer import wordTokenizer
from preprocessing import ban_processing

bp=ban_processing()
tokenizer=wordTokenizer()
exData={}
pos_dict={}
class UncustomizeNER:
    def __init__(self):
        for word in open('bn_nlp/dataset/exdata.txt', 'r'):
            word=word.replace('\n','')
            tokens=tokenizer.basic_tokenizer(word)
            if len(tokens)>=2:
                val=tokens[-1]
                ind=len(word)-len(val)
                tmp=word[0:ind-1]
                exData[tmp] = val
    def NER(self,text):
        i=0
        tokens=tokenizer.basic_tokenizer(text)
        l=len(tokens)
        ans={}
        while i<l:
            j=min(i+10,l-1);
            while j>i:
                st=' '.join(tokens[i:j])
                print(st)
                if exData.get(st):
                    ans[st]=exData[st]
                    break
                j-=1
            if j==i:
                j+=1
            i=j
        return ans












