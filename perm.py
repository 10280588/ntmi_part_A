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
        perms = itertools.permutations(corpusList)
        for perm in perms:
            perm = '<s> '+ ' '.join([str(i) for i in perm]) + ' </s>'
            permList.append(perm)
        return permList
