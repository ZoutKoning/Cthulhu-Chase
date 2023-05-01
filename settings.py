level_map1 = [
                '                                                                                              ',  
                '                                                                                              ',
                '                                                                                              ',
                '                                                                                              ',
                ' XX    XXX   X                                                        J                       ',
                ' XX S            X                                                  XXX                       ',
                ' XXXX                X                                             XXX                        ',
                ' XXXX                   X                  X                      XXXX                        ',
                ' X    G         X  XX  XX  X  X  XX       XX                     XXXXX                        ',
                ' X P  X  X  X  XX                      XXXXX     X    X    X C XXXXXXLLLLLLLLLLLLLLLLLLXXXXXXX',
                'E XXXXXLLXLLXLLXXLLLLLLLLLLLLLLLLLLLLLLLXXXXXLLLLLLLLLLLLLLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map2 = [
                '                                                                                                      ',
                '                                                                                                      ',
                '                                                                                                      ',
                '            XX                                                            XX              XXXXX   XXX ',
                '                  X                                                      XX              XXXXX    XXX ',
                ' XX    X              X                                                 XXX    X     X  XXXXXX    XXX ',
                ' XXX          S         X         XX                                  XXXXX       X     XXXXXX      X ',
                ' XXX          X  X  X  XX        XX                       X           XXXXX  XX         XXXXXX      X ',
                ' X           XX                 XXX        X   X    X  X     X       XXXXXLLLLLLLLLLLLXXXXXXXXLLX   X ',
                ' X P  X  X  XXXLLLLLLLLLLLLLLXXXXXXLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLXXXXXXXXXXLLLLLLLLLLLLXXXXXXXXX   X ',
                'E XXXXXLLXLLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX G      X',
                'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']#

level_map3 = [
                '                                                                                                      ',
                'E                                                           X                                         ',
                'X        X   XX     XXX                                     X               J                         ',
                'X XXX                     X    XLLLLXX       X   X    X     X               X                         ',
                'X XX                           XXXXXX    X                 XX          X                              ',
                'X XX                XX         X                       X  XX      X                                   ',
                'X XXP  X  X   XXLLLLLLLLXX     X                   X      XX    XXLLLLLLLLLLLLLLLXLLLXXLLLX           ',
                'X XXXXLLLLLLLLXXXXXXXXXXXX                X    XLLLLXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXX  XXX      X     ',
                'X XXXXXXXXXXXXXXXXXXXXXXXX            XLLLLLLLLXXXXXXX         XX                                     ',
                'X                       XXXLLLLXLLLLXLXXXXXXXXX         XXXXXXXX                      X               ',
                'X                          S                          XXXXXX G   XLLLXLLLLLXLLLLXXLLLLLLLLXLLLLLLLLLLL',
                'XXXLLLLXLLLLXXLLLLXLLLLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 64
screen_width = 1200
screen_height = len(level_map1) * tile_size