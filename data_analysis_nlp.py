
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords



from nltk.tokenize.punkt import PunktSentenceTokenizer




    
f = open('paypal.txt')
raw = f.read()



stop = set(stopwords.words('english'))


tokens = word_tokenize(raw)


def lexical_diversity(raw): # its so low 

    return len(set(raw)) / len(raw)




    

def content_fraction(raw):
    ## this will show how many words are not stop words in the documen 
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in raw if w.lower() not in stopwords]
    return len(content) / len(raw)



def frequency_dist(raw):
    stopwords = nltk.corpus.stopwords.words('english')
    extra = ','
    tokens = word_tokenize(raw)
    cleaned = [w for w in tokens if w.lower() not in stopwords and extra]
    fdist = nltk.FreqDist(cleaned)

    common_words = []

    common_words.append(fdist.most_common(200))

    ## fdist.max()
    ## fdist.plot()
    ## fdist1 < fdist2 

    return common_words
    
    
def dispersion(raw):

    ## plot the most freqwords
    return raw.dispersion_plot(common_words)






## to test against another file


## we get two text files , first lets say payapl related words and the other
## is all of the stop words


    ## male = names.words('')
    ## female = names.words('')


    ## [w for w in malle of w in female]


    
    

    
    
## dump an array into csv

## import numpy
## a = numpy.asarray(arra_name)
## numpy.savetxt("foo.csv", a, delimiter=",")






    












    



    
