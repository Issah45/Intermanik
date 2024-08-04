platforms = [
        pygame.Rect(0, 0, 32, 608),
        pygame.Rect(0, 576, 960, 32),
        pygame.Rect(928, 0, 32, 608),
        pygame.Rect(0, 0, 928, 32),
        pygame.Rect(416, 512, 320, 64),
]

spikes = [
        Spike(620, 488, False),
        Spike(492, 488, False),
]


dialogs = [
        Dialog(352, 512+32, [["ogre", "1: Beginnings"],
                          ["romania_confused", "Who are you?"],
                          ["manikom_bored", "Manikom."],
                          ["romania_bored", "Huh, so you ended up here as well."]]),
]

eol_x = 32
eol_y = 512
player_x = 832
player_y = 544