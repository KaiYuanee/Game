# Addition and Subtraction Games
# Made by KaiYuanee
# Copyright(C) 2022-2023 KaiYuanee Foundation, Inc.

signList = ['+', '-']
def main():
    sign = randint(0, 1)
    if sign == 0:
        A = randint(0, 9)
        B = randint(0, 9)
        while A + B >= 10:
            A = randint(0, 9)
            B = randint(0, 9)
        C = A + B
    else:
        A = randint(0, 9)
        B = randint(0, A)
        C = A - B
    # Augend and minuend are A
    # Addend and subtrahend are B
    # The result is C
    
    basic.show_number(A)
    basic.pause(1000)
    basic.show_string(signList[sign])
    basic.pause(1000)
    basic.show_number(B)
    basic.pause(1000)
    basic.show_string('=')

basic.forever(main)
