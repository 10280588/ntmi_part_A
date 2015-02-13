#######
# Copyright: Menno van Leeuwen (10280588)
# Assignment: NTMI step 1
#
import itertools

class Ngrams():
	#make variables and call relevant methods
	def __init__(self, corpus, n, m):
		self.n = n
		self.m = m
		self.corpusList = corpus
		self.nGrams = {}
		self.sorted_nGrams = {}
		self.sumFreq = 0

		self.calculateNGram()
		self.mostFrequent()
		self.sumOfFrequencies()
		self.resultPrinter()

	# The real calculation of occurences is done in this method
	def calculateNGram(self):
		print 'Calculating N-Gram'
		for i in range(0, len(self.corpusList) - (self.n-1)):
			sequence = self.corpusList[i];
			for j in range(1, self.n):
				sequence = sequence + " " + self.corpusList[i+j]
			if sequence in self.nGrams:
				self.nGrams.update({sequence:(self.nGrams[sequence]+1)})
			else:
				self.nGrams.update({sequence:1})
		#print self.nGrams

	# Look for most frequent occurences, and safe them.
	def mostFrequent(self):
		self.sorted_nGrams = sorted(self.nGrams.items(), key=lambda nGram: nGram[1], reverse=True)

	# Sum up all frequencies, for n = 1 this should be the same as the number of words
	def sumOfFrequencies(self):
		for i in range(0, len(self.sorted_nGrams)):
			self.sumFreq = self.sumFreq + self.sorted_nGrams[i][1]

	# Print all our findings
	def resultPrinter(self):
		print 'Calculations are done.'
		print
		print 'The top ' + str(self.m) + ' list of most occuring sequences ([word], [frequency]):'
		# Print the m most frequent ngrams.
		for i in range(0, self.m):
			#if the user wants a top 10 list, but there are for example only 5 combinations stop showing and display message.
			if i < len(self.sorted_nGrams):
				if self.sorted_nGrams[i][0] != '':
					print self.sorted_nGrams[i]
			else:
				print 'There were only ' + str(i) + ' combinations, so they all fitted in your top ' + str(self.m) + ' list.'
				break
		print
		print 'The total sum of all sequence frequencies is: ' + str(self.sumFreq)


	# find all permutations of a list and calculate their probability
	def probabilityOfPermutations(self, listo):
		print 'calculate probabilities of all permutations of words: ' #= list
		#find all permutations
		perms = itertools.permutations(listo)
		listperms = []
		for perm in perms:
			#add start and stop signs
			print perm
			perm = list(perm)
			perm = '<s>' + str(perm) + '</s>'
			listperms.append(perm)
			#calculate probabilities of permutation /// needs to be implemented
			#prob = calculateProbability(perm)
			print
			print 'perm: ' + str(perm)
			#print 'probability ' + prob
			print ' -------------------------------'
