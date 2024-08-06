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
        #352 512+32
        Dialog(352, 512+32, [["Israel_Angry", "You stole my land!"],
                        ["Palestine_Angry", "You stole my land!"],
                        ["Manikom_Confused", "Why are you fighting?"],
                        ["Romania_Bored", "Eh, they've been doing that for who knows how long"],
                        ["Manikom_Bored", "Isn't it worth it to work together for once?"],
                        ["Manikom_Confused", "I mean, you probably want to get out of here."],
                        ["Israel_Angry", "I guess so..."]], "images/dialogs/israel_angry.png", True),
]

eol_x = 32
eol_y = 512
player_x = 832
player_y = 544