#######
# Copyright: Menno van Leeuwen (10280588), Jelmer Alphenaar (10655751), Sosha Happel 
# Assignment: NTMI step 4
#
from __future__ import division
import argparse
import sys
import ngrams
import prob
import perm
import smooth
import filereader

class Main():
    def __init__(self):
        self.trainingCorpus = ''
        self.developCorpus = ''
        self.n = 0
        
        self.argumentReader()
        self.trainingCorpus = self.fileReader(self.trainingCorpus)
        print self.trainingCorpus
        print self.n
        gramInstance = ngrams.Ngrams()
        createdNgram = gramInstance.calculateNGram(self.trainingCorpus, self.n)
        createdNgramMin1 = gramInstance.calculateNGram(self.trainingCorpus, self.n-1)
        
        self.resultPrinter(createdNgram, createdNgramMin1)
        
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
        
    def fileReader(self, corpus):
        corpusList = ['one', 'two', 'three']
        #Todo: fileReader
        return corpusList
        
    def resultPrinter(self, createdNgram, createdNgramMin1):
        print 'Results: '
        print createdNgram
        