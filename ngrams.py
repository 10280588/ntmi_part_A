#######
# Copyright: Menno van Leeuwen (10280588)
# Assignment: NTMI step 1
#
class Ngrams():
	#make variables and call relevant methods
	def __init__(self, corpus, n, m, tmp):
		self.tmp = tmp
		self.n = n
		self.m = m
		self.corpusList = corpus
		self.tmp = tmp
		self.sorted_nGrams = {}
		self.sumFreq = 0

		self.calculateNGram()
		self.mostFrequent()
		self.sumOfFrequencies()
		#self.resultPrinter()

	# The real calculation of occurences is done in this method
	def calculateNGram(self):
		print 'Calculating N-Gram'
		for i in range(0, len(self.corpusList) - (self.n-1)):
			sequence = self.corpusList[i];
			for j in range(1, self.n):
				sequence = sequence + " " + self.corpusList[i+j]
			if (sequence in self.tmp):
				self.tmp.update({sequence:(self.tmp[sequence]+1)})
			else:
				if not "</s> <s>" in sequence and not "<s> </s>" in sequence:
					self.tmp.update({sequence:1})
		
	# Look for most frequent occurences, and safe them.
	def mostFrequent(self):
		self.sorted_nGrams = sorted(self.tmp.items(), key=lambda nGram: nGram[1], reverse=True)

	# Sum up all frequencies, for n = 1 this should be the same as the number of words
	def sumOfFrequencies(self):
		for i in range(0, len(self.sorted_nGrams)):
			self.sumFreq = self.sumFreq + self.sorted_nGrams[i][1]

	# Print all our findings
		