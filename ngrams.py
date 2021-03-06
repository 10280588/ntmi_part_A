#######
# Copyright: Menno van Leeuwen (10280588), Jelmer Alphenaar (10655751), Yuri Sturkenboom (10639748)
# Assignment: NTMI step 4
#
class Ngrams():
	# The real calculation of occurences is done in this method
	# It generates ngrams of length n given a corpus.
	def calculateNGram(self, corpus, n):
		print 'Calculating N-Gram with n = ' + str(n)
		ngrams = {}
		for i in range(0, len(corpus) - (n-1)):
			sequence = corpus[i];
			for j in range(1,n):
				sequence = sequence + " " + corpus[i+j]
			if (sequence in ngrams):
				ngrams.update({sequence:(ngrams[sequence]+1)})
			else:
				if not "</s> <s>" in sequence and not "<s> </s>" in sequence:
					ngrams.update({sequence:1})
		return ngrams

	# Look for most frequent occurences, and safe them.
	def mostFrequent(self, ngrams):
		sorted_nGrams = sorted(ngrams.items(), key=lambda nGram: nGram[1], reverse=True)
		return sorted_nGrams

	# Sum up all frequencies, for n = 1 this should be the same as the number of words
	def sumOfFrequencies(self, sorted_nGrams):
		sumFreq = 0
		for i in range(0, len(sorted_nGrams)):
			sumFreq = sumFreq + sorted_nGrams[i][1]
		return sumFreq
