# layer 1:


from textblob import TextBlob
import spacy
import numpy as np
import matplotlib.pyplot as plt







class sentiment:


   


    def __init__(self,sent, delta_sent):

        self.sent = sent
        self.delta_sent = delta_sent




    def sentim(str):

        clause = str
        clause = TextBlob(str)
        ## cant find the semantic meaning of tokenized words ???
        re = clause.sentiment
        re_1 = clause.sentiment.polarity

        
        
        
       
        return ("sentiment and polarity: " , re_1 ,"sentiment :", re)


    
        

    def results(str):

         blob = str
         blob = TextBlob(str)
            


         if blob.sentiment.polarity < 0:
                sentiment = "negative"
                return sentiment
                
         elif blob.sentiment.polarity == 0:
                sentiment = "neutral"
                return sentiment
                
         else:
                sentiment = "positive"
                return sentiment

                

class delta_sentiment:








    def word_tokenizer(str):


         blob = str
         blob = TextBlob(str)


         tokenized = blob.sentences


         
         sent_sentiment = []

         for line in text:

                values = tokenized.sentiment.polarity
                sent_sentiment.append(values) ## we need to make it go through all the text 

             

            


             


##    def calculation(sent_sentiment):
##
##
##        [for i in sent_sentiment n+1 - n ]


        ## this will output antoher array of the len of n-1, now for this array it is the y axis
        ## need to plot the x-axis which is time steps for every sentene

        ## vector format __> going to matrix format

        ## run the math to find the angle between two vectors

        ##eate an array that stroes all angles of length of n-2

        ## now go to every cosqent n, and n+1

        ## and calculate the following :


        ## deltatheta final - deltatheta intital

        ## store them in a final array

        ## map it on y axis ,x axis time stes

        ## find the linear fit which will dictates the behaviour on time, 

        

         

    


    ## we need to graph the vector of every word using 1 time step


    def draw_vector(arr):
    
        soa = np.array(arr) ## should be multidimensional array
        X, Y, U, V = zip(*soa)
        plt.figure()
        ax = plt.gca()
        ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
        ax.set_xlim([-1, 10])
        ax.set_ylim([-1, 10])
        plt.draw()
        plt.show()
            


## although there are some words that are neutral in normal conversations, however that word could be meaning something else, in,        ## a specific area, like (wet) for a jaket that supposed to isolate the rain.

        ## this will be trained through a speical lexicon , given by the buisness


        ## we shall train a special text classfier for this alone.
    
