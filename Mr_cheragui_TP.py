#!/usr/bin/python

"""
    auther : amin abdedaiem
    date & time : april 4th 2021 11:30 AM
    subject : creat {A*} algorithm to solve a game_board
    github repo : https://github.com/amincoding/AI_TP

""" 
# importing libraries __init__

import sys
import os
import random
import itertools
import collections
import time
import pygame 
# importing libraries __end__

class Casa:
    
    def __init__(self, O7jia, parent=None, action=None):
        self.O7jia = O7jia
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def kimat_F(self):
        return (self.g + self.h)

    @property
    def state(self):
        return str(self)

    @property 
    def trig(self):

        casa, p = self, []
        while casa:
            p.append(casa)
            casa = casa.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.O7jia.solved

    @property
    def actions(self):
        return self.O7jia.actions

    @property
    def h(self):
        return self.O7jia.manhattan

    @property
    def f(self):
        return self.h + self.g

    def __str__(self):
        return str(self.O7jia)

# --------------------------------------------------------------------------------------------
class AL_7al:
    def __init__(self, start):
        self.start = start

    def solve(self):

        queue = collections.deque([Casa(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda casa: casa.f))
            casa = queue.popleft()
            if casa.solved:
                return casa.trig

            for move, action in casa.actions:
                child = Casa(move(), casa, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)

# --------------------------------------------------------------------------------------------        


class O7jia:
    def __init__(self, game_board):
        self.width = len(game_board[0])
        self.game_board = game_board

    @property
    def solved(self):

        N = self.width * self.width
        return str(self) == ''.join(map(str, range(1,N))) + '0'

    @property 
    def actions(self):

        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            directions = {'R':(i, j-1),
                          'L':(i, j+1),
                          'D':(i-1, j),
                          'U':(i+1, j)}

            for action, (r, c) in directions.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.game_board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    @property
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] != 0:
                    x, y = divmod(self.game_board[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def shuffle(self):
 
        O7jia = self
        for _ in range(1000):
            O7jia = random.choice(O7jia.actions)[0]()
        return O7jia

    def copy(self):

        game_board = []
        for row in self.game_board:
            game_board.append([x for x in row])
        return O7jia(game_board)

    def _move(self, at, to):

        copy = self.copy()
        i, j = at
        r, c = to
        copy.game_board[i][j], copy.game_board[r][c] = copy.game_board[r][c], copy.game_board[i][j]
        return copy

    def pprint(self):
        for row in self.game_board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.game_board:
            yield from row

class Lo3ba_puzzle:
    def __init__(self,gs,ts,ms):
        self.gs, self.ts,self.ms = gs , ts , ms

        self.tiles_len = gs[0]*gs[1]-1

        self.tiles = [(x,y) for y in range(gs[1]) for x in range(gs[0])]

        self.tilepos = {(x,y): (x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1])  for x in range(gs[0])}



    def update(self,dt):
        pass

    def draw(self,screen):
        for i in range(self.tiles_len):
            x,y = self.tilepos[self.tiles[i]]
            pygame.draw.rect(screen , (0,255,0) , (x,y,self.ts,self.ts))



def Lo3ba_visual():

    pygame.init()
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    pygame.display.set_caption("Mr Cheragui O7jia")
    # screen size (320,320) ta9dar tbadlo 3ady
    screen = pygame.display.set_mode((320,320))
    # add the flag RESIZABLE to set_mode to make the game RESIZABLE
    fpsclock = pygame.time.Clock()
    program = Lo3ba_puzzle((3,3) , 100 , 5)

    while True:
        dt = fpsclock.tick()/1000

        # rgb (0,0,0) = black
        screen.fill((0,0,0))
        program.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            # sys.exit()

        program.update(dt)

def get_input():

    Tdim = int(input("Donner moi la dimension de set matrix : "))
    dim = Tdim - 1

    game_board_from_input = [dim][dim]

    for i in range(dim):
        for j in range(1 , dim):
            temp = int(input())
            game_board_from_input[i][j] = temp

    return game_board_from_input

    # the get imput function is not working

# --------------------------------------------------------------------------------------------

# the main menu for this program
if __name__ == '__main__':

    # example of use without input    
    #game_board = [[1,5,8],
    #              [2,0,3],
    #              [7,4,6]]

    # example of use with input
    game_board = get_input()

    o7jia = O7jia(game_board)
    #O7jia = O7jia.shuffle()
    s = AL_7al(o7jia)
    Stop_watch_before_start = time.process_time()
    p = s.solve()
    Stop_watch_after_start = time.process_time()

    path = []
    steps = 0
    for casa in p:
        path.append(casa.action)
        casa.O7jia.pprint()
        steps += 1

    print("Total number of steps: " + str(steps))
    print("Total amount of time in search: " + str(Stop_watch_after_start - Stop_watch_before_start) + " second(s)")
    print(f"the path to win the game is : {path}")

    Lo3ba_visual()
    
                
    # TODO:
    
    '''

        link : https://www.youtube.com/watch?v=afC3dq9MeJg
        time : 2:17

    '''