from preprocessing import ban_processing,StaticArray
from tokenizer import wordTokenizer
from bnltk.stemmer import BanglaStemmer
bn_stemmer = BanglaStemmer()
wordtokens=wordTokenizer()
word_vec=[]
word_dict={}
bp=ban_processing()
class stemmerOP:
    def __init__(self):
        for word in open("word2.txt", "r"):
            word=word.replace('\n','')
            word_vec.append(word)
            word_dict[word]=1
    def search(self,word):
        if bp.word_normalize(word) in word_dict:
            return True
        return False
    def stem_normalize(self,word):
        g = word[-1].encode("unicode_escape")
        g = g.upper()
        g = g[2:]
        g = g.decode('utf-8')
        if g in StaticArray.bn2enSuffix:
            word=word[:-1]
        return word

    def stem(self,word):
        new_word=bn_stemmer.stem(word)
        if new_word==word:
            new_word = self.stem_normalize(word)
            if self.search(new_word):
                return new_word
        else:
            if self.search(new_word):
                return new_word
            new_word= self.stem_normalize(word)
            if self.search(new_word):
                return new_word
        return word

    def stemSent(self,sent):

        tokens=wordtokens.normalize_tokenizer(sent)
        temp_tokens=[]
        for i in tokens:
            temp_tokens.append(self.stem(i))
        result = ' '.join(temp_tokens)

        return result




