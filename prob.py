#######
# Copyright: Menno van Leeuwen (10280588), Jelmer Alphenaar (10655751), Yuri Sturkenboom (10639748)
# Assignment: NTMI step 4
#

from __future__ import division
import sys
import smooth
import itertools
import math
class Prob():

    # most probable tag sequence given input sentence (list of words)
    def argMaxAllTags(self, sentence, tagCount, wordTagCount, bigram, trigram):
        wordTagValue = []
        wordTagValueList = {}
        tags = []
        tagList = []

        for word in sentence:
            found = 0
            for key, value in wordTagCount.iteritems():
                if key[0] == word:
                    found = 1
                    wordTagValue.append((key, value))
            if found != 1:
                key = (word, 'ANY')
                wordTagValue.append((key, 1)) # Assign 1 to unseen words, this is our smoothing
            for occurences in wordTagValue:
                tupleWordTag = occurences[0]
                tags.append(tupleWordTag[1])
                wordTagValueList.update({occurences[0]: occurences[1]})

            tagList.append(tags)
            wordTagValue = []
            tags = []

        # Get the best probability from all permutations possible
        maxProb = 0
        maxProbLog = 0
        bestTag = []
        for tag in itertools.product(*tagList):
            probTags = self.probTagsGivenSentence(sentence, tag, wordTagValueList, tagCount, bigram, trigram)
            if probTags > maxProb:
                maxProb = probTags
                if maxProb > 0:
                    maxProbLog = math.log10(maxProb)
                bestTag = tag
        currentSentence = sentence[2:-2]
        return (currentSentence, bestTag, maxProbLog)

        # We used some hacky smoothing technique above
    def probTagsGivenSentence(self, sentence, tag, wordTagListCount, tagListCount, bigram, trigram):
        
        tagLength = len(tag)
        
        # Language model
        languageProduct = 1
        for i in range(0, tagLength-2):
            trigramPartSentence = tag[i] + ' ' + tag[i+1] + ' ' + tag[i+2]
            trigramPart = tag[i] + ' ' + tag[i+1]
            trigramCount = trigram.get(trigramPartSentence, 0) + 1
            bigramCount = bigram.get(trigramPart, 0) + 1
            probLang = trigramCount/bigramCount
            languageProduct = languageProduct * probLang

        # Task model
        taskProduct = 1
        for i in range(0, tagLength):
            wordTagValue = wordTagListCount.get((sentence[i], tag[i]), 0) + 1
            tagValue = tagListCount.get(tag[i], 0) + 1
            probTag = wordTagValue/tagValue
            taskProduct = taskProduct * probTag

        # Acquired values used to calculate probability
        probTagsGivenSentenceValue = taskProduct * languageProduct
        return probTagsGivenSentenceValue
