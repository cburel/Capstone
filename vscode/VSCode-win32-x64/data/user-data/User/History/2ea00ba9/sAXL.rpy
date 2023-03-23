screen debugUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "debugidle.png"
        action ShowMenu("DebugUI")

screen DebugUI:
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
                text "INSANITY: " + (str(insanity)):
                    size 16
                text "pickedUpSmallKey: " + (str(pickedUpSmallKey)):
                    size 16
                
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "debugexit.png"
        action Return()