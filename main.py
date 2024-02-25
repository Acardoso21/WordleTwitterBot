from credentails import Credentails
import time

#THIS MAIN FILE WAS MADE IN 2022 FOR A COLLEGE PROJECT AND IS NO LONGER FUNCTIONAL

userName = 'WordleGuessAve'
a1 = Credentails()
term = str(a1.WordleNumber())
a1.search(term)
a1.analize()
TwitterR = a1.getAverage()
TwitterDetails = a1.detailStats()
TwitterR = ""
details = ""
box = ''
ComputerR = ""
greenSquare = "🟩"

for i in range(0,7):
    if i == 6:
        box = '❌'
    else:
        box = (greenSquare*(i))+("✅") 
    details += box + " " + str(TwitterDetails[i]) + "%" + '\n'

inp=input("Would you like to run the Wordle Solver (Windows10 only, y or n)? ")
if inp == 'y':
    ComputerR = a1.CompareToRobot()
    outPut = (f'Twitter users took {TwitterR} guesses on average  \n' + 
            details +
            f'My wordle solver took {ComputerR} guesses \n') 
else:
    outPut = (f'Todays average number of wordle guesses from twitter users is {TwitterR} \n' + details)
posted = a1.PostResults(outPut + '#Wordle #WordleStats')
a1.SaveContent(str(ComputerR), str(TwitterR))
time.sleep(10)
posted = True
if posted:
    inp = input("Would you like to post more details in a reply to your first tweet (y or n)?")
    if inp == 'y':
        userID = a1.searchbyName(userName)
        tweetID = a1.get_latest_tweet_byID(userID)
        content = a1.ExtraStats()
        a1.respondToTweetByID(tweetID, content)
        inp = input("Would you like to save a graph with the extra data (saved as an SVG file) (y or n)?")
        if inp == 'y':
            a1.GraphData()
    a1.UpdateWordleNumber()
print("Program Done")