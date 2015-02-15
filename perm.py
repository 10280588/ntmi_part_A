import itertools


class Permutation():
    def __init__(self, corpus):
        self.corpus = corpus
        self.list = ['one','two']
        # find all permutations of a list and calculate their probability
        self.createList()
        self.probabilityOfPermutations()


    def createList(self):
            f = open(self.corpus, 'r')
            words= [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
            self.list = words # or `print(words)` if you want to print out `words` as a list
            f.close()
    def probabilityOfPermutations(self):
        print 'calculating all permutations of the provided words words:'
        #find all permutations
        perms = itertools.permutations(self.list)
        for perm in perms:
            perm = list(perm)
            print perm
            #add start and stop signs
            #perm = '<s>'+ str(perm) + '</s>'
            #calculate probabilities of permutation /// needs to be implemented
            #prob = calculateProbability(perm)
            #print
            #print 'perm: ' + perm
            #print 'probability ' + prob
    print ' -------------------------------'
