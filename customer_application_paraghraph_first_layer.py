from __future__ import division
import nltk
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import numpy as np
import matplotlib.pyplot as plt

import re, pprint





f = open('para.txt', 'rU')










def fd(str):
    
      sentence =  (str.strip())
      tokenized_words = [w.lower() for w in nltk.word_tokenize(sentence)]
      fd = nltk.FreqDist(tokenized_words)

      return fd



def ie_preprocess(str):

     sentences = nltk.sent_tokenize(str)
     sentences = [nltk.word_tokenize(sent) for sent in sentences]
     sentences = [nltk.pos_tag(sent) for sent in sentences]
     namedEnt = nltk.ne_chunk(sentences, binary=True)
     

     return namedEnt



def process_content():
    
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()








            
    





    

    

            
            
