import tweepy
import os
from datetime import datetime, timedelta
from analize import Analize
# from pyautogui_SolveMain import Solve

class Credentails:
    def __init__(self):
        # Fetch credentials securely from environment variables
        self.Access_Token = os.environ('TWITTER_ACCESS_TOKEN')
        self.Access_Token_Secret = os.environ('TWITTER_ACCESS_TOKEN_SECRET')
        self.API_key = os.environ('TWITTER_API_KEY')
        self.API_secret_key = os.environ('TWITTER_API_KEY_SECRET')
        self.Bearer_Token = os.environ('TWITTER_BEARER_TOKEN')  
        if not self.Access_Token:
            print("TWITTER_ACCESS_TOKEN not found")
        if not self.Access_Token_Secret:
            print("TWITTER_ACCESS_TOKEN_SECRET not found")
        if not self.API_key:
            print("TWITTER_API_KEY not found")
        if not self.API_secret_key:
            print("TWITTER_API_KEY_SECRET not found")
        if not self.Bearer_Token:
            print("TWITTER_BEARER_TOKEN not found")
        # Verify if all required credentials are provided
        if not all([self.Access_Token, self.Access_Token_Secret, self.API_key, self.API_secret_key, self.Bearer_Token]):
            raise Exception("Missing Twitter API credentials. Ensure that all necessary environment variables are set.")

        # Set up Tweepy Client using the environment credentials
        try:
            self.client = tweepy.Client(
                bearer_token=self.Bearer_Token,
                consumer_key=self.API_key,
                consumer_secret=self.API_secret_key,
                access_token=self.Access_Token,
                access_token_secret=self.Access_Token_Secret)
        except tweepy.TweepyException as e:
            print(f"Error setting up Tweepy client: {e}")
        
        # Assuming Wordle number is stored locally
        self.currentDate = datetime.today().strftime('%Y-%m-%d')
        self.WordleN = open("WordleNumber.txt", "r").read()
        self.Analyze = Analize(self.tweets, (['🟩', '🟨', '⬛', '⬜']), self.currentDate,self.WordleN)

    def search(self, term:str):
        query = term
        enddate = self.currentDate + "T00:00:00Z"
        startdate = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d') + 'T00:00:00Z'
        for tweet in tweepy.Paginator(self.client.search_recent_tweets, query=query, start_time=startdate, end_time=enddate, max_results=100).flatten(limit=10000):
            self.tweets.append(tweet)
        print(len(self.tweets)," Tweets Found")

    def searchbyName(self, userName:str):
        user = self.client.get_user(username=userName)
        print("User ID Found")
        return user.data.id

    def get_latest_tweet_byID(self, userID):
        tweet = self.client.get_users_tweets(userID)
        data = tweet.data
        id = data[0].id
        print("Tweet ID Found")
        return id

    def respondToTweetByID(self,TweetID, content):
        try:
            for t in content:
                text = self.WordleN + ' \n' + t
                self.client.create_tweet(text=text, in_reply_to_tweet_id=TweetID)
            print("Replays Posted")
        except:
            print("Replays Failed to post")

    def PostResults(self, content):
        t = self.currentDate + '  ' + self.WordleN + '\n' + content
        print(len(t))
        try:
            self.client.create_tweet(text=t)
            print("Tweet Posted")
            return True
        except:
            print("Tweet failed to post, Check tweet is not too long")
            return False

    def analize(self):
        self.data = self.Analyze.countGuesses()
        print('Data Analyzed. ', len(self.data),'Tweets passed')

    def getAverage(self):
        ave = []
        Fail = []
        for i in self.data:
            if i == 'X':
                Fail.append(1)
            else:
                ave.append(int(i))
        try:
            average = round(sum(ave)/len(ave),3)
        except:
            average = 0
        print("Averages Calculated")
        return average

    def detailStats(self):
        stats = [[],[],[],[],[],[],[]]
        averages = []
        for i in self.data:
            for x in range(1,7):
                if i == str(x):
                    stats[x-1].append(1)
            if i == 'X':
                stats[-1].append(1)
        for x in range(0,7):
            averages.append(round(((len(stats[x])/len(self.data))*100), 2))
        print("Detailed Stats Calculated")
        return averages

    def ExtraStats(self):
        self.Analyze.countcolors()
        outPut = []
        aveG = [[],[],[],[],[],[],[]]
        aveY = [[],[],[],[],[],[],[]]
        aveGrey = [[],[],[],[],[],[],[]]
        GLetters, YLetters, GREYLetters = self.Analyze.extraCalculations()
        for x in range(0,7):
            try:
                aveG[x] = round(sum(GLetters[x])/(len(GLetters[x])),2)
            except:
                aveG[x] = "X"
            try:
                aveY[x] = round(sum(YLetters[x])/(len(YLetters[x])), 2)
            except:
                aveY[x] = "X"
            try:
                aveGrey[x] = round(sum(GREYLetters[x])/(len(GREYLetters[x])), 2)
            except:
                aveGrey[x] = "X"
            self.ColorDistrbution.append([])
            self.ColorDistrbution[-1].append(aveG[x])
            self.ColorDistrbution[-1].append(aveY[x])
            self.ColorDistrbution[-1].append(aveGrey[x])
            if x == 6:
                outPut.append("Users that Failed to guesses the wordle had on average:\n" + str(aveG[x]) + '🟩 letters \n' + str(aveY[x]) + '🟨 letters \n' + str(aveGrey[x]) + '⬛ letters \n\n')
            else:
                outPut.append("Users that took "+ str(x+1) +" guesses to get the wordle had on average:\n" + str(aveG[x]) + '🟩 letters \n' + str(aveY[x]) + '🟨 letters \n' + str(aveGrey[x]) + '⬛ letters \n\n')
        print('Extra Stats Calculated')
        return outPut

    def GraphData(self):
        self.Analyze.createGraph(self.ColorDistrbution,self.WordleN)
        print("Graph Created and Saved")

    # def CompareToRobot(self):
    #     solving = Solve()
    #     return solving.ComputerGuesses()

    def SaveContent(self,SolverR:str,TwitterR:str):
        try:
            f = open('WordleRecords.txt', 'a')
            f.write('\t' + str(self.currentDate) + '  ' + self.WordleN + '\n' + 
            ('Twitter Results'+ TwitterR) + '\n' + 
            ('Computer Solver Results' + SolverR) + 
            '\n\n')
            f.close
            print("Record Saved")
        except:
            print("Record Failed to Save")
        try:
            SRecord = open('SolverRecord.txt', 'a' )
            SRecord.write(SolverR+' \n')
            SRecord.close
            print("Solver Record Saved")
        except:
            print("Solver Record Failed to Save")
        try:
            TRecord = open('TwitterRecord.txt', 'a')
            TRecord.write(TwitterR+' \n')
            TRecord.close
            print("Solver Record Saved")
        except:
            print("Solver Record Failed to Saved")
    
    def WordleNumber(self):
        return self.WordleN

    def UpdateWordleNumber(self):
        search = self.WordleN
        n = search[7:10]
        number = int(n) + 1
        try:
            Wf = open("WordleNumber.txt", "w")
            Wf.write('Wordle '+str(number))
            Wf.close
            print("Wordle Number Updated")
        except:
            print("Wordle Number Failed to Update")
        return search