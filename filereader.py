
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
        corpusList = []
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

    def lineReader(self, corpus, n):
        lineList = []
        f = open(corpus, 'r')
        for line in f:
            lineLength = len(line.split())
            prefix = '<s> ' * (lineLength-1)
            postfix = ' </s>' * (lineLength-1)
            line = line.rstrip()
            line = prefix + line + postfix
            if(lineLength == n):
                if line.strip():
                    lineList.append(line)
        f.close()
        return lineList
