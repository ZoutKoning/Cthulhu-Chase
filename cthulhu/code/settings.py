global CURRENT_LEVEL
CURRENT_LEVEL = 0

if(CURRENT_LEVEL == 0 ):
    level_map = [
                '                            ',
                '                            ',
                '                            ',
                ' XX    XXX            XX    ',
                ' XX P          G            ',
                ' XXXX         XX         XX ',
                ' XXXX       XX              ',
                ' XX    X  XXXX    XX  XX    ',
                '       X  XXXX    XX  XXX   ',
                'E   XXXX  XXXXXX  XX  XXXX  ',
                'XXXXXXXX  XXXXXX  XX  XXXX  ']

if(CURRENT_LEVEL == 1):
    level_map = [
                '                                                                                              ',
                '                                                                                              ',
                '                                                                                              ',
                ' XX    XXX   X        XXX                                                                     ',
                ' XX              X           XX                                     XXXXXXXXXX  XXX           ',
                ' XXXX                 X                                            XXX                        ',
                ' XXXX                   X                  X                      XXXX                        ',
                ' X              X  XX  XX  X  X  XX       XX                     XXXXX                     G  ',
                ' X P  X  X  X  XX                      XXXXX     X    X        XXXXXXLLLLLLLLLLLLLLLLLLXXXXXXX',
                'E XXXXXLLXLLXLLXXLLLLLLLLLLLLLLLLLLLLLLLXXXXXLLLLLLLLLLLLLLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
    
if(CURRENT_LEVEL == 2):
    level_map = [
                '                                                                                                     ',
                '                                                                                                     ',
                '            XX                                                            XX              XXXXX  XXX ',
                '                  X                                                      XX              XXXXXX  XXX ',
                ' XX                  X                                                  XXX    X     X  XXXXXXX  XXX ',
                ' XXXX                   X         X                              X    XXXXX       X     XXXXXXX  XXX ',
                ' XXXX         X  X  X  XX        XX                       X           XXXXX  XX         XXXXXXX  XXX ',
                ' X           XX                 XXX         X   X    X  X     X       XXXXXLLLLLLLLLLLLXXXXXX    XXX ',
                ' X P  X  X  XXXLLLLLLLLLLLLLLXXXXXXLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLXXXXXXXXXXLLLLLLLLLLLLXXXX  XXXXXX ',
                'E XXXXXLLXLLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   G XXXL',
                'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']#

if(CURRENT_LEVEL == 3):
    level_map = [
                'XXXX                                                        X                                         ',
                'X                                                           X                                         ',
                'X XXX    X   XX    XXX    X    XLLLLXX           X    X     X               X                         ',
                'X XX                           XXXXXX    X   X             XX          X                              ',
                'X XX                 X         X                       X  XX      X                                   ',
                'X XXP  X  X   XXLLLLLLLLLX     X                   X      XX    XXLLLLLLLLLLLLLLLXLLLXXLLLX           ',
                'X XXXXLLLLLLLLXXXXXXXXXXXX                X    XLLLLXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXX  XXX      X     ',
                'X XXXXXXXXXXXXXXXXXXXXXXXX            XLLLLLLLLXXXXXXX         XX                                     ',
                'X                       XXXLLLLXLLLLXLXXXXXXXXX         XXXXXXXX                      X               ',
                'X                                                     XXXXXX G   XLLLXLLLLLXLLLLXXLLLLLLLLXLLLLLLLLLLL',
                'XXXLLLLXLLLLXXLLLLXLLLLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size