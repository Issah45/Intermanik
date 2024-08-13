platforms = [
        pygame.Rect(0, 576, 960, 32),
        pygame.Rect(0, 0, 992, 32),
        pygame.Rect(64, 32, 928, 32),
        pygame.Rect(192, 64, 768, 32),
        pygame.Rect(384, 96, 608, 32),
        pygame.Rect(960, 64, 32, 96),
        pygame.Rect(640, 128, 320, 32),
        pygame.Rect(768, 160, 224, 64),
        pygame.Rect(832, 224, 160, 64),
        pygame.Rect(960, 288, 32, 192),
        pygame.Rect(960, 576, 32, 32),
]

spikes = [
]


dialogs = [
        Dialog(512, 544, [["romania_bored", "So i guess this is the blue cave in question,"],
                          ["romania_confused", "who could possibly be in there?"]], "images/dialogs/romania_confused.png", True),
]

eol_x = 960-32
eol_y = 512
lavaballs = [
]
player_x = 32
player_y = 544