from __future__ import division
import sys
import smooth

class Prob():
    def calcProbNgram(self, ngram, ngramMin1):
        probDict = {}
        for key in ngram:
            biKey = key.rsplit(' ',1)[0]
            #print 'bikey is:'
            #print key
            #print biKey
            numerator = ngram.get(key,None)
            if biKey in ngramMin1:
                denominator = ngramMin1.get(biKey, None)
            #print numerator
            #print denominator
            prob = numerator/denominator
            #print prob
            probDict.update({key: prob})
            
            
            
          
        return probDict