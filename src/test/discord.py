class DiscordBot:
    def __init__(self):
        pass

    def winner(self):
        userinput = input('Type !winner if you just won or type !leaders to see to see leaderboard.\n')
        userinput = userinput.lower()
        if userinput == '!winner':
            print('Congrats on Winning!')
            self.addname()
        elif userinput == '!leaders':
           self.leaderboard()
        else:
            print ('Not a correct command.')
            
    def addname(self):
        pass

    def leaderboard(self):
        pass