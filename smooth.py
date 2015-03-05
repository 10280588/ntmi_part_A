from __future__ import division

class Smooth():
    def add1(self, ngram):
        smoothedNgram = {key: value+1 for (key, value) in ngram.iteritems()}
        return smoothedNgram
       
    def calculateN(self, ngram):
        N = [0,0,0,0,0,0]
        for key, value in ngram.iteritems():
            if value == 1:
                N[0] = N[0] + 1
            if value == 2:
                N[1] = N[1] + 1
            if value == 3:
                N[2] = N[2] + 1
            if value == 4:
                N[3] = N[3] + 1
            if value == 5:
                N[4] = N[4] + 1
            if value == 6:
                N[5] = N[5] + 1      
        return N
        
    def GT(self, ngram, corpusLength, N):
        for key, value in ngram.iteritems():             # for every entry in the ngram
            newValue = self.GTSmoothing(ngram, value, N, corpusLength) # return the new value using GT formula 
            ngram.update({key:newValue})                 # and update entry to new value
        return ngram

    def GTSmoothing(self, ngram, value, N, corpusLength):
            if value <= 5:
                newValue = ((value + 1) * N[value])/N[value-1]
                return newValue
            else: 
                return value
            