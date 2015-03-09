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
import datetime

# Still using the training set as test set?
class Main():
    def __init__(self):
        self.trainSet = ''
        self.testSet = ''
        
        self.startsym = '<start>/START '
        self.stopsym = ' <stop>/STOP'
        
        oldTime = datetime.datetime.time(datetime.datetime.now())
        
        self.argumentReader()
        lists = self.fileReader(self.trainSet)
        allSentencesList = lists[0]
        tagList = lists[1]
        wordTagList = lists[2]
        
        gramInstance = ngrams.Ngrams()
        # Ngrams for task model, calculate unigram for count
        tagCount = gramInstance.calculateNGram(tagList, 1)
        wordTagCount = gramInstance.calculateNGram(wordTagList, 1)
        
        # Ngrams for language model
        wordTagbigram = gramInstance.calculateNGram(tagList, 2)
        wordTagTrigram = gramInstance.calculateNGram(tagList, 3)
        
        self.resultPrinter(wordTagTrigram)
        probInstance = prob.Prob()
        for sentenceList in allSentencesList:
            if len(sentenceList) <= 19: # Max length of sentence is 15 + start/stops
                sentence = ' '.join(sentenceList)
                probInstance.argMaxAllTags(sentence.split(), tagCount, wordTagCount, wordTagbigram, wordTagTrigram)
        
        newTime = datetime.datetime.time(datetime.datetime.now())  
        print
        print oldTime
        print newTime
        
        # Show accuracy
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
        
    def fileReader(self, corpus):
        tagList = []
        tupleList = []
        
        f = open(corpus, 'r')
        allSentencesList = []
        currentSentence = ''
        currentSentenceNoTags = []
        tagOccurence = []
        wordTagList = []
        for line in f:
            if not ('======================================' in line):
                line = line.replace('[','')
                line = line.replace(']','')

                if not ('./.' in line):
                    currentSentence += line
                else :
                    currentSentence += line
                    currentSentenceList = currentSentence.split()
                    size = len(currentSentenceList)
                    currentSentence = self.startsym * 2 + currentSentence + self.stopsym * 2 # slechts 2 starts nodig, we gebruiken alleen trigrams
                    currentSentenceList = currentSentence.split()
                    
                    for word in currentSentenceList:
                        if '/' in word:
                            wordAndTag = word.rsplit('/', 1)
                            word = wordAndTag[0]
                            word = word.replace('\\', '')
                            currentSentenceNoTags.append(word)
                            tag = wordAndTag[1]
                            wordTagList.append((word,tag))
                            tagList.append(tag)
                    allSentencesList.append(currentSentenceNoTags)
                    currentSentence = ''
                    currentSentenceNoTags = []
                    currentSentenceList = []
        print 'tagging'
        return (allSentencesList, tagList, wordTagList)
        
    def resultPrinter(self, trigram):
        print 'Results: '
        