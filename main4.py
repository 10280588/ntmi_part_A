#######
# Copyright: Menno van Leeuwen (10280588), Jelmer Alphenaar (10655751), Sosha Happel 
# Assignment: NTMI step 4
#
from __future__ import division
import argparse
import sys
import ngrams
import smooth
import filereader
import prob4

class Main():
    def __init__(self):
        self.trainingCorpus = ''
        self.developCorpus = ''
        self.n = 0
        
        self.argumentReader()
        self.trainingCorpus = self.fileReader(self.trainingCorpus)

        gramInstance = ngrams.Ngrams()
        createdNgram = gramInstance.calculateNGram(self.trainingCorpus, self.n)
        createdNgramMin1 = gramInstance.calculateNGram(self.trainingCorpus, self.n-1)
        
        self.resultPrinter(createdNgram, createdNgramMin1)
        probInstance = prob4.Prob()
        probDict = probInstance.calcProbNgram(createdNgram, createdNgramMin1)
        print probDict
        
    #Takes care of provided arguments, if none given use default!
    def argumentReader(self):
        # Make a nice way to handle command line arguments
        parser = argparse.ArgumentParser()
        # -corpus argumentgit
        parser.add_argument('-n',  type=int,
        help='Provide a number (integer) to calculate N-grams with word sequences of length n.')
        parser.add_argument('-trainingCorpus', help='Provide a text corpus file in the .pos format to perform an N-gram calculation and probabilities.')
        parser.add_argument('-developCorpus', help='Provide a text corpus file in the .pos format to test our calculations on another corpus.')
        args = parser.parse_args()
        
        self.trainingCorpus = args.trainingCorpus
        self.developCorpus = args.developCorpus
        self.n = args.n
        
        # No start/stop statements, sentences longer than 15 words can be ignored.
    def fileReader(self, corpus):
        corpusList = []
        tagDict = {}
        f = open(corpus, 'r')
        for line in f:
            if (not '=======' in line):
                lineLength = len(line.split())
                if lineLength <= 15:
                    for word in line.split():
                        if not (( '[' in word) or ( ']' in word)):
                            print word
                        if '/' in word:
                            wordAndTag = word.split('/')
                            key = wordAndTag[0]
                            value = wordAndTag[1]
                            if not ( key in tagDict):
                                valueList = []
                                valueList.append(value)
                                
                            elif (key in tagDict):
                                print tagDict.get(key, None)
                                valueList = tagDict.get(key, None)
                                valueList.append(value)
                            if key.isalnum():
                                corpusList.append(key)
                            tagDict.update({key : valueList})
            else:
                num  =5
            #Todo: fileReader
        print 'tagging'
        print tagDict
        return corpusList
        
    def resultPrinter(self, createdNgram, createdNgramMin1):
        print 'Results: '
        print createdNgram
        