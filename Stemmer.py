from bn_nlp.preprocessing import ban_processing,StaticArray
from bn_nlp.tokenizer import wordTokenizer
import functools
import re
import string
wordtokens=wordTokenizer()
word_vec=[]
word_dict={}
bp=ban_processing()
rule_words = ['ই', 'ও', 'তো', 'কে', 'তে', 'রা', 'চ্ছি', 'চ্ছিল', 'চ্ছে', 'চ্ছিস', 'চ্ছিলেন', 'চ্ছ', 'য়েছে', 'েছ', 'েছে',
              'েছেন', 'রছ', 'রব', 'েল', 'েলো', 'ওয়া', 'েয়ে', 'য়', 'য়ে', 'েয়েছিল', 'েছিল', 'য়েছিল', 'েয়েছিলেন',
              'ে.েছিলেন', 'েছিলেন', 'লেন', 'দের', 'ে.ে', 'ের', 'ার', 'েন', 'বেন', 'িস', 'ছিস', 'ছিলি', 'ছি', 'ছে', 'লি',
              'বি', 'ে', 'টি', 'টির', 'েরটা', 'েরটার', 'টা', 'টার', 'গুলো', 'গুলোর', 'েরগুলো', 'েরগুলোর'
              'যোগ্য','কেই','েও','সহ','রা','ভাবে','কারি','কৃত','ই','কে','র','কি','েই','ভাবে','গুলো',
              'তে','েতে','গন','মুলক','সুচক','টুকু','টুকুই','গুলি','পদ','সমুহ','সংক্রান্ত','সংলগ্ন','সংশ্লিষ্ট',
              'সুত্রে','রুপে','ানুসারে','ানুযায়ি','তত্ত্','ি','মুখি','প্রতি','ভাবে'
              ]
rule_dict = {"রছ":"র","রব":"র","েয়ে":"া","েয়েছিল":"া","েয়েছিলেন":"া","ে.েছিলেন":"া.","ে.ে":"া."}


class stemmerOP:
    def __init__(self):
        for word in open("bn_nlp/word2.txt", "r"):
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
    def bnCompare(self,item1,item2):
        return (len(item1)>len(item2))-(len(item1)<len(item2))

    def stem(self,word):
        suf_arr=[]
        for wd in rule_words:
            if re.search('.*' + wd + '$', word):
                suf_arr.append(wd)
        suf_arr = sorted(suf_arr, key=functools.cmp_to_key(self.bnCompare))

        if len(suf_arr)>0:
            for i in suf_arr:
                if i in rule_dict:
                    ind = len(word) - len(i)
                    new_word=word[0:ind]+rule_dict[i]
                    if self.search(new_word):
                        return new_word
                else:
                    ind = len(word) - len(i)
                    new_word = word[0:ind]
                    if len(new_word)==0:
                        return word
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
