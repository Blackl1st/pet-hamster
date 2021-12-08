function sleepy_blink_icon() {
    basic.showLeds(`
        . . . . .
                # # . # #
                . . . . .
                . . # # .
                . . # # .
    `)
}

function sleepy_icon() {
    basic.showLeds(`
        # . . . #
                . # . # .
                # . . . #
                . . # # .
                . . # # .
    `)
}

function default_state() {
    basic.showLeds(`
        . . . . .
                . # . # .
                . . . . .
                # . # . #
                . # . # .
    `)
}

function sleepy_blink() {
    sleepy_icon()
    sleepy_blink_icon()
    return
}

input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Sad)
    soundExpression.sad.playUntilDone()
    default_state()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showIcon(IconNames.Happy)
    soundExpression.giggle.playUntilDone()
    default_state()
})
function sleepy_boy() {
    basic.showString("ZzZz")
    sleepy_icon()
    soundExpression.yawn.playUntilDone()
    return
}

basic.showIcon(IconNames.Asleep)
sleepy_boy()
sleepy_blink_icon()
sleepy_icon()
sleepy_blink_icon()
sleepy_icon()
default_state()
