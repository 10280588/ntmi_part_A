#######
# Copyright: Menno van Leeuwen (10280588)
# Assignment: NTMI step 1
#
import argparse
import sys
import ngrams

class Main():
    def __init__(self, step):
        self.corpus = ''
        self.n = 0
        self.m = 0
        self.corpusList = []

        if step == 1:
            self.argumentReader()
            self.startPrinter()
            self.fileReaderStep1()

        ngrams.Ngrams(self.corpusList, self.n, self.m)
    #Takes care of provided arguments, if none given use default!
    def argumentReader(self):
        # Make a nice way to handle command line arguments
        parser = argparse.ArgumentParser()
        # -corpus argument
        parser.add_argument('-corpus', required=True,
        help='Provide a text corpus file in the .txt format to perform an N-gram calculation.')
        # -n argument
        parser.add_argument('-n', type=int, required=True,
        help='Provide a number (integer) to calculate N-grams with word sequences of length n.')
        # -m argument
        parser.add_argument('-m', type=int, required=True,
        help='Provide a number (integer) to display the m-th most frequent sequences.')
        args = parser.parse_args()
        self.corpus = args.corpus
        self.n = args.n
        self.m = args.m
    #Prints an initial start message as well as the used values.
    def startPrinter(self):
        print
        print 'The program to calculate N-grams of a corpus has started.'
        print 'You can find help about the working by typing main.py -h'
        print 'If no arguments are provided the program loads with default values.'
        print
        print 'The used corpusfile is: ' + self.corpus
        print 'We will calculate the N-Gram with sequences of length: ' + str(self.n)
        print 'The number of most frequent sequences (m) is: ' + str(self.m)
        print 
    #Opens our corpus.txt file and converts it to a list of words.
    def fileReaderStep1(self):
        f = open(self.corpus, 'r')
        for line in f:
            for word in line.split():
                self.corpusList.append(word)
        f.close()


