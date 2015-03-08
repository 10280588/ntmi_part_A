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
        
        self.startsym = '<s>'
        self.stopsym = '</s>'
        
        self.argumentReader()
        lists = self.fileReader(self.trainSet)
        tagList = lists[0]
        wordTagList = lists[1]
        #print wordTagList
        
        gramInstance = ngrams.Ngrams()
        # Ngrams for task model, calculate unigram for count
        tagCount = gramInstance.calculateNGram(tagList, 1)
        wordTagCount = gramInstance.calculateNGram(wordTagList, 1)
        
        # Ngrams for language model
        wordTagBigram = gramInstance.calculateNGram(tagList, 2)     
        wordTagTrigram = gramInstance.calculateNGram(tagList, 3)
        
        self.resultPrinter(wordTagTrigram, wordTagBigram)
        probInstance = prob.Prob()
        #probDict = probInstance.calcProbNgram(trigram, bigram)
        #print probDict
        probInstance.argMaxTags('a man has a balloon'.split(), tagCount, wordTagCount)
        
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
        currentSentence = ''
        tagOccurence = []
        wordTagList = []
        for line in f:
            if not ('======================================' in line):
                line = line.replace('[','')
                line = line.replace(']','')

                if not ('./.' in line):
                    currentLine += line
                    currentSentence += line
                else :
                    currentLine += line
                    currentSentence += line
                    currentSentenceList = currentSentence.split()
                    size = len(currentSentenceList)
                    sentenceNoTags = ''
                    sentenceTags = ''
                    for word in currentSentenceList:
                        if '/' in word:
                            wordAndTag = word.rsplit('/', 1)
                            word = wordAndTag[0]
                            word = word.replace('\\', '')
                            tag = wordAndTag[1]
                            wordTagList.append((word,tag))
                            tagList.append(tag)
                    currentLine = self.startsym * (size - 1) + currentSentence + self.stopsym * (size - 1)
                    currentSentence = ''

            #Todo: fileReader
        print 'tagging'
        return (tagList, wordTagList)
        
    def resultPrinter(self, trigram, bigram):
        print 'Results: '
        