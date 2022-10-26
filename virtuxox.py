import cl_games

class MainGame(cl_games.Game):

    def __init__(self):

        super(MainGame, self).__init__()

        self.title = "My New Game"

    def update(self):

        #This is run every frame
        
        game = MainGame()
        game.run()

class Player(cl_games.sprites.Sprite):

    def __init__(self, game):

        super(Player, self).__init__(game)

        self.image = [

            "  ^  ",

            " / \ ",

            "/___\\"

        ]

        self.posX, self.posY = 18, 17

        self.setLengthToImage()

    def update(self):
        game = MainGame()

    #Also run every frame
        game.addSprite(Player(game))