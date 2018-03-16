import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import random
import pickle
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation




stopwords = nltk.corpus.stopwords.words('english')


lemmatizer = WordNetLemmatizer()
hm_lines = 100000


pos = 'pos.txt'
neg = 'neg.txt'

num = list(range(0, 100))
char = list(set(punctuation))


lexicon = []
with open(pos,'r') as f:
        contents = f.readlines()
        for l in contents[:hm_lines]:
                all_words = word_tokenize(l)
                lexicon += list(all_words)

with open(neg,'r') as f:
        contents = f.readlines()
        for l in contents[:hm_lines]:
                all_words = word_tokenize(l)
                lexicon += list(all_words)

lexicon = [lemmatizer.lemmatize(i) for i in lexicon]
w_counts = Counter(lexicon)

l2 = []
for w in w_counts:
        #print(w_counts[w])
        if 1000 > w_counts[w] > 3 and w not in stopwords and w not in str(num) and w not in str(char) and len(w) > 2:
                l2.append(w)
               # print(len(l2))

for i in l2:
        print(i)



with open('test.pickle','wb') as f:
	pickle.dump(l2[0:hm_lines],f)

        
        


        

                


	



