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
import prob

class Main():
    def __init__(self):
        self.trainSet = ''
        self.testSet = ''
        
        self.argumentReader()
        self.trainSet = self.fileReader(self.trainSet)
        
        gramInstance = ngrams.Ngrams()
        trigram = gramInstance.calculateNGram(self.trainSet, 3)
        bigram = gramInstance.calculateNGram(self.trainSet, 2)
        unigram = gramInstance.calculateNGram(self.trainSet, 1)

        if self.trainSet == 'minitraining.pos':
            print 
            #print 'unigram = '
            #print unigram
            
            #print 
            #print 'bigram = '
            #print bigram
            
            #print 
            #print 'trigram = '
            #print trigram
        
        self.resultPrinter(trigram, bigram)
        probInstance = prob.Prob()
        probDict = probInstance.calcProbNgram(trigram, bigram)
        #print probDict
        
    #Takes care of provided arguments, if none given use default!
    def argumentReader(self):
        # Make a nice way to handle command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-train-set', help='Provide a text corpus file in the .pos format to perform an N-gram calculation and probabilities.')
        parser.add_argument('-test-set', help='Provide a text corpus file in the .pos format to test our calculations on another corpus.')
        parser.add_argument('-test-set-predicted')
        args = parser.parse_args()
        
        self.trainSet = args.train_set
        self.testSet = args.test_set
        
        # No start/stop statements, sentences longer than 15 words can be ignored.
    def fileReader(self, corpus):
        tagList = []
        tupleList = []
        
        f = open(corpus, 'r')
        currentLine = ''
        for line in f:
            if (not './.' in line):
                currentLine += line
            #line = '</s> <s>'
            #if (not '=======' in line):
                
            else:
                lineLength = len(currentLine.split())
                if lineLength <= 15:
                    for string in currentLine.split():
                        #print string
                        if not (( '[' in string) or ( ']' in string)):
                            #print string
                            if '/' in string:
                                wordAndTag = string.split('/')
                                word = wordAndTag[0]
                                tag = wordAndTag[1]
                                if word.isalnum():
                                    tagList.append(tag)
                                    tupleList.append((word,tag))
                currentLine = ''
            #Todo: fileReader
        print 'tagging'
        #print tupleList
        return tagList
        
    def resultPrinter(self, trigram, bigram):
        print 'Results: '
        print trigram
        