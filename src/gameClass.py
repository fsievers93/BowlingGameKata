class Game:
    def __init__(self):
        self.rolls = []
        self.currentRoll = 0
    def roll(self, pins: int):
        self.rolls.append(pins)
    def score(self):
        score=0
        frameIndex = 0
        for frame in range(10):
            if self.isStrike(frameIndex):
                score += 10 + self.rolls[frameIndex+1] + self.rolls[frameIndex+2]
                frameIndex += 1
            elif self.isSpare(frameIndex):
                score += 10 + self.rolls[frameIndex+2]
                frameIndex += 2
            else:
                score += self.rolls[frameIndex] + self.rolls[frameIndex+1]
                frameIndex += 2
        return score
    def isSpare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10
    def isStrike(self, frameIndex):
        return self.rolls[frameIndex] == 10