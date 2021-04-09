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
import math
import copy
# importing libraries __end__

def possible_moves(game_board, search_zero):
    x = search_zero
    if x == (1,1):
        moves = 4
        for i in range(moves):
            new_board = copy.deepcopy(game_board)


        new_board = copy.deepcopy(game_board)
        new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
        yield State(new_board, moves, self)
    if i in [1, 2, 4, 5, 7, 8]:
        new_board = self.values[:]
        new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
        yield State(new_board, moves, self)
    if i in [0, 1, 3, 4, 6, 7]:
        new_board = self.values[:]
        new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
        yield State(new_board, moves, self)
    if i in [0, 1, 2, 3, 4, 5]:
        new_board = self.values[:]
        new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
        yield State(new_board, moves, self)


def h(game_board,game_board_goal,dim):
    itere = 0
    for i in range(dim - 1):
        for j in range(dim - 1):
            if game_board[i][j] - game_board_goal[i][j] == 0:
                itere += 1
    if itere == 9:
        return 0
    else:
        return dim*dim -itere

def g():
    pass


def moves(zero_position):
    some_list = [(0,0),(0,2),(2,0),(2,2)]

    if zero_position == (1,1):
        possible_moves = 4
        list_of_coardonates = [(0,1),(1,0),(2,1),(1,2)]
    elif zero_position in some_list:
        possible_moves = 2
        # possible_directions

def search_zero(game_board,dim):
    exist = False
    i = -1
    j = -1
    for rows in game_board:
        i += 1
        j = 0
        for colomns in rows:
            if colomns == 0:
                j += 1
                exist = True
                return (i,j)
    if not exist :
        return "broken board"

def f():

    return lenghtOf_f
def inputt():
    dim = int(input("input the dimension on your board : "))
    n = dim

    game_board = [[0 for j in range(n)] for i in range(n)]
    game_board_goal = [[0 for j in range(n)] for i in range(n)]

    print("Input vals for your board : ")
    for i in range(n):
        for j in range(n):
            k = int(input())
            game_board[i][j] = k

    # User input of goal state       
    print("Input vals for your goal_board : ")
    for i in range(n):
        for j in range(n):
            k = int(input())
            game_board_goal[i][j] = k
    return n , game_board , game_board_goal

def main():
    dim , game_board , game_board_goal = inputt()
    print(search_zero(game_board,dim))
    print(h(game_board,game_board_goal,dim))

    # print(game_board[2][1])

if __name__ == '__main__':
    main()



    #TODO:
    
    '''
        add a dynamic allocatoin position
      
        link : https://www.youtube.com/watch?v=afC3dq9MeJg
        time : 2:17

    '''

