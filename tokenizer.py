from preprocessing import ban_processing,StaticArray
bp=ban_processing()
class wordTokenizer:
    def basic_tokenizer(self,sent):
        sent=bp.punctuation_remove(sent)
        tokens = sent.split()
        temp_tokens = []
        for i in tokens:
            if len(bp.dust_removal(i)) == 0:
                continue
            temp_tokens.append(i)
        return temp_tokens

    def normalize_tokenizer(self,sent):
        sent=bp.word_normalize(sent)
        tokens=sent.split()
        temp_tokens=[]
        for i in tokens:
            if len(bp.dust_removal(i))==0:
                continue
            i=bp.dust_removal(i)
            temp_tokens.append(i)
        return temp_tokens

class sentenceTokenizer:

    def basic_tokenizer(self,text):
        text=text.replace('\n',' ')
        tokens = []
        s = ""
        bangla_fullstop = '0964'
        for c in text:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g == bangla_fullstop:
                tokens.append(s)
                s = ""
                continue
            s += c
        if len(s) > 0:
            tokens.append(s)
        temp_tokens = []
        for i in tokens:
            if len(bp.dust_removal(i))==0:
                continue

            temp_tokens.append(i)
        return temp_tokens

    def normalize_tokenizer(self,text):
        tokens=[]
        text = text.replace('\n', ' ')
        s=""
        bangla_fullstop = '0964'
        for c in text:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g==bangla_fullstop:
                tokens.append(s)
                s=""
                continue
            s+=c
        if len(s)>0:
            tokens.append(s)
        temp_tokens=[]
        for i in tokens:
            if len(bp.dust_removal(i))==0:
                continue
            i=bp.punctuation_remove(i)
            temp_tokens.append(i)
        return temp_tokens



