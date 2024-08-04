platforms = [
        pygame.Rect(0, 0, 960, 32),
        pygame.Rect(0, 0, 32, 608),
        pygame.Rect(0, 576, 960, 32),
        pygame.Rect(928, 0, 32, 576),
        pygame.Rect(96, 512, 64, 32),
        pygame.Rect(192, 480, 64, 32),
        pygame.Rect(256, 416, 64, 32),
        pygame.Rect(384, 448, 64, 32),
        pygame.Rect(512, 416, 64, 32),
        pygame.Rect(608, 384, 64, 32),
        pygame.Rect(704, 352, 64, 32),
        pygame.Rect(800, 320, 64, 0),
        pygame.Rect(672, 288, 64, 32),
        pygame.Rect(576, 256, 64, 32),
        pygame.Rect(448, 224, 64, 32),
        pygame.Rect(320, 192, 64, 32),
        pygame.Rect(192, 160, 96, 32),
        pygame.Rect(32, 128, 160, 32),
        pygame.Rect(160, 128, 32, 64),
]

spikes = [
        Spike(236, 456, False),
        Spike(300, 392, False),
        Spike(588, 232, False),
        Spike(460, 200, False),
        Spike(332, 168, False),
        Spike(140, 104, False),
]


dialogs = [

        Dialog(704-64, 320+32, [["ogre", "2: A Message"],
                          ["romania", "I found something!"],
                          ["manikom_confused", "what is it?"],
                          ["romania_bored", "Its a letter sent by 'Rigorous'"],
                          ["manikom_small", "Well, that's not helpful (whoever Rigorous is)"]]),
]

eol_x = 32
eol_y = 64
player_x = 32
player_y = 544