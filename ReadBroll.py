class ReadBroll():
    def __init__(self, location):
        self.file = open(location, 'r')
        self.lines = self.file.readlines()

        self.source_txt = []

        for self.line in self.lines:
            if self.line[-1] == '\n':
                self.source_txt.append(self.line[:-1])
            else:
                self.source_txt.append(self.line)
    
    def getLines(self):
        self.lines = []
        for self.keys in self.source_txt:
            if self.keys != '' and self.keys != None:
                self.lines.append(self.keys)
                
        return self.lines

    def getKeywords(self):
        self.keyWords = []
        for self.line in self.lines:
            for self.words in self.line.split():
                if self.words[0] == '!' and self.words[-1] == '!':
                    self.keyWords.append(self.words[1:-1])
        if len(self.keyWords) == 0:
            return "No keywords found!, To get a keyword please surround the keyword with '!' (eg: !green!)"
        else:
            return self.keyWords

