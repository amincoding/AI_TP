#!/usr/bin/python

"""
    auther : amin abdedaiem
    date & time of start : april 4th 2021 12:30 PM
    subject : creat {A*} algorithm to solve a game_board
    github repo : https://github.com/amincoding/AI_TP
    date & time of end : april 9th 2021 02:30 AM

""" 
# importing libraries __init__

from PyQt5 import QtWidgets ,QtCore, QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
import os
import time
import copy
import window

# import pygame
sys.setrecursionlimit(2000)

# importing libraries __end__

game_board_goal = []

def get_game(m):
    for i in range(len(m)):
        game_board_goal.append(m[i])

def h(state):
    result = 0
    for i in range(1, 9):
        if state.index(i) != game_board_goal.index(i):
            result += 1
    return result


def generate_moves(state, m, b):
    temp = state[:]
    if m == 'l': 
        temp[b], temp[b - 1] = temp[b - 1], temp[b]
    if m == 'r': 
        temp[b], temp[b + 1] = temp[b + 1], temp[b]
    if m == 'u': 
        temp[b], temp[b - 3] = temp[b - 3], temp[b]
    if m == 'd': 
        temp[b], temp[b + 3] = temp[b + 3], temp[b]
    return temp


def possible_moves(state, visited_states):
    b = state.index(0)
    d = []
    pos_moves = []
    if b <= 5: 
        d.append('d')
    if b >= 3: 
        d.append('u')
    if b % 3 > 0: 
        d.append('l')
    if b % 3 < 2: 
        d.append('r')
    for i in d:
        temp = generate_moves(state, i, b)
        if not temp in visited_states: 
            pos_moves.append(temp)
    return pos_moves


def A_search_algorithm(game_board, game_board_goal, visited_states, g):
    if game_board == game_board_goal: 
        return visited_states
    visited_states.append(game_board)
    aa = possible_moves(game_board, visited_states)
    f = []
    selected_moves = []
    for move in aa: 
        f.append(h(move) + g)
    if len(f) == 0:
        min_score = 0
    else:
        min_score = min(f)
    for i in range(len(aa)):
        if f[i] == min_score: 
            selected_moves.append(aa[i])
    for move in selected_moves:
        if A_search_algorithm(move, game_board_goal, visited_states, g + 1): 
            return visited_states
    return None

def solve(game_board, game_board_goal,dim):
    visited_states = []

    result = A_search_algorithm(game_board, game_board_goal, visited_states, 0)

    if result:
        i = -1
        for state in result:
            # print('move :', i + 1, end="\n")
            # print()
            # display(state,dim)
            i += 1
        r = i + 1
        res = r
    return res
        # display(game_board_goal,dim)


def display(state,dim):
    print()
    for i in range(dim*dim):
        if i % 3 == 0: print()
        if state[i] == -1:
            print(state[i], end="\t")
        else:
            print(state[i], end="\t")
    print(end="\n")

def initualize():

    dim = int(input("donner moi la taille de votre taquin matrix : "))

    print('Donner moi votre taquin {\Etat initial} :')
    
    game_board = [] 
    for i in range(dim):
        temp = input().split(" ")
        for t in temp:
            game_board.append(int(t))
    display(game_board,dim)
    
    print('Donner moi votre taquin matrix {\Etat Final} :')

    game_board_goal = [] 
    for i in range(0,dim):
        temp = input().split(" ")
        for t in temp:
            game_board_goal.append(int(t))
    display(game_board_goal,dim)


    return game_board ,game_board_goal ,dim

def main():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    dim = 3

   
    sys.exit(app.exec_())

if __name__ == '__main__':
    
    main()
    

   


    ##TODO:

    '''
        add a dynamic allocatoin position
    '''
