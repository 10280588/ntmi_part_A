from __future__ import division
import sys
import smooth
import itertools

class Prob():
    
    # most probable tag sequence given input sentence (list of words)
    # wordtaglist = bigrams
    # taglist = ngrams
    def argMaxTags(self, sentence, tagCount, wordTagCount):
        print tagCount
        alltags = []
        tagOccurence = {}
        wordTagValueList = []
        tags = []
        tagList = []
        for word in sentence:
            for key, value in wordTagCount.iteritems():
                
                if key[0] == word:
                    wordTagValueList.append((key, value))
            print 'zijn dit ze ' + str(wordTagValueList)
            
            for occurences in wordTagValueList:
                print occurences
                tupleWordTag = occurences[0]
                tags.append(tupleWordTag[1])
                
            print tags
            tagList.append(tags)
            wordTagValueList = []
            tags = []
            
            print tagList
            #print itertools.product(*tagList)
        count = 0
        for element in itertools.product(*tagList):
            count = count+1
            print element
            
            #tagOccurence = {}
            
        #for word in
        print 'hoi ' + str(count)
        self.taskModel(sentence, count, tags, wordTagValueList, wordTagCount)
        
    def taskModel(self, sentence, permutationCount, tags, wordTagListCount, tagListCount):
        print sentence
        print tags
        count = 0
        print 'hoi2 ' + str(permutationCount)
        for i in range(0, permutationCount):
            for word in sentence:
                c = 1
            #print wordTagListCount
                #for tag in tags[count]:
                 #   count = count
            #count = count + 1
                #tagListCount.get(tags[count]) #no
                #wordTagListCount/tagListCount
        #for tuples, value in wordTagCount.iteritems():
        #return wordTagListCount/tagListCount
            
            
            
            
            
            
            
            
            
            
            
            
        #count = 0
        #for word in sentence:
        #    print word
        #    for tuples, value in tagOccurence.iteritems():
            #    if tuples[0] == word:
            #        print tuples[1]
            
        #print tagOccurence
            #alltags.append(tags)
           
        #print alltags
        
        #for element in alltags:#itertools.product(alltags):
        #    print element
        
    
    #def calcProbNgram(self, ngram, ngramMin1):
    #    probDict = {}
    #    for key in ngram:
    #        biKey = key.rsplit(' ',1)[0]
    #        numerator = ngram.get(key,None)
    #        if biKey in ngramMin1:
    #            denominator = ngramMin1.get(biKey, None)
    #        prob = numerator/denominator
    #        probDict.update({key: prob})
            
            
            
          
       # return probDict