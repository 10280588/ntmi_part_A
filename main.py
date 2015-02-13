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
        self.n = 1
        self.m = 2
        self.corpusList = []
        self.cp = None
        self.sp = None
        self.perm = False
        self.case = ''

        self.argumentReader()
        self.caseOptions()

        if self.case == '1':
            self.printer1()
            self.fileReaderStep1()
            ngrams.Ngrams(self.corpusList, self.n, self.m)
        elif self.case == '2.1':
            self.printer21()
            #TODO: like case 1, classes or methods need to be added
        elif self.case == '2.2':
            self.printer22()
            #TODO: like case 1, classes or methods need to be added
        elif self.case == '2.3':
            self.printer23()
            #TODO: like case 1, classes or methods need to be added
        elif self.case == '2.4':
            self.printer24()
            boe = ngrams.Ngrams(['one','two','three'], 1, 2)
            boe.probabilityOfPermutations(boe.corpusList)
            #TODO: like case 1, classes or methods need to be added

    #Takes care of provided arguments, if none given use default!
    def argumentReader(self):
        # Make a nice way to handle command line arguments
        parser = argparse.ArgumentParser()
        # -corpus argumentgit
        parser.add_argument('-corpus', required=True,
        help='Provide a text corpus file in the .txt format to perform an N-gram calculation.')
        # -n argument
        parser.add_argument('-n',  type=int,
        help='Provide a number (integer) to calculate N-grams with word sequences of length n.')
        # -m argument
        parser.add_argument('-m', type=int,
        help='Provide a number (integer) to display the m-th most frequent sequences.')
        # -conditional-prob-file
        parser.add_argument('-conditional-prob-file',
        help='Provide a text corpus file in the .txt format to use for conditional probability')
        # -sequence-prob-file argument
        parser.add_argument('-sequence-prob-file',
        help='Provide a text corpus file in the .txt format')
        # -scored-permutations argument
        parser.add_argument('-scored-permutations', action='store_true')

        args = parser.parse_args()
        self.corpus = args.corpus
        self.n = args.n
        self.m = args.m
        self.cp = args.conditional_prob_file
        self.sp = args.sequence_prob_file
        self.perm = args.scored_permutations

    #Decides what we are going to do, given the provided arguments.
    def caseOptions(self):
        print
        print 'The following part of the assignment is performed:'
        if  self.m > 0:
            print 'Do step 1'
            self.case = '1'
        elif self.n > 0:
            print 'Do step 2.1'
            self.case = '2.1'
        elif self.cp != None:
            print 'Do step 2.2'
            self.case = '2.2'
        elif self.sp != None:
            print 'Do step 2.3'
            self.case = '2.3'
        elif self.perm == True:
            print 'Do step 2.4'
            self.case = '2.4'
        else:
           print 'The program has found no options, nothing to do here.'
           print 'Please read the documentation.'
        print '-----------------------'

    #Prints an initial start message as well as the used values.
    def printer1(self):
        print
        print 'The program to calculate N-grams of a corpus has started.'
        print 'You can find help about the working by typing main.py -h'
        print 'If no arguments are provided the program loads with default values.'
        print
        print 'The used corpusfile is: ' + self.corpus
        print 'We will calculate the N-Gram with sequences of length: ' + str(self.n)
        print 'The number of most frequent sequences (m) is: ' + str(self.m)
        print
    def printer21(self):
        print 'step 2.1 is not implemented yet'
    def printer22(self):
        print 'step 2.2 is not implemented yet'
    def printer23(self):
        print 'step 2.3 is not implemented yet'
    def printer24(self):
        print 'step 2.4 is not fully implemented yet'
        print 'The program will now calculate permutations for you'
        print 'The used corpusfile is: ' + self.corpus
        print

    #Opens our corpus.txt file and converts it to a list of words.
    def fileReaderStep1(self):
        f = open(self.corpus, 'r')
        for line in f:
            for word in line.split():
                self.corpusList.append(word)
        f.close()
