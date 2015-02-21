from __future__ import division

class Smooth():
    def add1(self, ngram):
        smoothedNgram = {key: value+1 for (key, value) in ngram.iteritems()}
        return smoothedNgram
        
    def GT(self, ngram):
        N = [0,0,0,0,0,0]
        
        for key, value in ngram.iteritems():
            if value == 1:
                N[1] = N[1] + 1
            if value == 2:
                N[2] = N[2] + 1
            if value == 3:
                N[3] = N[3] + 1
            if value == 4:
                N[4] = N[4] + 1
            if value == 5:
                N[5] = N[5] + 1
            if value == 6:
                N[6] == N[6] + 1
        for key, value in ngram.iteritems():             # for every entry in the ngram
            newValue = self.GTSmoothing(ngram, value, N) # return the new value from GT 
            ngram.update({key:newValue})                 # and update entry to new value
            
        #need for prob: len(yourdict.keys()) or len(yourdict) for vocabulary count
        #N = number words total (or ngrams)

    def GTSmoothing(self, ngram, value, N):
        if value == 0:
            return N[1]/len(ngram)
        else:
            if value <= 5:
                newValue = ((value + 1) * N[value+1])/N[value]
                return newValue
            else: 
                return value
            