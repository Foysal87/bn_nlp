import re
import functools

class StaticArray:
    bn2en={'0985':'a','0986':'aa','0987':'i','0988':'ii',
           '0989':'u','098A':'uu','098B':'r','09E0':'rr',
           '098C':'l','09E1':'ll','098F':'e','0990':'ai',
           '0993':'o','0994':'au',
           '0995':'ka','0996':'kha','0997':'ga','0998':'gha',
           '0999':'nga','099A':'ca','099B':'cha','099C':'ja',
           '099D':'jha','099E':'nya','099F':'tta', '09A0':'ttha',
           '09A1':'dda','09DC':'rra','09A2':'ddha','09DD':'rha',
           '09A3':'nna','09A4':'ta','09A5':'tha','09A6':'da',
           '09A7':'dha','09A8':'na','09AA':'pa','09AB':'pha',
           '09AC':'ba','09AD':'bha','09AE':'ma','09AF':'ya',
           '09DF':'yya','09B0':'ra','09B2':'la','09B6':'sha',
           '09B7':'ssa','09B8':'sa','09B9':'ha','09CE':'ta',
           '09BE':'aa','09BF':'i','09C0':'ii','09C1':'u',
           '09C2':'uu','09C3':'r','09C4':'rr','09C7':'e',
           '09C8':'ai', '09CB':'o','09CC':'au',
           '09CD':'','09D7':'','09E6':'0',
           '09E7':'1','09E8':'2','09E9':'3','09EA':'4',
           '09EB':'5','09EC':'6','09ED':'7','09EE':'8',
           '09EF':'9',
           '09BC':'','0982':'n','0983':'','0981':''
           }
    bn2enNum={
        '09E6': '0',
        '09E7': '1', '09E8': '2', '09E9': '3', '09EA': '4',
        '09EB': '5', '09EC': '6', '09ED': '7', '09EE': '8',
        '09EF': '9'
    }
    bn2enPunc={
        '09BE': 'a', '09BF': 'i', '09C0': 'i', '09C1': 'u',
        '09C2': 'u', '09C3': 'r', '09C4': 'r', '09C7': 'e',
        '09C8': 'ai', '09CB': 'o', '09CC': 'au','09B0':'ra'
    }
    bn2enSuffix={
        '09BE': 'a', '09B0':'ra','09CB': 'o','0993':'o','09C7': 'e'
    }
    bn_norm={
        '09C0':'\u09bf','09C2':'\u09c1','09C4':'\u09c3','09A3':'\u09a8','0988':'\u0987','098A':'\u0989'
    }

    bn_serial={
        '0985': 0, '0986': 1, '09BE': 2, '0987': 3, '09BF': 4,'0988': 5, '09C0': 6,
        '0989': 7, '09C1': 8, '098A': 9, '09C2': 10,'098B': 11,'09C3': 12, '09E0': 13,'09C4': 14,
        '098C': 15, '09E1': 16, '098F': 17,  '09C7': 18, '0990': 19,'09C8': 20,
        '0993': 21, '09CB': 22, '0994': 23, '09CC': 24,
        '0995': 25, '0996': 26, '0997': 27, '0998': 28,
        '0999': 29, '099A': 30, '099B': 31, '099C': 32,
        '099D': 33, '099E': 34, '099F': 35, '09A0': 36,
        '09A1': 37, '09DC': 38, '09A2': 39, '09DD': 40,
        '09A3': 41, '09A4': 42, '09A5': 43, '09A6': 44,
        '09A7': 45, '09A8': 46, '09AA': 47, '09AB': 48,
        '09AC': 49, '09AD': 50, '09AE': 51, '09AF': 52,
        '09DF': 53, '09B0': 54, '09B2': 55, '09B6': 56,
        '09B7': 57, '09B8': 58, '09B9': 59, '09CE': 60,
        '09E6': 61,
        '09E7': 62, '09E8': 63, '09E9': 64, '09EA': 65,
        '09EB': 66, '09EC': 67, '09ED': 68, '09EE': 69,
        '09EF': 70,
        '09CD': 71, '09D7': 72,
        '09BC': 73, '0982': 74, '0983': 75, '0981': 76
    }

