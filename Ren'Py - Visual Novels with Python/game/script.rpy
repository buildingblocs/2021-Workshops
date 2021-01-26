# characters
define g = Character(_("Green"), color="#2a5235")

# main
label start:

    scene bg space
    with fade
    "somewhere in space far far away..."

    show green normal
    g "Mr Stark, I'm not feeling too good."

    show green final


menu:

    "Call for an emergency meeting":
        jump meeting
    "Ignore":
        jump ignore
    "send help":
        jump send

label meeting:
    "we have lost :("
    return

label ignore:
    'HEY! you are sus'
    return

label send:
    "he has revived"
    return

return