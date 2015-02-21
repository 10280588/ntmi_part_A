#######
# Copyright: Menno van Leeuwen (10280588)
# Assignment: NTMI step 1
#
import argparse
import sys
import ngrams
import prob
import perm
import filereader


# Class reads in arguments and then selects the correct case.
# Besides this a lot of information is printed.
# Actual program is devided among other classes.

class Main():
    def __init__(self):
        self.corpus = ''
        self.n = 0
        self.m = 10
        self.corpusList = []
        self.cp = None
        self.sp = None
        self.perm = False
        self.case = ''
        self.corpusList = []
        self.corpusList2 = []
        self.probList = []
        self.probDict = {}
        self.tmp = []
        self.sorted_nGrams = {}
        self.sorted_nGrams2 = {}
        self.sumFreq = 0

        self.argumentReader()
        self.caseOptions()

        if self.case == '1':
            self.printer1()
            #Create an instance so we can read the fileReader
            reader = filereader.Reader()
            #Actually read the file
            corpusList = reader.fileReaderStep1(self.corpus)
            # create instance of Ngram class
            gramInstance = ngrams.Ngrams()
            # create nGram
            createdNgram = gramInstance.calculateNGram(corpusList, self.n, self.m)
            # calculate the most frequent
            mostFreq = gramInstance.mostFrequent(createdNgram)
            # Calculate the sum
            sumOfFreq = gramInstance.sumOfFrequencies(mostFreq)
            # Print all results, which are stored in the variables
            self.printResult1(mostFreq,sumOfFreq)
        elif self.case == '2.1':
            self.printer21()
            self.fileReaderStep1()
            self.fileReader("paragraph")
            self.fileReader("paragraph2")
            ngrams.Ngrams(self.corpusList, self.n, self.m, self.sorted_nGrams)
            ngrams.Ngrams(self.corpusList, self.n-1, self.m, self.sorted_nGrams2)
            self.printResult21()
            #TODO: DONE!
        elif self.case == '2.2':
            self.printer22()
            self.fileReader("paragraph")
            self.fileReader("paragraph2")
            ngrams.Ngrams(self.corpusList, self.n, self.m, self.sorted_nGrams)
            ngrams.Ngrams(self.corpusList2, self.n-1, self.m, self.sorted_nGrams2)
            prob.Prob(self.case, self.cp, self.n, self.corpusList, self.corpusList2, self.probList, self.sorted_nGrams, self.sorted_nGrams2, self.probDict)
            self.printResult22()
            #TODO: like case 1, classes or methods need to be added
        elif self.case == '2.3':
            #self.printer23()
            self.fileReader("paragraph")
            self.fileReader("paragraph2")
            ngrams.Ngrams(self.corpusList, self.n, self.m, self.sorted_nGrams)
            ngrams.Ngrams(self.corpusList2, self.n-1, self.m, self.sorted_nGrams2)
            prob.Prob(self.case, self.sp, self.n, self.corpusList, self.corpusList2, self.probList, self.sorted_nGrams, self.sorted_nGrams2, self.probDict)
        elif self.case == '2.4':
            self.printer24()
            perm.Permutation(self.corpus)
        elif self.case == '3':
            self.fileReader("paragraph")
            ngrams.Ngrams(self.corpusList, 2, self.m, self.sorted_nGrams)
            self.sorted_nGrams = {key: value+1 for (key, value) in self.sorted_nGrams.iteritems()}
            #print self.sorted_nGrams

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
        parser.add_argument('-smoothing', help='Provide a smoothing method to get rid of zero entries')

        args = parser.parse_args()
        self.corpus = args.corpus
        self.n = args.n
        self.m = args.m
        self.cp = args.conditional_prob_file
        self.sp = args.sequence_prob_file
        self.perm = args.scored_permutations
        self.smoothing = args.smoothing

    #Decides what we are going to do, given the provided arguments.
    def caseOptions(self):
        print
        print 'The following part of the assignment is performed:'
        if  self.m > 0:
            print 'Do step 1'
            self.case = '1'
        elif self.cp != None:
            print 'Do step 2.2'
            self.case = '2.2'
        elif self.sp != None:
            print 'Do step 2.3'
            self.case = '2.3'
        elif self.perm == True:
            print 'Do step 2.4'
            self.case = '2.4'
        elif self.smoothing == 'no' or self.smoothing == 'add1' or self.smoothing == 'gt':
            self.case = '3'
            print 'Do step 3'
        elif self.smoothing != 'no' or self.smoothing == 'add1' or self.smoothing == 'gt':
            print 'The argument for the smoothing algorithm is incorrect, use \'no\', \'add1\' or \'gt\''
            sys.exit()
        elif self.n > 0:
            print 'Do step 2.1'
            self.case = '2.1'
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
        print
        print 'The program to calculate N-grams and N-1-Grams of a corpus has started.'
        print 'We will calculate two N-gram tables and display the top 10 most occurences of sequences per table'
        print
        print 'The used corpusfile is: ' + self.corpus
        print 'We will calculate the N-Gram with sequences of length: ' + str(self.n)
        print 'And a second table of with sequences of length: ' + str(self.n-1)
        print
    def printer22(self):
        print 'We will calculate the N-gram and the N-1-Gram, and then the probability.'
    def printer23(self):
        print 'step 2.3 is not implemented yet'
    def printer24(self):
        print 'step 2.4 is not fully implemented yet'
        print 'The program will now calculate permutations for you'
        print 'The used corpusfile is: ' + self.corpus
        print

    def printResult1(self, mostFrequent, sumOfFreq):
        print 'Calculations are done.'
        print
        print 'The top ' + str(self.m) + ' list of most occuring sequences ([word], [frequency]):'
        # Print the m most frequent ngrams.
        for i in range(0, self.m):
            #if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
            if i < len(mostFrequent):
                if mostFrequent[i][0] != '':
                    print mostFrequent[i]
            else:
                print 'There were only ' + str(i) + ' combinations, so they all fitted in your top ' + str(self.m) + ' list.'
                break
        print
        print 'The sum of all frequencies of the sequences is: ' + str(sumOfFreq)
        print
        #print 'The total sum of all sequence frequencies is: ' + str(self.sumFreq)
    #Opens our corpus.txt file and converts it to a list of words.
    def printResult21(self):
        print 'Calculations are done.'
        self.sorted_nGrams = sorted(self.sorted_nGrams.items(), key=lambda nGram: nGram[1], reverse=True)
        self.sorted_nGrams2 = sorted(self.sorted_nGrams2.items(), key=lambda nGram: nGram[1], reverse=True)
        print ''
        print 'The top 10 list of most occuring sequences ([word], [frequency]) for the provided N:'
        #Print the m most frequent ngrams.
        for i in range(0, 10):
            #if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
            if i < len(self.sorted_nGrams):
                if self.sorted_nGrams[i][0] != '':
                    print self.sorted_nGrams[i]
            else:
                print 'There were only ' + str(i) + ' combinations, so they all fitted in your top 10 list.'
                break
        print
        print 'Now for the value N-1'
        print ''
        print 'The top 10 list of most occuring sequences ([word], [frequency]) for the provided N-1:'
        #Print the m most frequent ngrams.
        for i in range(0, 10):
            #if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
            if i < len(self.sorted_nGrams2):
                if self.sorted_nGrams2[i][0] != '':
                    print self.sorted_nGrams2[i]
            else:
                print 'There were only ' + str(i) + ' combinations, so they all fitted in your top 10 list.'
                break
        print
        #print 'The total sum of all sequence frequencies is: ' + str(self.sumFreq)
    #Opens our corpus.txt file and converts it to a list of words.
    def printResult22(self):
        self.probDict = sorted(self.probDict.items(), key=lambda nGram: nGram[1], reverse=False)
        print 'We have calculated N-gram and the N-1-Gram.'
        print 'Then probability is calculated.'
        print 'We will now display the 25 sequences with the LOWEST probability.'
        for i in range(0, 25):
            #if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
            if i < len(self.probDict):
                if self.probDict[i][0] != '':
                    print self.probDict[i]
            else:
                print 'There were only ' + str(i) + ' combinations, so they all fitted in your top 25 list.'
                break
        print