class ban_processing:

    def punctuation_remove(self,text):
        whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
        bangla_fullstop = u"\u0964"
        punctSeq = u"['\"“”‘’]+|[.?!,…]+|[:;]+"
        punc = u"[(),$%^&*+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
        text = whitespace.sub(" ", text).strip()
        text = re.sub(punctSeq, " ", text)
        text = re.sub(bangla_fullstop, " ", text)
        text = re.sub(punc, " ", text)
        text = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', ' ', text)
        text=text.replace("\\", " ")
        return text

    def dust_removal(self,word):
        s=""
        for c in word:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g in StaticArray.bn2en:
                s+=c
        return s


    def stop_word_remove(self,text):
        stopwords = []
        for i in open("bn_nlp/dataset/stop_word.txt", "r"):
            i = i.rstrip("\n")
            stopwords.append(i)
        querywords = text.split()
        resultwords = [word for word in querywords if word not in stopwords]
        result = ' '.join(resultwords)
        return result

    def add_stopword(self,text):
        stopwords = []
        for i in open("bn_nlp/dataset/stop_word.txt", "r"):
            i = i.rstrip("\n")
            stopwords.append(i)
        stopwords.append(text)
        file=open("bn_nlp/dataset/stop_word.txt", "wb")
        for i in stopwords:
            i=i+'\n'
            file.write(i.encode('utf8'))
        file.close()

    def remove_stopword(selfself,text):
        stopwords = []
        for i in open("bn_nlp/dataset/stop_word.txt", "r"):
            i = i.rstrip("\n")
            stopwords.append(i)
        file = open("bn_nlp/dataset/stop_word.txt", "wb")
        for i in stopwords:
            if i==text:
                continue
            i = i + '\n'
            file.write(i.encode('utf8'))
        file.close()

    def last_num_remove(self,word):
        if len(word)==0:
            return word
        c=word[0]
        g = c.encode("unicode_escape")
        g = g.upper()
        g = g[2:]
        g = g.decode('utf-8')
        if g in StaticArray.bn2enNum:
            return word
        while True:
            c=word[-1]
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g in StaticArray.bn2enNum:
                word=word[:-1]
                continue
            break
        return word

    def word_normalize(self,word):
        s = ""
        for c in word:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g in StaticArray.bn_norm:
                g = StaticArray.bn_norm[g].encode().decode('utf-8')
                s+=g
                continue
            s+=c
        return s

    def bn2enCon(self,word):
        s=""
        for c in word:
            g=c.encode("unicode_escape")
            g=g.upper()
            g=g[2:]
            g=g.decode('utf-8')
            if g in StaticArray.bn2enPunc:
                if len(s)>0 and s[-1]=='a':
                    s=s[:-1]
                s+=StaticArray.bn2enPunc[g]
                continue
            if g in StaticArray.bn2en:
                s+=StaticArray.bn2en[g]
        return s

    def bnCompare(self,item1,item2):
        g1=self.bn2enCon(item1)
        g2=self.bn2enCon(item2)
        return (g1 > g2) - (g1 < g2)

    def isBan(self,word):
        for c in word:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g in StaticArray.bn2en:
                return True
        return False

    def bn_word_sort(self,vec):
        temp_vec=[]
        for i in vec:
            if self.isBan(i):
              i=self.dust_removal(i)
              temp_vec.append(self.punctuation_remove(i).replace(' ',''))
        vec=list(set(temp_vec))
        vec=sorted(vec,key=functools.cmp_to_key(self.bnCompare))
        return vec

    def bnCompare2(self,item1,item2):
        ln=min(len(item1),len(item2))
        for i in range(ln):
            if item1[i]==item2[i]:
                continue
            g1 = item1[i].encode("unicode_escape")
            g1 = g1.upper()
            g1 = g1[2:]
            g1 = g1.decode('utf-8')
            g1=StaticArray.bn_serial[g1]
            g2 = item2[i].encode("unicode_escape")
            g2 = g2.upper()
            g2 = g2[2:]
            g2 = g2.decode('utf-8')
            g2=StaticArray.bn_serial[g2]
            return (g1>g2) -(g1<g2)
        return (len(item1)>len(item2))-(len(item1)<len(item2))
    def bn_word_sort_bn_sys(self,vec):
        temp_vec = []
        for i in vec:
            if self.isBan(i):
                i = self.dust_removal(i)
                temp_vec.append(self.punctuation_remove(i).replace(' ', ''))
        vec = list(set(temp_vec))
        vec = sorted(vec, key=functools.cmp_to_key(self.bnCompare2))
        return vec




