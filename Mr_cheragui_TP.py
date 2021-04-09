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
import time
import copy
import pygame
# importing libraries __end__
from queue import Queue

src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, 8, -1, 6, 7]


def h(state):
    res = 0
    for i in range(1, 9):
        if state.index(i) != target.index(i): res += 1
    return res


def gen(state, m, b):
    temp = state[:]
    if m == 'l': temp[b], temp[b - 1] = temp[b - 1], temp[b]
    if m == 'r': temp[b], temp[b + 1] = temp[b + 1], temp[b]
    if m == 'u': temp[b], temp[b - 3] = temp[b - 3], temp[b]
    if m == 'd': temp[b], temp[b + 3] = temp[b + 3], temp[b]
    return temp


def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    pos_moves = []
    if b <= 5: d.append('d')
    if b >= 3: d.append('u')
    if b % 3 > 0: d.append('l')
    if b % 3 < 2: d.append('r')
    for i in d:
        temp = gen(state, i, b)
        if not temp in visited_states: pos_moves.append(temp)
    return pos_moves


def search(src, target, visited_states, g):
    if src == target: return visited_states
    visited_states.append(src),
    adj = possible_moves(src, visited_states)
    scores = []
    selected_moves = []
    for move in adj: scores.append(h(move) + g)
    if len(scores) == 0:
        min_score = 0
    else:
        min_score = min(scores)
    for i in range(len(adj)):
        if scores[i] == min_score: selected_moves.append(adj[i])
    for move in selected_moves:
        if search(move, target, visited_states, g + 1): return visited_states
    return None

def solve(src, target, bfs=True):
    visited_states = []

    res = search(src, target, visited_states, 0)

    if res:
        i = 0
        for state in res:
            print('move :', i + 1, end="\n")
            print()
            display(state)
            i += 1
        print('move :', i + 1)
        display(target)


def display(state):
    print()
    for i in range(9):
        if i % 3 == 0: print()
        if state[i] == -1:
            print(state[i], end="\t")
        else:
            print(state[i], end="\t")
    print(end="\n")


def main():
    print('Initial State :')
    display(src)
    print('Goal State :')
    display(target)
    print('*' * 10)
    solve(src, target)

if __name__ == '__main__':
    main()
    #TODO:
    
    '''
        add a dynamic allocatoin position
      
        link : https://www.youtube.com/watch?v=afC3dq9MeJg
        time : 2:17

    '''
