#######
# Copyright: Menno van Leeuwen (10280588)
# Assignment: NTMI step 1
#
from __future__ import division
import argparse
import sys
import ngrams
import prob
import perm
import smooth
import filereader


# Class reads in arguments and then selects the correct case.
# Besides this a lot of information is printed.
# Actual program is devided among other classes.

class Main():
    def __init__(self):
        self.corpus = ''
        self.n = 0
        self.m = 10
        self.cp = None
        self.sp = None
        self.perm = False
        self.case = ''
        self.train = None
        self.test = None

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
            createdNgram = gramInstance.calculateNGram(corpusList, self.n)
            mostFreq = gramInstance.mostFrequent(createdNgram)
            sumOfFreq = gramInstance.sumOfFrequencies(mostFreq)
            # Print all results, which are stored in the variables
            self.printResult1(mostFreq,sumOfFreq)
        elif self.case == '2.1':
            self.printer21()
            #Create an instance so we can read the fileReader
            reader = filereader.Reader()
            #Actually read the file
            corpusList = reader.fileReader(self.corpus, self.n)
            gramInstance = ngrams.Ngrams()
            createdNgram = gramInstance.calculateNGram(corpusList, self.n)
            createdNgramMin1 = gramInstance.calculateNGram(corpusList, self.n-1)
            mostFreq = gramInstance.mostFrequent(createdNgram)
            mostFreqMin1 = gramInstance.mostFrequent(createdNgramMin1)
            self.printResult21(mostFreq, mostFreqMin1)
        elif self.case == '2.2':
            self.printer22()
            reader = filereader.Reader()
            corpusList = reader.fileReader(self.corpus, self.n)
            lineList = reader.lineReader(self.cp, self.n)
            #print lineList
            #create the two ngrams
            gramInstance = ngrams.Ngrams()
            createdNgram = gramInstance.calculateNGram(corpusList, self.n)
            createdNgramMin1 = gramInstance.calculateNGram(corpusList, self.n-1)
            # Calculate the probability
            probInstance = prob.Prob()
            probList = probInstance.calculateProb(createdNgram, createdNgramMin1, lineList, self.n)
            self.printResult22(probList)
        elif self.case == '2.3':
<<<<<<< HEAD
            print 'hoi'
            #self.printer23()
           # ngrams.Ngrams(self.corpusList, self.n, self.m, self.sorted_nGrams)
        #    ngrams.Ngrams(self.corpusList2, self.n-1, self.m, self.sorted_nGrams2)
        #    prob.Prob(self.case, self.sp, self.n, self.corpusList, self.corpusList2, self.probList, self.sorted_nGrams, self.sorted_nGrams2, self.probDict)
=======
            self.printer23()
            reader = filereader.Reader()
            corpusList = reader.fileReader(self.corpus, self.n)
            lineList = reader.lineReader(self.sp, self.n)
            #print lineList
            #create the two ngrams
            gramInstance = ngrams.Ngrams()
            createdNgram = gramInstance.calculateNGram(corpusList, self.n)
            createdNgramMin1 = gramInstance.calculateNGram(corpusList, self.n-1)
            # Calculate the probability
            probInstance = prob.Prob()
            probList = probInstance.sequenceProb(createdNgram, createdNgramMin1, lineList, self.n)
            self.printResult22(probList)
