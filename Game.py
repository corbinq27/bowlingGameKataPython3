class Game:

    def __init__(self):
        self.score = 0
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        self.score += pins
        self.rolls.append(pins)
        self.current_roll += 1

    def return_score(self):
        score = 0
        frameIndex = 0
        for frame in range(0, 10):
            if self.rolls[frameIndex] == 10: #strike
                score += 10 + self.strikeBonus(frameIndex)
                frameIndex += 1
            elif self.is_spare(frameIndex): #spare
                score += 10 + self.spareBonus(frameIndex)
                frameIndex += 2
            else:
                score += self.sumOfBallsRolled(frameIndex)
                frameIndex += 2
        return score

    def sumOfBallsRolled(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1]

    def spareBonus(self, frameIndex):
        return self.rolls[frameIndex + 2]

    def strikeBonus(self,frameIndex):
        return self.rolls[frameIndex + 1] + self.spareBonus(frameIndex)

    def is_spare(self, frameIndex):
        return self.sumOfBallsRolled(frameIndex) == 10
