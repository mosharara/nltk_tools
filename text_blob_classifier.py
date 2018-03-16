
import textblob
from textblob.classifiers import NaiveBayesClassifier
















with open('final.json', 'r') as fp:
   cl = NaiveBayesClassifier(fp, format="json")
