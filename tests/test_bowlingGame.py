
class TestBowlingGame:
    def rollMany(self,game, n, pins):
        for i in range(n):
            game.roll(pins)
    def rollSpare(self,game):
        game.roll(5)
        game.roll(5)
    def rollStrike(self,game):
        game.roll(10)
    def test_GutterGame(self,game):
        self.rollMany(game,20,0)
        assert(game.score() == 0)
    def test_AllOnes(self,game):
        self.rollMany(game,20,1)
        assert(game.score() == 20)
    def test_OneSpare(self,game):
        self.rollSpare(game)
        game.roll(3)
        self.rollMany(game,17,0)
        assert game.score() == 16
    def test_OneStrike(self,game):
        self.rollStrike(game)
        game.roll(4)
        game.roll(5)
        self.rollMany(game,17,0)
        assert game.score() == 28
    def test_perfektGame(self,game):
        self.rollMany(game,12,10)
        assert game.score() == 300
