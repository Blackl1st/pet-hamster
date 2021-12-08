def chew_icon():
    basic.show_leds("""
        . # . # .
                . . . . .
                . . # # #
                . . # . #
                . . # # #
    """)
    music.play_tone(147, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                . . # # .
                . . # # .
    """)
def sleepy_blink_icon():
    basic.show_leds("""
        . . . . .
                # # . # #
                . . . . .
                . . # # .
                . . # # .
    """)
def sleepy_icon():
    basic.show_leds("""
        # . . . #
                . # . # .
                # . . . #
                . . # # .
                . . # # .
    """)

def on_button_pressed_a():
    chew_icon()
    chew_icon()
    chew_icon()
    basic.show_icon(IconNames.HAPPY)
    soundExpression.giggle.play_until_done()
    default_state()
input.on_button_pressed(Button.A, on_button_pressed_a)

def default_state():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . # . #
                . # . # .
    """)
def sleepy_blink():
    sleepy_icon()
    sleepy_blink_icon()
    return

def on_button_pressed_b():
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
    soundExpression.sad.play_until_done()
    basic.show_icon(IconNames.SAD)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    soundExpression.giggle.play_until_done()
    default_state()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def sleepy_boy():
    basic.show_string("ZzZz")
    sleepy_icon()
    soundExpression.yawn.play_until_done()
    return
basic.show_icon(IconNames.ASLEEP)
sleepy_boy()
sleepy_blink_icon()
sleepy_icon()
sleepy_blink_icon()
sleepy_icon()
default_state()

def on_every_interval():
    default_state()
    basic.show_icon(IconNames.SAD)
    soundExpression.sad.play_until_done()
    basic.show_string("Feed Me!")
    basic.show_icon(IconNames.SAD)
loops.every_interval(60000, on_every_interval)
