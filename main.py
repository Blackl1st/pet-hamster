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

def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
    soundExpression.sad.play_until_done()
    default_state()
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