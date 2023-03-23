screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "button.jpg"
        action ShowMenu("StatsUI")

screen StatsUI:
    add Solid("#fff")
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                # add the text to the screen
                text "STRENGTH: " + (str(strength)):
                    size 16
                text "WISDOM: " + (str(wisdom)):
                    size 16
                text "KNOWLEDGE: " + (str(knowledge)):
                    size 16
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "buttonreturn.jpg"
        action Return()