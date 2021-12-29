class Statistic():

    def __init__(self):
        self.statistic()
        with open('HS.txt', 'r') as f:
            self.HScore = int(f.readline())
    def statistic(self):
        self.gun_live = 2
        self.score = 0
        self.res = False
        self.GoRes = False
        self.StopB = False