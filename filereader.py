
class Reader():

    def fileReaderStep1(self, corpus):
        corpusList = []
        f = open(corpus, 'r')
        for line in f:
            for word in line.split():
                corpusList.append(word)
        f.close()
        return corpusList

    def fileReader(self, corpus, n):
        #if texttype == "paragraph" or texttype == "paragraph2":
        test = self.changeText(corpus, n)

        #elif texttype == "lines":
        #    f = open(corpus, 'r')
        #    for line in f:
        #       lst = line.split()
        #       if(len(lst) == n):
        #            if line.strip():
        #                for x in range(1, n):
        #                    self.probList.append(["<s>"])
        #                    self.probList.append(lst)
        #                    for x in range(1, n):
        #                        self.probList.append(["</s>"])
        #                    self.probList.append(" ")
        #    f.close()
        #    self.probList = [item for sublist in self.probList for item in sublist]

        return test
    def changeText(self, corpus, n):
        corpusList = []
        print n
        #if texttype == "paragraph":
        #    n = self.n
        #elif texttype == "paragraph2":
        #    n = self.n-1

        for x in range(1, n):
            corpusList.append(["<s>"])
        f = open(corpus, 'r')
        for line in f:
            if not line.strip():
                for x in range(1, n):
                    corpusList.append(["</s>"])
                for x in range(1, n):
                    corpusList.append(["<s>"])
            else:
                corpusList.append(line.split())
        for x in range(1, n):
            corpusList.append(["</s>"])
        corpusList = [item for sublist in corpusList for item in sublist]

        return corpusList
        #
        #if texttype == "paragraph":
        #    self.corpusList = tmp
        #if texttype == "paragraph2":
        #    self.corpusList2 = tmp
