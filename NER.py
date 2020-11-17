import requests
import math
import operator
from bs4 import BeautifulSoup
from bn_nlp.tokenizer import wordTokenizer
from bn_nlp.Stemmer import stemmerOP
from bn_nlp.word2vec_embedding import word2vec
from bn_nlp.preprocessing import ban_processing

index=['স্থান','অর্থ','ব্যক্তি','শহর','দেশ']
bp=ban_processing()
stemmer=stemmerOP()
tokenizer=wordTokenizer()
w2v=word2vec()

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
                exData[tmp] = tokens[val]
        for word in open('bn_nlp/dataset/word3.txt'):
            word = word.replace('\n', '')
            pos_dict[word] = 1
    def gett(self,qr):
        print(qr)
        query=stemmer.stemSent(qr)
        if exData.get(query)!=None:
            return exData.get(query)
        query = query.replace(' ', '+')
        URL = f"https://bn.wikipedia.org/w/index.php?search={query}&title=বিশেষ:অনুসন্ধান&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"

        resp = requests.get(URL)
        results = []
        ans = ""
        cnt=0
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            for g in soup.find_all('div', class_='mw-search-result-heading'):
                anchors = g.find_all('a')
                if anchors:
                    link = anchors[0]['href']
                    title = anchors[0][('title')]
                    if stemmer.stemSent(qr) in title:
                        cnt+=1
                        if cnt>3:
                            break
                        item = {
                            "title": title,
                            "link": link
                        }
                        results.append(item)
        for a in results:
            url = f"https://bn.wikipedia.org/{a['link']}"

            resp = requests.get(url)
            if resp.status_code == 200:
                sop = BeautifulSoup(resp.content, "html.parser")
                for g in sop.find_all('p'):
                    g = g.text.replace('\n', '')
                    if g:
                        ans += g + ' '
        if len(ans)==0:
            return 0
        ans=stemmer.stemSent(ans)
        ans=bp.stop_word_remove(ans)
        tokens=tokenizer.basic_tokenizer(ans)
        temp_dict={}
        for i in tokens:
            if temp_dict.get(i)==None:
                temp_dict[i]=1
                continue
            temp_dict[i]+=1
        A = dict(sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True)[:20])
        mn=math.inf
        ind=-1
        cn=0
        for i in index:
            sum=0
            vec=w2v.closure_word(i,20)
            for j in vec:
                for k in A:
                    sum+=(w2v.dist(j,k))*(1.0/(A[k]*1.0))
            if sum<mn:
                mn=sum
                ind=cn
            cn+=1
        return ind+1


    def NER(self,sent):
        tokens = tokenizer.basic_tokenizer(sent)
        i=0
        dict={}
        while(i<len(tokens)):
            if pos_dict.get(stemmer.stem(tokens[i]))!=None:
                i+=1
                continue
            j=len(tokens)-1
            ind=-1
            while(j>=i):
                k=i
                query=""
                while(k<j):
                    query+=stemmer.stem(bp.word_normalize(tokens[k]))+' '
                    k+=1
                query+=tokens[k]
                q=self.gett(query)
                if q!=0:
                    dict[query]=index[q-1]
                    ind=j
                    break
                j-=1
                if ind!=-1:
                    break
            if ind!=-1:
                i=ind+1
                continue
            i=i+1
        return dict












