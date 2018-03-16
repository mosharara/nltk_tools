
import textblob


from textblob.classifiers import NaiveBayesClassifier

import json




with open('train.json') as json_file:
    obj = json.load(json_file)
    cl = NaiveBayesClassifier(obj, format="json")


