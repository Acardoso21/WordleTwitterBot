from Wordle_Solver import wordleSolver
from PIL import ImageGrab
import pyautogui
import time
class Solve:
    def __init__(self):
        self.words = (open("WordleWords.txt", "r").read()).split(',')
        self.a1 = wordleSolver(self.words)
        self.guesses = []
        self.greenL = []
        self.yellowL = []
        self.locationY = []
        self.blackL = []
        self.locationG = []
        self.saveY = [[],[],[],[],[],[]]
        self.saveG = [[],[],[],[],[],[]]
        self.yellow = (183, 169, 62)
        self.green = (30, 155, 82)  
        self.black = (58, 58, 60)
        self.colors = [[],[],[],[],[],[]]
        self.solved = False

    def ComputerGuesses(self):
        x, y = pyautogui.size()
        pyautogui.moveTo(10, (y-10), 0.1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite("Google Chrome",0.1)
        time.sleep(2)
        pyautogui.hotkey("enter")
        time.sleep(1)
        pyautogui.moveTo(x/2, ((y*2)/3), 0.1)
        pyautogui.click()
        pyautogui.hotkey("ctrl", "shift", "n")
        time.sleep(1)
        pyautogui.typewrite("https://www.nytimes.com/games/wordle/index.html")
        pyautogui.hotkey("enter")

        time.sleep(1)
        pyautogui.hotkey("f11")
        pyautogui.moveTo(1180, 297, 0.1)
        pyautogui.click()
        pyautogui.moveTo(800, 270,0.1)
        pyautogui.click()
        self.a1.SortWords()
        Ly = 270
        T = 2
        for j in range(0,6):

            wordpool = self.a1.getWords()[:]
            best = 0
            if best < len(wordpool)-1:
                while wordpool[best] in self.guesses and best <= len(wordpool)-2:
                    best +=1            
            try:
                pyautogui.typewrite(wordpool[best],0.1)
                self.guesses.append(wordpool[best][:])
            except:
                print("Something went wrong, Check that wordle site did not have problems")
            pyautogui.hotkey('enter')

            time.sleep(T)
            T += 0.5
            Lx = 800

            for i in range (0,5):
                pyautogui.moveTo(Lx, Ly,0.1)
                pixel1=ImageGrab.grab().load()
                pxcolor1=pixel1[pyautogui.position()]
                if pxcolor1 == self.yellow:
                    self.yellowL.append(self.guesses[j][i])
                    self.locationY.append(i)
                elif pxcolor1 == self.green:
                    self.greenL.append(self.guesses[j][i])
                    self.locationG.append(i)
                elif pxcolor1 == self.black:
                    self.blackL.append(self.guesses[j][i])
                else:
                    self.blackL.append(self.guesses[j][i])
                Lx = Lx+67
            Ly = Ly + 67

            #calculate the next word here
            self.a1.addGreenLetters(self.greenL, self.locationG)
            self.a1.addYellowLetter(self.yellowL,self.locationY)
            self.a1.addBlackLetter(self.blackL)
            self.a1.CalculateWords()
            self.a1.SortWords()
            self.saveG[j] = self.greenL[:]
            self.saveY[j] = self.yellowL[:]
            time.sleep(2)
            pixel1=ImageGrab.grab().load()
            pxc=pixel1[1010,665]
            if pxc == self.green:
                print('Wordle Solved')
                self.solved = True
                break
            self.yellowL.clear
            self.locationY.clear
            self.greenL.clear
            self.locationG.clear
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('ctrl', 'w')
        if self.solved:
            return len(self.guesses)
        else:
            return "X"

