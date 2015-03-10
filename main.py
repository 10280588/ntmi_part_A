#######
# Copyright: Menno van Leeuwen (10280588), Jelmer Alphenaar (10655751), Yuri Sturkenboom (10639748)
# Assignment: NTMI step 4
#
from __future__ import division
import argparse
import sys
import ngrams
import smooth
import prob
import datetime

class Main():
    def __init__(self):
        self.trainSet = ''
        self.testSet = ''

        self.startsym = '<start>/START '
        self.stopsym = ' <stop>/STOP'

        # determines how many lines should be read before stopping
        # set to 99999999 to read until EOF (takes VERY long!!!)
        maxLinesToRead = 100

        oldTime = datetime.datetime.time(datetime.datetime.now())

        self.argumentReader()
        trainingCorpuslist = self.fileReader(self.trainSet)

        print 'Tagging'
        gramInstance = ngrams.Ngrams()
        # Ngrams for task model, calculate unigram for count
        tagCount = gramInstance.calculateNGram(trainingCorpuslist[1], 1)
        wordTagCount = gramInstance.calculateNGram(trainingCorpuslist[2], 1)

        # Ngrams for language model
        wordTagbigram = gramInstance.calculateNGram(trainingCorpuslist[1], 2)
        wordTagTrigram = gramInstance.calculateNGram(trainingCorpuslist[1], 3)

        lists = self.fileReader(self.trainSet)
        allSentencesList = lists[0]
        tagList = lists[1]
        wordTagList = lists[2]

        probInstance = prob.Prob()
        testCorpusList = self.fileReader(self.testSet)
        fileWrite = open(self.testSetPredicted,'w')

        # these two variables are to deterine accuracy later on
        totalConsidered = 0
        totalCorrect = 0
        
        # used to terminate earlier to save time
        acCount = 0

        for sentenceAndTagList in testCorpusList[3]:

            # if we don't want to read any more lines, break out of the loop
            if acCount > maxLinesToRead:
                break

            if len(sentenceAndTagList[0]) <= 19: # Max length of sentence is 15 + start/stops

                acCount += 1

                # find the tag sequence that is the most likely
                probMaxTags = probInstance.argMaxAllTags(sentenceAndTagList[0], tagCount, wordTagCount, wordTagbigram, wordTagTrigram)
                correctTags = sentenceAndTagList[1]
                tagsFound = probMaxTags[1]
                count = 0
                correctAmount = 0 # The start and stop statements are always correct, so distract 4 later on
                for i in range(0, len(sentenceAndTagList[0])):
                    if len(probMaxTags[1]) > 0:
                        if tagsFound[count] == correctTags[count]: # We used something like the add-1 smoothing to get 
                                                                   # a random tag in this location to not get an empty tag list.
                            correctAmount = correctAmount + 1
                        count = count + 1
                bestTag = probMaxTags[1]

                # the following 5 lines write to an output file
                fileWrite.write('The current sentence is: ' + ' '.join(probMaxTags[0]) + '\n')
                fileWrite.write('The tags gotten from the formula are: ' + str(bestTag[2:-2]) + '\n')
                fileWrite.write('The correct tags were: ' + str(correctTags[2:-2]) + '\n')
                fileWrite.write('Correctly tagged: ' + str(correctAmount-4) + '/' + str(len(sentenceAndTagList[0])-4) + '\n')
                fileWrite.write('The formula gives a probability of (logscale): ' + str(probMaxTags[2]) + '\n\n')
                
                # these 5 lines contain the same information as the previous ones but these are output to the terminal
                print 'The current sentence is: ' + ' '.join(probMaxTags[0])
                print 'The tags gotten from the formula are: ' + str(bestTag[2:-2])
                print 'The correct tags were: ' + str(correctTags[2:-2])
                print 'Correctly tagged: ' + str(correctAmount-4) + '/' + str(len(sentenceAndTagList[0])-4)
                print 'The formula gives a probability of (logscale): ' + str(probMaxTags[2])
                print
                totalCorrect+= correctAmount-4
                totalConsidered += len(sentenceAndTagList[0])-4
        fileWrite.close()

        print "Accuracy = " + str(totalCorrect) + "/"+ str(totalConsidered) + "(" + str((totalCorrect / totalConsidered) * 100) + "%)"

        # get the new time, so a benchmark can be made 
        newTime = datetime.datetime.time(datetime.datetime.now())

        print oldTime
        print newTime

    #Takes care of provided arguments, if none given use default!
    def argumentReader(self):
        # Make a nice way to handle command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-train-set', help='Provide a text corpus file in the .pos format to perform an N-gram calculation and probabilities.', required=True)
        parser.add_argument('-test-set', help='Provide a text corpus file in the .pos format to test our calculations on another corpus.', required=True)
        parser.add_argument('-test-set-predicted', required=True)
        args = parser.parse_args()

        self.trainSet = args.train_set
        self.testSet = args.test_set
        self.testSetPredicted = args.test_set_predicted

    # This method parses a file based on the rules given by the corpus.
    # Certain symbols are ignored, and the rest of the words and their tags are saved. 
    # Returns: a list of sentences, a list of tags, a list of words combined with tags, a list of sentences combined with their tags

    def fileReader(self, corpus):
        tagList = []
        tupleList = []

        f = open(corpus, 'r')
        allSentencesList = []
        allSentencesListWithTags = []
        currentSentence = ''
        currentSentenceNoTags = []
        tagSentence = []
        wordTagList = []
        for line in f:
            if not ('======================================' in line):
                line = line.replace('[','')
                line = line.replace(']','')

                if not ('./.' in line):
                    currentSentence += line
                else :
                    line = line.replace('./.','')
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
                            if '|' in tag:
                                split = tag.split('|')
                                tag = split[0]
                            wordTagList.append((word,tag))
                            tagList.append(tag)
                            tagSentence.append(tag)
                    allSentencesList.append(currentSentenceNoTags)
                    allSentencesListWithTags.append((currentSentenceNoTags, tagSentence))
                    currentSentence = ''
                    currentSentenceNoTags = []
                    currentSentenceList = []
                    tagSentence = []
        return (allSentencesList, tagList, wordTagList, allSentencesListWithTags)