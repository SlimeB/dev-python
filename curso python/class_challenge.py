class player():
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
        self.score = 0

    def set_level(self, int = 0):
        if int > 0:
            self.score += 100
        return self.level + int 
    
    def set_score(self):
        return self.score

Timmy = player("timmy")

print("your level is: {}".format(Timmy.set_level(1)))
print("your score is: {}".format(Timmy.set_score()))