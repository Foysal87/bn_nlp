from bn_nlp.preprocessing import ban_processing
from bn_nlp.tokenizer import wordTokenizer
from bn_nlp.tokenizer import sentenceTokenizer
from bn_nlp.Stemmer import stemmerOP
from bn_nlp.word2vec_embedding import word2vec
from bn_nlp.sent2sent_embedding import sent2sent
from bn_nlp.posTag import postag
from bn_nlp.NER import UncustomizeNER
bp=ban_processing()
# punctuation Remove
text="সড়কের ‘কারণে’ বৃহস্পতিবার দেখা গেল পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।"
print(bp.punctuation_remove(text))

#stopWord remove from text
print(bp.stop_word_remove(text))

# add a stopword in stopword list (try to call stemmer sentence)
bp.add_stopword('সড়কের')
print(bp.stop_word_remove(text))

#remove a stopword from stopword list
bp.remove_stopword('সড়কের')
print(bp.stop_word_remove(text))

#Dust removal
text="সড়কের12A'--,.:Bকারণে"
print(bp.dust_removal(text))

#word Normalize
text="অসহনীয় ভারী বর্ষণে"
print(bp.word_normalize(text))

# Bangla to english conversion
text="রাজধানী"
print(bp.bn2enCon(text))

# sort according to english alphabet
vec=['১', 'ঘণ্টার', 'ভারী' ,'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']
print(bp.bn_word_sort(vec))

#sort according to Bangla alphabet
vec=['১', 'ঘণ্টার', 'ভারী' ,'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']
print(bp.bn_word_sort_bn_sys(vec))

#word tokenize (Basic)
wordtoken=wordTokenizer()
text="১ ঘণ্টার ভারী বর্ষণে সোমবার রাজধানীর বিভিন্ন এলাকায় জলাবদ্ধতা দেখা দেয়"
print(wordtoken.basic_tokenizer(text))

#word tokenize (Normalize)
text="১ ঘণ্টার ভারী বর্ষণে সোমবার রাজধানীর বিভিন্ন এলাকায় জলাবদ্ধতা দেখা দেয়"
print(wordtoken.normalize_tokenizer(text))

#Sentence tokenize(Basic)
senttoken=sentenceTokenizer()
text="ভোগান্তিতে পড়েন নগরবাসী। ব্যাহত হয় যান চলাচল। গতকাল সকালবেলা ছিল অসহনীয় গরম।"
print(senttoken.basic_tokenizer(text))

#sentence tokenize(Normalize)
text="ভোগান্তিতে পড়েন নগরবাসী। ব্যাহত হয় যান চলাচল। গতকাল সকালবেলা ছিল অসহনীয় গরম।"
print(senttoken.basic_tokenizer(text))

#Find a word in the bangla dictionary
stemmer=stemmerOP()
text="ভোগান্তিতে"
print(stemmer.search(text))

#stem a word
text="ভোগান্তিতে"
print(stemmer.stem(text))
text="সড়কের ভোগান্তিতে পড়েন নগরবাসী"
print(stemmer.stemSent(text))

#word embedding
w2v=word2vec()
text="বর্ষণে"
print(w2v.closure_word(text,5))
text2="বৃষ্টি"
print(w2v.dist(text,text2))

#sentence embedding
s2s=sent2sent()
text1="আমি ভাত খাই"
text2="আমি পাস্তা খেতে চাই"
print(s2s.dist(text1,text2))

#Pos tagger
tagger=postag()
text="সড়কের ‘কারণে’ বৃহস্পতিবার দেখা গেল পুরো এলাকা ‘হাবুডুবু’ খাচ্ছে অথৈ পানিতে।"
print(tagger.tag(text))

#NER
ner=UncustomizeNER()
text="বাংলাদেশ দক্ষিণ এশিয়ার একটি রাষ্ট্র। দেশটির উত্তর, পূর্ব ও পশ্চিম সীমানায় ভারত ও দক্ষিণ-পূর্ব সীমানায় মায়ানমার"
print(ner.NER(text))

