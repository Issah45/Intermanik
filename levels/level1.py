platforms = [
        pygame.Rect(0, 0, 960, 32,),
        pygame.Rect(928, 0, 32, 608,),
        pygame.Rect(0, 576, 928, 32,),
        pygame.Rect(0, 0, 32, 576),
        pygame.Rect(160, 160, 768, 32),
        pygame.Rect(32, 320, 672, 32),
        pygame.Rect(192, 256, 32, 64),
        pygame.Rect(256, 160, 32, 128),
        pygame.Rect(320, 256, 32, 64),
        pygame.Rect(416, 160, 32, 128),
        pygame.Rect(480, 256, 32, 64),
        pygame.Rect(544, 160, 32, 128),
        pygame.Rect(128, 544, 672, 32),
        pygame.Rect(128, 512, 512, 32),
        pygame.Rect(128, 448, 384, 64),
        pygame.Rect(96, 480, 32, 96),
        pygame.Rect(160, 416, 256, 32),
]

spikes = [
        Spike(748, 136, False),
        Spike(588, 136, False),
        Spike(396, 136, False),
        Spike(236, 136, False),
        Spike(44, 296, False),
        Spike(76, 296, False),
        Spike(652, 520, False),
        Spike(524, 488, False),
        Spike(428, 424, False),
        Spike(108, 456, False),
        Spike(748, 520, False),
        Spike(908, 552, False),
]

lavaballs = [
]

dialogs = [
        # 640 288
        Dialog(640, 288, [["romania_confused", "Who are you?"],
                          ["manikom_bored", "Manikom."],
                          ["romania_bored", "Huh, so you ended up here as well."]], "images/dialogs/romania_confused.png"),
]

eol_x = 32
eol_y = 512
player_x = 896
player_y = 128