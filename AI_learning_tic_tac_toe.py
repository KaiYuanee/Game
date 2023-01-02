# Tic-tac-toe game
# Made by KaiYuanee
# Copyright (C) 2022-2023 KaiYuanee Foundation, Inc.

import time
import os

gameBoard = [[' ', '|', ' ', '|', ' '],
             ['-', '+', '-', '+', '-'],
             [' ', '|', ' ', '|', ' '],
             ['-', '+', '-', '+', '-'],
             [' ', '|', ' ', '|', ' ']]
piece = 0
endSystem = 0


def welcome():
    os.system("cls")
    print("歡迎遊玩「井字遊戲」！")
    time.sleep(1)


def main():
    global endSystem
    gameMode = input("請選擇遊玩模式(輸入1為單人、2為雙人、0為離開遊戲)：")
    if gameMode == '0':
        print("謝謝您的遊玩！")
        time.sleep(1)
        os.system("cls")
        endSystem += 1
    elif gameMode == '1':
        singlePlayer()
    elif gameMode == '2':
        multiPlayer()
    else:
        print("錯誤：請輸入有效字元！")


def singlePlayer():
    pass  # 尚未製作單人模式


def multiPlayer():
    resetGameBoard()
    global gameBoard, piece
    os.system("cls")
    printGameBoard()
    winner = ''
    while piece < 9:
        if piece % 2 == 0:
            turn = 'O'
        else:
            turn = 'X'
        move = input("請輸入您要下棋的位置：")
        if (move == '1' and gameBoard[0][0] == ' '):
            gameBoard[0][0] = turn
            piece += 1
        elif (move == '2' and gameBoard[0][2] == ' '):
            gameBoard[0][2] = turn
            piece += 1
        elif (move == '3' and gameBoard[0][4] == ' '):
            gameBoard[0][4] = turn
            piece += 1
        elif (move == '4' and gameBoard[2][0] == ' '):
            gameBoard[2][0] = turn
            piece += 1
        elif (move == '5' and gameBoard[2][2] == ' '):
            gameBoard[2][2] = turn
            piece += 1
        elif (move == '6' and gameBoard[2][4] == ' '):
            gameBoard[2][4] = turn
            piece += 1
        elif (move == '7' and gameBoard[4][0] == ' '):
            gameBoard[4][0] = turn
            piece += 1
        elif (move == '8' and gameBoard[4][2] == ' '):
            gameBoard[4][2] = turn
            piece += 1
        elif (move == '9' and gameBoard[4][4] == ' '):
            gameBoard[4][4] = turn
            piece += 1
        else:
            print("錯誤：您輸入的字元無效或該位置已被佔據！")
            time.sleep(1)
        os.system("cls")
        printGameBoard()
        if gameBoard[0][0] == gameBoard[0][2] == gameBoard[0][4] == 'O':
            winner = 'O'
            break
        elif gameBoard[2][0] == gameBoard[2][2] == gameBoard[2][4] == 'O':
            winner = 'O'
            break
        elif gameBoard[4][0] == gameBoard[4][2] == gameBoard[4][4] == 'O':
            winner = 'O'
            break
        elif gameBoard[0][0] == gameBoard[2][0] == gameBoard[4][0] == 'O':
            winner = 'O'
            break
        elif gameBoard[0][2] == gameBoard[2][2] == gameBoard[4][2] == 'O':
            winner = 'O'
            break
        elif gameBoard[0][4] == gameBoard[2][4] == gameBoard[4][4] == 'O':
            winner = 'O'
            break
        elif gameBoard[0][0] == gameBoard[2][2] == gameBoard[4][4] == 'O':
            winner = 'O'
            break
        elif gameBoard[0][4] == gameBoard[2][2] == gameBoard[4][0] == 'O':
            winner = 'O'
            break
        elif gameBoard[0][0] == gameBoard[0][2] == gameBoard[0][4] == 'X':
            winner = 'X'
            break
        elif gameBoard[2][0] == gameBoard[2][2] == gameBoard[2][4] == 'X':
            winner = 'X'
            break
        elif gameBoard[4][0] == gameBoard[4][2] == gameBoard[4][4] == 'X':
            winner = 'X'
            break
        elif gameBoard[0][0] == gameBoard[2][0] == gameBoard[4][0] == 'X':
            winner = 'X'
            break
        elif gameBoard[0][2] == gameBoard[2][2] == gameBoard[4][2] == 'X':
            winner = 'X'
            break
        elif gameBoard[0][4] == gameBoard[2][4] == gameBoard[4][4] == 'X':
            winner = 'X'
            break
        elif gameBoard[0][0] == gameBoard[2][2] == gameBoard[4][4] == 'X':
            winner = 'X'
            break
        elif gameBoard[0][4] == gameBoard[2][2] == gameBoard[4][0] == 'X':
            winner = 'X'
            break
    if winner == 'O':
        print("恭喜先手獲勝！")
    elif winner == 'X':
        print("恭喜後手獲勝！")
    else:
        print("平手，沒有勝負！")


def printGameBoard():
    global gameBoard
    print()
    for row in gameBoard:
        for column in row:
            print(column, end='')
        print()
    print()


def resetGameBoard():
    global gameBoard, piece
    gameBoard = [[' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' ']]
    piece = 0


welcome()
while True:
    if endSystem == 1:
        break
    main()
