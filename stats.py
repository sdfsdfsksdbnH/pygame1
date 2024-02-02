class Stats():
    def __init__(self):
        self.resets()
        self.rungame = True
        with open('highscore.txt', 'r') as f:
            self.record = int(f.readline())

    def resets(self):
        self.gun_left = 2
        self.score = 0