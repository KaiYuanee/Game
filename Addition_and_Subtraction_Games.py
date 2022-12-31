# Addition and Subtraction Games
# Made by KaiYuanee
# Copyright(C) 2022-2023 KaiYuanee Foundation, Inc.

basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)

def neverGonnaGiveYouUp():
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))

    basic.pause(200)

    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.HALF))


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
    
    # Show the question
    basic.show_number(A)
    basic.pause(300)
    basic.show_string(signList[sign])
    basic.pause(300)
    basic.show_number(B)
    basic.pause(300)
    basic.show_string('=')

    # User inputs the answer
    Ans = 0
    while not(input.button_is_pressed(Button.AB)):
        if input.button_is_pressed(Button.A):
            Ans -= 1
        elif input.button_is_pressed(Button.B):
            Ans += 1

        # Set the range from 0 to 9
        if Ans == -1:
            Ans = 9
        elif Ans == 10:
            Ans = 0

        basic.show_number(Ans)
    
    # Judge if the answer is correct
    if C == Ans:
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    elif C != Ans:
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.pause(2000)

neverGonnaGiveYouUp()
basic.forever(main)
