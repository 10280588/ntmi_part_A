from __future__ import division

class Prob():

    def __init__(self, case, probfile, n, corpusList, corpusList2, probList, sorted_nGrams, sorted_nGrams2, probDict):
        self.probfile = probfile
        self.n = n
        self.corpusList = corpusList
        self.corpusList2 = corpusList2
        self.probList = probList
        self.sorted_nGrams = sorted_nGrams
        self.sorted_nGrams2 = sorted_nGrams2
        self.probDict = {}
        self.case = case

        if self.case == '2.2':
            self.calculateProb()
        if self.case == '2.3':
            self.calculateProbUsingFormula()

    # Calculates the probability of an N-gram given an (N-1)-Gram of a file. Uses only sentences of length n (starts/stops not included)
    def calculateProb(self):
        f = open(self.probfile, 'r')
        for line in f:
            line = line[:len(line)-1]
            strList = line.split()
            if len(strList) == self.n:
                line = ['<s>' for s in xrange(self.n-1)] + strList + ['</s>' for s in xrange(self.n-1)]
                for i in range(0, len(line) - self.n):
                    entryAmount = self.sorted_nGrams.get(' '.join(line[i:i+self.n]), None)
                    if entryAmount != None:
                        entryAmount2 = self.sorted_nGrams2.get(' '.join(line[i:i+self.n-1]), None)
                        if entryAmount2 != None:
                            odds = entryAmount/entryAmount2
                            self.probDict.update({' '.join(line[i:i+self.n]):odds})
                            #print self.probDict

    def calculateProbUsingFormula(self):
        odds = 1
        f = open(self.probfile, 'r')
        for line in f:
            line = line[:len(line)-1]
            strList = line.split()
            lineWithStarts = ['<s>' for s in xrange(self.n-1)] + strList + ['</s>' for s in xrange(self.n-1)]
            for i in range(1, len(strList) + self.n):
                entryAmount = self.sorted_nGrams.get(' '.join(lineWithStarts[i-1:i+self.n-1]), None)
                #print line
                #print ' '.join(lineWithStarts[i-1:i+self.n-1])
                if entryAmount != None:
                    #print '1'
                    entryAmount2 = self.sorted_nGrams2.get(' '.join(lineWithStarts[i-1:i+self.n]), None)
                    if entryAmount2 != None:
                        #print '2'
                        odds = odds * (entryAmount/entryAmount2)
                        #print odds
                    #if entryAmount2 != None:

                #print entryAmount
                #odds = odds * self.sorted_nGrams.get(' '.join(strList
