alphabet = ("a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
vowels = ('a','e','i','o','u','y')

class wordleSolver:
    def __init__(self, wordpool):
        self.wordpool = wordpool
        self.allwords = wordpool
        self.blackLetters = []
        self.yellowLetters = []
        self.yellowLocations = []
        self.greenLetters = []
        self.greenLocations = []

    def addBlackLetter(self, letters):
        temp = []
        for x in range(0,len(letters)):
            if letters[x] not in self.yellowLetters:
                if letters[x] not in self.greenLetters:
                    temp.append(letters[x])
        self.blackLetters += temp
    
    def addYellowLetter(self, letters, locations):
        temp = []
        temp2 = []
        for x in range(0, len(letters)):
            if letters[x] not in self.greenLetters:
                temp.append(letters[x])
                temp2.append(locations[x])
        self.yellowLetters += temp
        self.yellowLocations += temp2
                    
    def addGreenLetters(self, letters, locations):
        self.greenLetters += letters
        self.greenLocations += locations

    def CalculateWords(self):
        out = []
        for i in range(0,len(self.wordpool)):
            c = 0
            for x in range(0,5):
                for j in range(0,len(self.blackLetters)):
                    if self.wordpool[i][x] == self.blackLetters[j]:
                        c=c+1
            if c == 0:
                out.append(self.wordpool[i])
        self.wordpool=out[:]

        if len(self.yellowLetters) >= 1:
            out2 = []
            for i in range(0,len(self.wordpool)):
                c=0
                for j in range(0,len(self.yellowLetters)):
                    for x in range(0,5):
                        if self.yellowLocations[j] == x:
                            c=c
                        elif self.wordpool[i][x] == self.yellowLetters[j]:
                            c=c+1
                            break #fix this
                if c >= len(self.yellowLetters):
                    out2.append(self.wordpool[i])
            self.wordpool = out2[:]

        if len(self.greenLetters) > 0:
            out3 = []
            for i in range(0,len(self.wordpool)):
                c=0
                for j in range(0,len(self.greenLetters)):
                    if self.wordpool[i][self.greenLocations[j]] == self.greenLetters[j]:
                        c=c+1
                    else:
                        c=c
                if c > len(self.greenLetters)-1:
                    out3.append(self.wordpool[i])
            self.wordpool = out3[:]


    def getWords(self):
        return self.wordpool

    def getWordsIndex(self, index):
        return self.wordpool[index]

    def SortWords(self):
        words = self.wordpool[:]
        one = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
        two = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        three = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        four = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        five = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        for i in range(len(words)):
            for x in range(0,5):
                for j in range(len(alphabet)):
                    if words[i][x] == alphabet[j]:
                        if x == 0:
                            one[j] = one[j]+1
                        if x == 1:
                            two[j] = two[j]+1
                        if x == 2:
                            three[j] = three[j]+1
                        if x == 3:
                            four[j] = four[j]+1
                        if x == 4:
                            five[j] = five[j]+1

        out = []
        for i in range(len(words)):
            out.append(0)
            for x in range(0,5):
                for j in range(len(alphabet)):
                    v=0
                    if words[i][x] == alphabet[j]:
                        # if words[i][x] in vowels:
                        #     v = 100
                        if x == 0:
                            out[i] = out[i] +  one[j] + v 
                        if x == 1:
                            out[i] = out[i] +  two[j] + v 
                        if x == 2:
                            out[i] = out[i] +  three[j] + v 
                        if x == 3:
                            out[i] = out[i] +  four[j] + v 
                        if x == 4:
                            out[i] = out[i] +  five[j] + v 
        rating = out[:]
        n = len(rating)
        for i in range(n):
            for j in range(0, n-i-1):
                if rating[j] < rating[j+1] :
                    rating[j], rating[j+1] = rating[j+1], rating[j]
                    words[j], words[j+1] = words[j+1], words[j]
        self.wordpool = words[:]
        return words

        

    def __str__(self):
        return f'Green Letters: {self.greenLetters}, Yellow Letters: {self.yellowLetters}, Black Letters: {self.blackLetters}'




        