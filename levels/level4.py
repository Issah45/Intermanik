platforms = [
        pygame.Rect(256, 416, 32, 32),
        pygame.Rect(384, 416, 32, 32),
        pygame.Rect(480, 416, 32, 32),
        pygame.Rect(576, 416, 32, 32),
        pygame.Rect(672, 416, 32, 32),
        pygame.Rect(768, 416, 32, 32),
        pygame.Rect(0, 384, 192, 224),
        pygame.Rect(864, 384, 128, 224),
        pygame.Rect(832, 384, 32, 224),
]

spikes = [
]


dialogs = [
        Dialog(288-(32*4), 544-(32*6), [["ogre", "Hold x to dash"],
                        ["ogre", "You can only place 3 blocks per level."]]),
]

eol_x = 960-32
eol_y = 320
lavaballs = [
        LavaBall(256, 352, 0.06),
        # LavaBall(384, 352),
        LavaBall(480, 352, 0.06),
        # LavaBall(576, 352),
        LavaBall(672, 352, 0.06),
        LavaBall(768, 352, 0.06),
]
player_x = 32
player_y = 352