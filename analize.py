import pygal
from pygal.style import Style

class Analize:
    def __init__(self, tweets, Required, date, number):
        self.tweets = tweets
        self.required = Required[:]
        self.date = date
        self.guesses = []
        self.number = number
        self.GreenLetter = []
        self.YellowLetter = []
        self.GreyLetter = []
    
    def countGuesses(self):
        index = 0
        l1 = []
        for twet in self.tweets:
            doubleCheck = False
            g = 0
            gCheck= 0
            tx = twet.text
            for char in range(0, len(tx)):
                if tx[char] == 'W':
                    if tx[char+0:char+10] == self.number:
                        temp = char
                        while tx[temp] != '/':
                            if temp+1 < len(tx):
                                temp+=1
                            else:
                                break
                        if tx[temp] == '/' and tx[temp+1] == '6':
                            g = tx[temp-1]
                temp = char
                while tx[temp] in self.required and not doubleCheck:
                    gCheck+=1
                    if (temp+6) < len(tx):
                        temp+=6
                    else:
                        break
                if gCheck > 0:
                    doubleCheck = True
            if g == str(gCheck) or g == 'X':
                self.guesses.append(g)
                l1.append(tx)
            else:
                self.tweets.pop(index)
            index+=1
        self.tweets = l1
        return self.guesses

    def countcolors(self):
        output = []
        for twet in self.tweets:
            yellow = 0
            grey = 0
            green = 0
            for i in twet:
                if i in self.required:
                    if i == '🟩':
                        green+=1
                    elif i ==  '🟨' :
                        yellow+=1
                    elif i == '⬛' or i == '⬜':
                        grey+=1
            self.GreenLetter.append(green)
            self.GreyLetter.append(grey)
            self.YellowLetter.append(yellow)
        output.append(self.GreenLetter)
        output.append(self.GreyLetter)
        output.append(self.YellowLetter)
        return output
    
    def extraCalculations(self):
        GLetters = [[],[],[],[],[],[],[]]
        YLetters= [[],[],[],[],[],[],[]]
        GREYLetters = [[],[],[],[],[],[],[]]
        green = self.GreenLetter
        yellow = self.YellowLetter
        grey = self.GreyLetter
        for i in range(0,len(self.guesses)):
            if self.guesses[i] == 'X':
                GLetters[-1].append(green[i])
                YLetters[-1].append(yellow[i])
                GREYLetters[-1].append(grey[i])
            else:
                for num in range(1,7):
                    if self.guesses[i] == str(num):    
                        GLetters[num-1].append(green[i])
                        YLetters[num-1].append(yellow[i])
                        GREYLetters[num-1].append(grey[i])
                        break
        return GLetters, YLetters, GREYLetters

    def createGraph(self, data,Filename):
        custom_style = Style(
            font_family='googlefont:Roboto',
            background='white',
            plot_background='white',
            foreground='black',
            foreground_strong='black',
            foreground_subtle='black',
            opacity='1',
            colors=('#1E9B52', '#b7a93e','#3a3a3c')
            )
        bar_chart = pygal.Bar(fill=True, style=custom_style)
        bar_chart.title = 'Number of Green Letters, Yellow Letters, and Grey Lettters \n by Number of Guesses'
        bar_chart.x_labels = map(str, ('Guess 1', 'Guess 2', 'Guess 3', 'Guess 4', 'Guess 5','Guess 6','Failed',))
        bar_chart._y_title = 'Number of Letters'
        bar_chart.add('Green Letters',  [data[0][0], data[1][0], data[2][0], data[3][0], data[4][0], data[5][0],data[6][0]])
        bar_chart.add('Yellow Letters', [data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1],data[6][1]])
        bar_chart.add('Grey Letters',   [data[0][2], data[1][2], data[2][2], data[3][2], data[4][2], data[5][2],data[6][2]])
        # fileSvg = f'W:\CODE\python\FinalProjectContinued\WordleTwitterBot/{str(Filename)}.svg'
        bar_chart.render_to_file(fileSvg)

    def __str__(self):
        return self.guesses