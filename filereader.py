
class Reader():

    def fileReaderStep1(self, corpus):
        corpusList = []
        f = open(corpus, 'r')
        for line in f:
            for word in line.split():
                corpusList.append(word)
        f.close()
        return corpusList

    def fileReader(self, texttype):
        if texttype == "paragraph" or texttype == "paragraph2":
            self.changeText(texttype)

        elif texttype == "lines":
            f = open(self.cp, 'r')
            for line in f:
               lst = line.split()
               if(len(lst) == self.n):
                    if line.strip():
                        for x in range(1, self.n):
                            self.probList.append(["<s>"])
                            self.probList.append(lst)
                            for x in range(1, self.n):
                                self.probList.append(["</s>"])
                            self.probList.append(" ")
            f.close()
            self.probList = [item for sublist in self.probList for item in sublist]

    def changeText(self, texttype):
        tmp = []
        if texttype == "paragraph":
            n = self.n
        elif texttype == "paragraph2":
            n = self.n-1

        for x in range(1, n):
            tmp.append(["<s>"])
        f = open(self.corpus, 'r')
        for line in f:
            if not line.strip():
                for x in range(1, n):
                    tmp.append(["</s>"])
                for x in range(1, n):
                    tmp.append(["<s>"])
            else:
                tmp.append(line.split())
        for x in range(1, n):
            tmp.append(["</s>"])
        tmp = [item for sublist in tmp for item in sublist]
        if texttype == "paragraph":
            self.corpusList = tmp
        if texttype == "paragraph2":
            self.corpusList2 = tmp