>>>>>>> 23c04ae247801cf3c91a3e94a7d2e4e1470bc088
        elif self.case == '2.4':
            self.printer24()
            # create a list
            reader = filereader.Reader()
            corpusList = reader.fileReaderStep1(self.corpus)
            print corpusList
            permInstance = perm.Permutation()
            permutations = permInstance.allPermutations(corpusList)
            gramInstance = ngrams.Ngrams()
            createdNgram = gramInstance.calculateNGram(permutations, 2)
            createdNgramMin1 = gramInstance.calculateNGram(permutations, 1)
            # Calculate the probability
            probInstance = prob.Prob()
            #probList = probInstance.calculateProb(createdNgram, createdNgramMin1, permutationS, self.n)
            mostFreq = gramInstance.mostFrequent(createdNgram)
            mostFreqMin1 = gramInstance.mostFrequent(createdNgramMin1)
            self.printResult21(mostFreq, mostFreqMin1)
            print createdNgram
            print createdNgramMin1
        elif self.case == '3add1':
            print '3add1'
            print 'Add1 smoothing and GT smoothing will never assign 0 probability to a sentence, whereas without smoothing'
            print 'it would assign 0 whenever one ngram of the sentence doesn\'t occur'
            #read files
            reader = filereader.Reader()
            corpusListTrain = reader.fileReader(self.train, self.n)
            corpusListTest = reader.lineReader(self.test, self.n)
            #make ngrams
            gramInstance = ngrams.Ngrams()
            createdNgram = gramInstance.calculateNGram(corpusListTrain, self.n)
            createdNgramMin1 = gramInstance.calculateNGram(corpusListTrain, self.n-1)
            #calculate probability
            probInstance = prob.Prob()
            probList = probInstance.calculateProb(createdNgram, createdNgramMin1, corpusListTest, self.n)
            smoothInstance = smooth.Smooth()
            ngramAdd1 = smoothInstance.add1(createdNgram)
            ngramMin1Add1 = smoothInstance.add1(createdNgramMin1)
            probInstance = prob.Prob()
            for item in corpusListTest:
                odds = 1
                entryList = item.split()
                for i in range(0, len(entryList)-self.n):
                    entry = ' '.join(entryList[i+1:i+self.n+1])
                    odds = odds*probInstance.calculateProbabilityUsingAdd1(ngramAdd1, ngramMin1Add1, entry)
                print item + '-> odds = ' + str(odds)
        elif self.case == '3gt':
            print 'Add1 smoothing and GT smoothing will never assign 0 probability to a sentence, whereas without smoothing'
            print 'it would assign 0 whenever one ngram of the sentence doesn\'t occur'
            corpusLength = len(self.corpus)

        elif self.case == '3no':
            print 'Add1 smoothing and GT smoothing will never assign 0 probability to a sentence, whereas without smoothing'
            print 'it would assign 0 whenever one ngram of the sentence doesn\'t occur'
            print 'Todo 3 no' # same as 2.3 so fix pls


    #Takes care of provided arguments, if none given use default!
    def argumentReader(self):
        # Make a nice way to handle command line arguments
        parser = argparse.ArgumentParser()
        # -corpus argumentgit
        parser.add_argument('-corpus', help='Provide a text corpus file in the .txt format to perform an N-gram calculation.')
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
        parser.add_argument('-train-corpus', help='Provide a smoothing method to get rid of zero entries')
        parser.add_argument('-test-corpus', help='Provide a smoothing method to get rid of zero entries')

        args = parser.parse_args()
        self.corpus = args.corpus
        self.n = args.n
        self.m = args.m
        self.cp = args.conditional_prob_file
        self.sp = args.sequence_prob_file
        self.perm = args.scored_permutations
        self.smoothing = args.smoothing
        self.test = args.test_corpus
        self.train = args.train_corpus

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
        elif self.smoothing == 'no':
            self.case = '3no'
            print 'Do step 3, with no smoothing'
        elif self.smoothing == 'add1':
            self.case = '3add1'
            print 'Do step 3, with add1 smoothing'
        elif self.smoothing == 'gt':
            self.case = '3gt'
            print 'Do step 3, with Good-Turing smoothing'
        elif self.n > 0:
            print 'Do step 2.1'
            self.case = '2.1'
        else:
           print 'The program has found no options, nothing to do here.'
           print 'Please read the documentation.'
           sys.exit()
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
        print 'We will calculate the change of the sequence based on multiplication of the probability of every word.'
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
    def printResult21(self, mostFreq, mostFreqMin1):
        print 'Calculations are done.'
        print ''
        print 'The top 10 list of most occuring sequences ([word], [frequency]) for the provided N:'
        #Print the m most frequent ngrams.
        for i in range(0, 25):
            #if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
            if i < len(mostFreq):
                if mostFreq[i][0] != '':
                    print mostFreq[i]
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
            if i < len(mostFreqMin1):
                if mostFreqMin1[i][0] != '':
                    print mostFreqMin1[i]
            else:
                print 'There were only ' + str(i) + ' combinations, so they all fitted in your top 10 list.'
                break
        print
        #print 'The total sum of all sequence frequencies is: ' + str(self.sumFreq)
    #Opens our corpus.txt file and converts it to a list of words.
    def printResult22(self, probList):
        probList = sorted(probList.items(), key=lambda probList: probList[1], reverse=False)
        print 'We have calculated N-gram and the N-1-Gram.'
        print 'Then probability is calculated.'
        print 'We will now display the 25 sequences with the LOWEST probability.'
        for i in range(0, 25):
            #if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
            if i < len(probList):
                if probList[i][0] != '':
                    print probList[i]
            else:
                print 'There were only ' + str(i) + ' combinations, so they all fitted in your top 25 list.'
                break
        print
