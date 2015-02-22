from __future__ import division
import sys
class Prob():
    #    if self.case == '2.2':
    #        self.calculateProb()
    #    if self.case == '2.3':
    #        f = open(self.probfile, 'r')
    #        for line in f:
    #            probs = self.calculateProbabilityOfString(line)
    #            self.probDict.update({line:probs})
    #        print self.probDict

    # Calculates the probability of an N-gram given an (N-1)-Gram of a file. Uses only sentences of length n (starts/stops not included)
    def calculateProb(self, ngram, ngramMin1, lineList, n):
        probDict = {}
        #f = open(self.probfile, 'r')
        for line in lineList:
            strList = line.split()
            if n < 3:
                loop = n
            else:
                loop = n + 2
            for i in range(0, loop):
                #Make the sequence we want to test
                print 'begin of sbuilder'
                sequence = strList[i];
                #print strList
                for j in range(1,n):
                    sequence = sequence + " " + strList[i+j]
                print sequence
                probDict.update({sequence:0})
                #Now make the sequence which is one item shorter
                sequenceMin1 = strList[i];
                for j in range(1,n-1):
                    sequenceMin1 = sequenceMin1 + " " + strList[i+j]

                #If the test sequence exists in our training Ngram get its occurences
                print 'testeds'
                print sequence
                occurenceNgram = ngram.get((sequence), None)
                print occurenceNgram
                if occurenceNgram != None:
                    #If the test sequence exists in our training Ngram then also get Ngram-1 occurences
                    occurenceNgramMin1 = ngramMin1.get((sequenceMin1), None)
                    print occurenceNgramMin1
                    if occurenceNgramMin1 != None:
                        # If the sequence exits in both the Ngram and Ngram -1 calculate the odds
                        odds = occurenceNgram/occurenceNgramMin1
                        probDict.update({(sequence):odds})
        return probDict
    # Calculates the probability of a sentence by multiplying the probability of sequences of N-grams

    def calculateProbabilityOfString(self, line):
        odds = 1
        line = line[:len(line)-1]
        strList = line.split()
        lineWithStarts = ['<s>' for s in xrange(self.n-1)] + strList + ['</s>' for s in xrange(self.n-1)]
        self.probDict.update({line:0})

        for i in range(1, len(strList) + self.n):
            entryAmount = self.sorted_nGrams.get(' '.join(lineWithStarts[i-1:i+self.n-1]), None)
            if entryAmount != None:
                entryAmount2 = self.sorted_nGrams2.get(' '.join(lineWithStarts[i-1:i+self.n-2]), None)
                if entryAmount2 != None:
                    odds = odds * (entryAmount/entryAmount2)
                    return odds
