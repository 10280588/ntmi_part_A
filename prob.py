from __future__ import division
    
class Prob():
    
    def __init__(self, probfile, n, corpusList, corpusList2, probList, sorted_nGrams, sorted_nGrams2, probDict):
        self.probfile = probfile
        self.n = n
        self.corpusList = corpusList
        self.corpusList2 = corpusList2
        self.probList = probList
        self.sorted_nGrams = sorted_nGrams
        self.sorted_nGrams2 = sorted_nGrams2
        self.probDict = probDict
        self.calculateProb()
        
    # Calculates the probability of an N-gram given an (N-1)-Gram of a file. Uses only sentences of length n (starts/stops not included)    
    def calculateProb(self):
        f = open(self.probfile, 'r')
        for line in f:
            line = line[:len(line)-1]
            strList = line.split()
           # print strList
            if len(strList) == self.n:
               # print 'same'
                line = ['<s>' for s in xrange(self.n-1)] + strList + ['</s>' for s in xrange(self.n-1)]
                #print line
                for i in range(0, len(line) - self.n):
                    #print self.sorted_nGrams
                    entryAmount = self.sorted_nGrams.get(' '.join(line[i:i+self.n]), None)
                    if entryAmount != None:
                        entryAmount2 = self.sorted_nGrams2.get(' '.join(line[i:i+self.n-1]), None)  
                        odds = entryAmount/entryAmount2
                        self.probDict.update({' '.join(line[i:i+self.n]):odds})