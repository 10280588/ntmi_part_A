from __future__ import division
import sys
import smooth
import itertools

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
                
            tagList.append(tags)
            for item in wordTagValue:
                wordTagValueList.update({item[0]: item[1]})
            wordTagValue = []
            tags = []
        
        # Get the best probability from all permutations possible
        maxProb = 0
        bestTag = []
        for tag in itertools.product(*tagList):
            probTags = self.probTagsGivenSentence(sentence, tag, wordTagValueList, tagCount, bigram, trigram)
            if probTags > maxProb:
                maxProb = probTags
                bestTag = tag
        tag = tag[2:-2]
        currentSentence = sentence[2:-2]
        print 'The current sentence is: ' + ' '.join(currentSentence)
        print 'The tags gotten from the formula are: ' + str(tag)
        print 'The formula gives a probability of: ' + str(maxProb)
            
    # no smoothing used yet
    # using trigrams
    def probTagsGivenSentence(self, sentence, tag, wordTagListCount, tagListCount, bigram, trigram):
        
        # Language model
        tagLength = len(tag)
        languageProduct = 1
        
        for i in range(0, tagLength-2):
            trigramPartSentence = tag[i] + ' ' + tag[i+1] + ' ' + tag[i+2]
            trigramPart = tag[i] + ' ' + tag[i+1]
            trigramCount = trigram.get(trigramPartSentence, None)
            if trigramCount != None:
                bigramCount = bigram.get(trigramPart, None)
                if bigramCount != 0:
                    prob3 = trigramCount/bigramCount
            languageProduct = languageProduct * prob3
            
        # Task model
        taskProduct = 1    
        for i in range(0, tagLength):
            wordTagValue = wordTagListCount.get((sentence[i], tag[i]))
            tagValue = tagListCount.get(tag[i])
            probTag = wordTagValue/tagValue
            taskProduct = taskProduct * probTag
            
        # Acquired values used to calculate probability
        probTagsGivenSentenceValue = taskProduct * languageProduct
        return probTagsGivenSentenceValue