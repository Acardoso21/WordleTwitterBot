alphabet = ("a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
vowels = ('a','e','i','o','u','y')

class wordleSolver:
    def __init__(self, wordpool):
        self.wordpool = wordpool
        self.allwords = wordpool
        self.blackLetters = []
        self.yellow_info = []
        self.green_info = []
        self.NextGuess = ""

    def addAllletters(self, bletters, yletters, gletters):
        self.addBlackLetter(bletters)
        self.addYellowLetter(yletters['letters'], yletters['locations'])
        self.addGreenLetters(gletters['letters'], gletters['locations'])

    def addBlackLetter(self, letters):
        temp = []
        for x in range(0,len(letters)):
            if letters[x] not in self.yellowLetters:
                if letters[x] not in self.greenLetters:
                    temp.append(letters[x])
        self.blackLetters += temp
    
    def addYellowLetter(self, letters, locations):
        temp = []
        for x in range(0, len(letters)):
            if letters[x] not in self.greenLetters:
                temp.append({'letter': letters[x], 'location': locations[x]})
        self.yellow_info += temp

    def addGreenLetters(self, letters, locations):
        self.green_info += [{'letter': letters[i], 'location': locations[i]} for i in range(len(letters))]

            
    def CalculateWords(self):
        # Step 1: Remove words containing black letters
        out = []
        for i in range(0, len(self.wordpool)):
            c = 0
            for x in range(0, 5):
                for letter_info in self.blackLetters:
                    if self.wordpool[i][x] == letter_info['letter']:
                        c += 1
            if c == 0:
                out.append(self.wordpool[i])
        self.wordpool = out[:]  # Update wordpool without words containing black letters

        # Step 2: Remove words not matching yellow letters and locations
        if len(self.yellow_info) >= 1:
            out2 = []
            for i in range(0, len(self.wordpool)):
                c = 0
                for letter_info in self.yellow_info:
                    for x in range(0, 5):
                        # Check if the yellow letter is at the correct location
                        if letter_info['location'] == x and self.wordpool[i][x] == letter_info['letter']:
                            c += 1
                        # Check if the word contains the yellow letter at any other location
                        elif letter_info['location'] != x and self.wordpool[i][x] == letter_info['letter']:
                            c += 1
                # If the count of matching yellow letters is equal to or greater than the expected count
                if c >= len(self.yellow_info):
                    out2.append(self.wordpool[i])
            self.wordpool = out2[:]  # Update wordpool without words not matching yellow letters and locations

        # Step 3: Remove words not matching green letters and locations
        if len(self.green_info) > 0:
            out3 = []
            for i in range(0, len(self.wordpool)):
                c = 0
                for letter_info in self.green_info:
                    # Check if the green letter is at the correct location
                    if self.wordpool[i][letter_info['location']] == letter_info['letter']:
                        c += 1
                    else:
                        c = c
                # If the count of matching green letters is greater than the expected count minus one
                if c > len(self.green_info) - 1:
                    out3.append(self.wordpool[i])
            self.wordpool = out3[:]  # Update wordpool without words not matching green letters and locations


    def getWords(self):
        return self.wordpool

    def getWordsIndex(self, index):
        return self.wordpool[index]

    def SortWords(self):
        # Copy the wordpool to avoid modifying the original list
        words = self.wordpool[:]

        # Initialize lists to store letter frequencies for each word position
        one = [0] * 26
        two = [0] * 26
        three = [0] * 26
        four = [0] * 26
        five = [0] * 26
        six = [0] * 26
        seven = [0] * 26
        eight = [0] * 26

        # Loop through each word in the wordpool
        for i in range(len(words)):
            # Loop through each character position in the current word
            for x in range(0, len(words[0])):
                # Loop through each character in the alphabet
                for j in range(len(alphabet)):
                    # Check if the current character in the word matches the alphabet
                    if words[i][x] == alphabet[j]:
                        # Increment the corresponding frequency count based on the position and word length
                        if x == 0:
                            one[j] += 1
                        if x == 1:
                            two[j] += 1
                        if len(words[i]) >= 3 and x == 2:
                            three[j] += 1
                        if len(words[i]) >= 4 and x == 3:
                            four[j] += 1
                        if len(words[i]) >= 5 and x == 4:
                            five[j] += 1
                        if len(words[i]) >= 6 and x == 5:
                            six[j] += 1
                        if len(words[i]) >= 7 and x == 6:
                            seven[j] += 1
                        if len(words[i]) >= 8 and x == 7:
                            eight[j] += 1
        
        # Custom sorting algorithm based on a rating system.
        
        # Parameters:
        # - words (list): List of words to be sorted.
        # - alphabet (list): List of characters in the alphabet.
        # - one, two, three, four, five (list): Lists representing the weights for each alphabet position.

        # The sorting algorithm assigns a rating to each word based on the weights given to each alphabet position.
        # The higher the rating, the higher the word is placed in the sorted list.
        
        out = [] # Output list to store ratings
        for i in range(len(words)):
            out.append(0)
            for x in range(0,5):
                for j in range(len(alphabet)):
                    v=0
                    if words[i][x] == alphabet[j]:
                        # Additional logic for vowels (currently commented out)
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
        # Sorting based on the calculated ratings

        rating = out[:]
        n = len(rating)
        for i in range(n):
            for j in range(0, n-i-1):
                if rating[j] < rating[j+1] :
                    rating[j], rating[j+1] = rating[j+1], rating[j]
                    words[j], words[j+1] = words[j+1], words[j]
        # Update the wordpool attribute with the sorted words

        self.wordpool = words[:]
        self.NextGuess = self.wordpool[0]
        # return words

    def guess(self):
        return self.NextGuess
        

    def __str__(self):
        return f'Green Letters: {self.green_info}, Yellow Letters: {self.yellow_info}, Black Letters: {self.blackLetters}'




        