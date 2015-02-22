import itertools


class Permutation():
    def __init__(self):
        print ''
        #self.corpus = corpus
        #self.list = ['one','two']
        ## find all permutations of a list and calculate their probability
        #self.createList()
        #self.probabilityOfPermutations()

    def allPermutations(self, corpusList):
        permList = []
        print 'check'
        perms = itertools.permutations(corpusList)
        print perms
        for perm in perms:
            #perm = list(perm)
            print perm
            perm = '<s> '+ ' '.join([str(i) for i in perm]) + ' </s>'
            print perm
            perm =  perm.split()
            permList.extend(perm)
        print permList
        return permList

    def probabilityOfPermutations(self, corpusList):
        print 'calculating all permutations of the provided words words:'
        #find all permutations
        perms = itertools.permutations(self.list)
        for perm in perms:

            print perm
            #add start and stop signs

            #calculate probabilities of permutation /// needs to be implemented
            #prob = calculateProbability(perm)
            #print
            #print 'perm: ' + perm
            #print 'probability ' + prob
    print ' -------------------------------'
