import unittest
from Game import Game

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_gutter_game(self):
        self.rollMany(20, 0)
        self.assertEquals(0, self.g.return_score())

    def test_all_ones(self):
        self.rollMany(20, 1)
        self.assertEquals(20, self.g.return_score())

    def test_one_spare(self):
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17,0)
        self.assertEquals(16, self.g.return_score())

    def test_one_strike(self):
        self.rollStrike()
        self.g.roll(3)
        self.g.roll(4)
        self.rollMany(16, 0)
        self.assertEquals(24, self.g.return_score())

    def test_perfect_game(self):
        self.rollMany(12, 10)
        self.assertEquals(300, self.g.return_score())
            
    def rollMany(self, pins, roll):
        for _ in range(0, pins):
            self.g.roll(roll)

    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5)

    def rollStrike(self):
        self.g.roll(10)
