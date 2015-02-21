

class Smooth():
    def add1(self, ngram):
        smoothedNgram = {key: value+1 for (key, value) in ngram.iteritems()}
        return smoothedNgram
