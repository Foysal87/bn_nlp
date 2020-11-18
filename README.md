# bn_nlp
Bangla NLP toolkit.This is version 2.0(Another Version will come with a paper and higer data). You can use it now.

### what will you get here?

* [Bangla Preprocessing system](https://github.com/Foysal87/bn_nlp)
* [Bangla Text **Punctuation** Remove](https://github.com/Foysal87/bn_nlp#punctuation-remove)
* [Bangla **Stopword** removal](https://github.com/Foysal87/bn_nlp#stopword-removal)
* [Bangla Dust removal](https://github.com/Foysal87/bn_nlp#dust-removal) (without bangla character everything will be removed)
* [Bangla word Normalize](https://github.com/Foysal87/bn_nlp#word-normalize) (Less error form)
* [Bangla 'Bangla word to english equivalent word conversion'](https://github.com/Foysal87/bn_nlp#bangla-word-to-english-equivalent-word-conversion)
* [Bangla word **Sort** according to english alphabet](https://github.com/Foysal87/bn_nlp#bangla-word-sort-according-to-english-alphabet)
* [Bangla word **Sort** according to Bangla alphabet](https://github.com/Foysal87/bn_nlp#bangla-word-sort-according-to-bangla-alphabet)
* [Bangla Basic word **tokenizer**](https://github.com/Foysal87/bn_nlp#bangla-basic-word-tokenizer)
* [Bangla normalize word tokenizer](https://github.com/Foysal87/bn_nlp#bangla-normalize-word-tokenizer)
* [Bangla Basic Sentence tokenizer](https://github.com/Foysal87/bn_nlp#bangla-basic-sentence-tokenizer)
* [Bangla normalize **sentence tokenizer**](https://github.com/Foysal87/bn_nlp#bangla-normalize-sentence-tokenizer)
* [Bangla word **checker**](https://github.com/Foysal87/bn_nlp#bangla-word-checker) (word exist)
* [Bangla word **Stemmer**](https://github.com/Foysal87/bn_nlp#bangla-word-stemmer)(extended version of bnltk.stemmer & less error form & **higher accuracy** with word checker)
* [Bangla **word2vec** embedding](https://github.com/Foysal87/bn_nlp#bangla-word2vec-embedding)(7,00,000+ vocab, 100 Dimension, much accurate,pretrained) @pipilika
* [Bangla **sent2sent** embedding/similiarty](https://github.com/Foysal87/bn_nlp#bangla-sent2sent-embeddingsimiliarty-from-word2vec) from word2vec
* Bangla **Pos tagger**
* Bangla wiki and database related **NER**

### Required package(python 3.7)
* numpy
* scipy

### Punctuation Remove
```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
text="সড়কের ‘কারণে’ বৃহস্পতিবার দেখা গেল পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।"
print(bp.punctuation_remove(text))
```
**output**
```
সড়কের  কারণে  বৃহস্পতিবার দেখা গেল পুরো এলাকা  হাবুডুবু  খাচ্ছে অথৈ পানিতে 
```

### Stopword removal
Remove some constant word from sentence. you can find those word in 'stop_word.txt'.
```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
text="সড়কের ‘কারণে’ বৃহস্পতিবার দেখা গেল পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।"
print(bp.stop_word_remove(text))
```
**output**
```
সড়কের ‘কারণে’ বৃহস্পতিবার পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।
```
### Stopword add
Add word in stopword list
```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
text="সড়কের ‘কারণে’ বৃহস্পতিবার দেখা গেল পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।"
bp.add_stopword('সড়কের')
print(bp.stop_word_remove(text))
```
**output**
```
‘কারণে’ বৃহস্পতিবার পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।
```

### Dust Removal
Everything will remove from word with out bangla character
```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
text="সড়কের12A'--,.:Bকারণে"
print(bp.dust_removal(text))
```
**output**
```
সড়কেরকারণে
```

### Word Normalize
similar vowel defines same character for better accuracy.
```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
text="অসহনীয় ভারী বর্ষণে"
print(bp.word_normalize(text))
```
**output**
```
অসহনিয় ভারি বর্ষণে
```
### Bangla word to english equivalent word conversion

```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
text="রাজধানী"
print(bp.bn2enCon(text))
```
**output**
```
rajadhani
```

### Bangla word Sort according to english alphabet

```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
vec=['১', 'ঘণ্টার', 'ভারী' ,'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']
print(bp.bn_word_sort(vec))
```
**output**
```
['১', 'ভারী', 'বিভিন্ন', 'বর্ষণে', 'দেখা', 'দেয়', 'এলাকায়', 'ঘণ্টার', 'জলাবদ্ধতা', 'রাজধানীর', 'সোমবার']
```
### Bangla word Sort according to bangla alphabet

```py
from bn_nlp.preprocessing import ban_processing
bp=ban_processing()
vec=['১', 'ঘণ্টার', 'ভারী' ,'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']
print(bp.bn_word_sort_bn_sys(vec))
```
**output**
```
['এলাকায়', 'ঘণ্টার', 'জলাবদ্ধতা', 'দেখা', 'দেয়', 'বিভিন্ন', 'বর্ষণে', 'ভারী', 'রাজধানীর', 'সোমবার', '১']
```

### Bangla Basic word tokenizer

```py
from bn_nlp.tokenizer import wordTokenizer
wordtoken=wordTokenizer()
text="১ ঘণ্টার ভারী বর্ষণে সোমবার রাজধানীর বিভিন্ন এলাকায় জলাবদ্ধতা দেখা দেয়"
print(wordtoken.basic_tokenizer(text))
```
**output**
```
['১', 'ঘণ্টার', 'ভারী', 'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']
```
### Bangla Normalize word tokenizer

```py
from bn_nlp.tokenizer import wordTokenizer
wordtoken=wordTokenizer()
text="১ ঘণ্টার ভারী বর্ষণে সোমবার রাজধানীর বিভিন্ন এলাকায় জলাবদ্ধতা দেখা দেয়"
print(wordtoken.normalize_tokenizer(text))
```
**output**
```
['১', 'ঘণ্টার', 'ভারি', 'বর্ষণে', 'সোমবার', 'রাজধানির', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']
```
### Bangla Basic Sentence tokenizer

```py
from bn_nlp.tokenizer import sentenceTokenizer
senttoken=sentenceTokenizer()
text="ভোগান্তিতে পড়েন নগরবাসী। ব্যাহত হয় যান চলাচল। গতকাল সকালবেলা ছিল অসহনীয় গরম।"
print(senttoken.basic_tokenizer(text))
```
**output**
```
['ভোগান্তিতে পড়েন নগরবাসী', ' ব্যাহত হয় যান চলাচল', ' গতকাল সকালবেলা ছিল অসহনীয় গরম']
```
### Bangla Normalize Sentence tokenizer
No Dust. No punctuation. Normalize words.
```py
from bn_nlp.tokenizer import sentenceTokenizer
senttoken=sentenceTokenizer()
text="ভোগান্তিতে পড়েন নগরবাসী। ব্যাহত হয় যান চলাচল। গতকাল সকালবেলা ছিল অসহনীয় গরম।"
print(senttoken.basic_tokenizer(text))
```
**output**
```
['ভোগান্তিতে পড়েন নগরবাসি', 'ব্যাহত হয় যান চলাচল', 'গতকাল সকালবেলা ছিল অসহনিয় গরম']
```
### Bangla Word Checker
Is this word exist in bangla dictionary?
```py
from bn_nlp.Stemmer import stemmerOP
stemmer=stemmerOP()
text="ভোগান্তিতে"
print(stemmer.search(text))
```
**output**
```
True
```
### Bangla word Stemmer
finding root word.
```py
from bn_nlp.Stemmer import stemmerOP
stemmer=stemmerOP()
text="ভোগান্তিতে"
print(stemmer.stem(text))
text="ভোগান্তিতে পড়েন নগরবাসী"
print(stemmer.stemSent(text))
```
**output**
```
ভোগান্তি
ভোগান্তি পড় নগরবাসি
```

### Bangla word2vec embedding
**pretrained word2vec embedding download link**: <br/>
* [google Drive](https://drive.google.com/file/d/1aj8knLQ8H7O5nsb7wwNjq1-dQVLfEeA3/view?usp=sharing)
* [Pipilika Developer site](https://devlopers.pipilika.com/?fbclid=IwAR39VXgkWLoofm8Z03pyloPZTRV3ub7EAH9gRFM2UCgxIPiJJvzR1d_NPW0)

After downloading, paste this file in bn_nlp directory.
```py
from bn_nlp.word2vec_embedding import word2vec
w2v=word2vec()
text="বর্ষণে"
print(w2v.closure_word(text,5))
text2="বৃষ্টি"
print(w2v.dist(text,text2))
# you can get embedding vector by calling 'w2v.embedding_vec'
```
**output**
```
['বর্ষণে', 'বৃষ্টিপাতে', 'বৃষ্টিতে', 'কালবৈশাখী', 'জলোচ্ছ্বাসে']
26.64097023010254
```

### Bangla sent2sent embedding/similiarty from word2vec
Less value closure similarity. Built from word2vec. you can make embedding vector from similarity.
I directly implement dist, cause we basically need distance.
```py
from bn_nlp.sent2sent_embedding import sent2sent
s2s=sent2sent()
text1="আমি ভাত খাই"
text2="আমি পাস্তা খেতে চাই"
print(s2s.dist(text1,text2))
# 'sent2sent_dist' function takes vector and gives 2D array with every sent to other sent dist
```
**output**
```
37.503074645996094
```

**Thank you** <br/>
**Let's make better resources for Bangla**
