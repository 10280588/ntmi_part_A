from __future__ import division
import sys
import smooth

class Prob():
    # Calculates the probability of an N-gram given an (N-1)-Gram of a file. Uses only sentences of length n (starts/stops not included)
    def calculateProb(self, ngram, ngramMin1, lineList, n):
        probDict = {}

        #f = open(self.probfile, 'r')
        print lineList
        for line in lineList:
            strList = line.split()
            print strList
            if n < 3:
                loop = n + 1
            else:
                loop = n + 2
            for i in range(0, loop):
                #Make the sequence we want to test
                sequence = strList[i];
                print sequence
                for j in range(1,n):
                    sequence = sequence + " " + strList[i+j]
                    print sequence
                probDict.update({sequence:0})
                #Now make the sequence which is one item shorter
                sequenceMin1 = strList[i];
                for j in range(1,n-1):
                    sequenceMin1 = sequenceMin1 + " " + strList[i+j]
                #If the test sequence exists in our training Ngram get its occurences
                occurenceNgram = ngram.get((sequence), None)
                if occurenceNgram != None:
                    #If the test sequence exists in our training Ngram then also get Ngram-1 occurences
                    occurenceNgramMin1 = ngramMin1.get((sequenceMin1), None)

                    if occurenceNgramMin1 != None:
                        # If the sequence exits in both the Ngram and Ngram -1 calculate the odds
                        odds = occurenceNgram/occurenceNgramMin1
                        probDict.update({(sequence):odds})
        return probDict

    def sequenceProb(self, ngram, ngramMin1, lineList, n):
        probDict = {}
        odds = 1

        for line in lineList:
            strList = line.split()
            if n < 3:
                loop = n + 1
            else:
                loop = n + 2
            for i in range(0, loop):
                #Make the sequence we want to test
                sequence = strList[i];
                probDict.update({line:0})
                #Now make the sequence which is one item shorter
                sequenceMin1 = strList[i];
                for i in range(1, len(strList)):
                    iteminNgram = ' '.join(strList[i-1:i+n-1])
                    iteminNgramMin1 = ' '.join(strList[i-1:i+n-2])
                    entryAmount = ngram.get(iteminNgram, None)
                    if entryAmount != None:
                        entryAmount2 = ngramMin1.get(iteminNgramMin1, None)
                        if entryAmount2 != None:
                            odds = odds * (entryAmount/entryAmount2)
                        probDict.update({line:odds})
        return probDict

    def permProb(self, ngram, ngramMin1, lineList, n):
        probDict = {}

        #f = open(self.probfile, 'r')
        for line in lineList:
            strList = line.split()

            if n < 3:
                loop = n + 1
            else:
                loop = n + 2
            for i in range(0, loop):
                #Make the sequence we want to test
                sequence = strList[i];
                for j in range(1,n):
                    sequence = sequence + " " + strList[i+j]
                probDict.update({sequence:0})
                #Now make the sequence which is one item shorter
                sequenceMin1 = strList[i];
                for j in range(1,n-1):
                    sequenceMin1 = sequenceMin1 + " " + strList[i+j]
                #If the test sequence exists in our training Ngram get its occurences
                occurenceNgram = ngram.get((sequence), None)
                if occurenceNgram != None:
                    #If the test sequence exists in our training Ngram then also get Ngram-1 occurences
                    occurenceNgramMin1 = ngramMin1.get((sequenceMin1), None)

                    if occurenceNgramMin1 != None:
                        # If the sequence exits in both the Ngram and Ngram -1 calculate the odds
                        odds = occurenceNgram/occurenceNgramMin1
                        probDict.update({(sequence):odds})

        return probDict

    # This is only for one ngram-combination, can be used for whole sentences
    def calculateProbabilityUsingAdd1(self, ngram, ngramMin1, entry):
        entryAmount = ngram.get(entry, None)
        entryList = entry.split()
        entryListWithoutLastWord = entryList[:-1]
        entryWithoutLastWord = ' '.join(entryListWithoutLastWord)
        if entryAmount == None:
            entryAmount = 1
        entryAmount2 = ngramMin1.get(entryWithoutLastWord, None)
        if entryAmount2 == None:
            entryAmount2 = 1
        odds = entryAmount/(entryAmount2 + len(ngram))
        return odds

    # Exercise doesn't clearly tell how to do this
    #def calculateProbabilityUsingGT(self, ngram, ngramMin1, corpusLength):
        #smoothedNgram = smooth.GT(ngram, corpusLength)
    
