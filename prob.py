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
            for key, value in wordTagCount.iteritems():
                if key[0] == word:
                    wordTagValue.append((key, value))

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

        # Still needs smoothing
    def probTagsGivenSentence(self, sentence, tag, wordTagListCount, tagListCount, bigram, trigram):

        # Language model
        tagLength = len(tag)
        languageProduct = 1

        for i in range(0, tagLength-2):
            probLang = 0
            trigramPartSentence = tag[i] + ' ' + tag[i+1] + ' ' + tag[i+2]
            trigramPart = tag[i] + ' ' + tag[i+1]
            trigramCount = trigram.get(trigramPartSentence, None)
            if trigramCount != None:
                bigramCount = bigram.get(trigramPart, None)
                if bigramCount != None:
                    probLang = trigramCount/bigramCount
            languageProduct = languageProduct * probLang

        # Task model
        taskProduct = 1
        for i in range(0, tagLength):
            probTag = 0
            wordTagValue = wordTagListCount.get((sentence[i], tag[i]), None)
            tagValue = tagListCount.get(tag[i], None)
            if wordTagValue != None and tagValue != None:
                probTag = wordTagValue/tagValue
            taskProduct = taskProduct * probTag

        # Acquired values used to calculate probability
        probTagsGivenSentenceValue = taskProduct * languageProduct
        return probTagsGivenSentenceValue
