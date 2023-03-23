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
                text "Sanity: " + (str(sanity)):
                    size 16
                
    imagebutton:
        xalign 1.0
        yalign 1.0
        xoffset -30
        yoffset 30
        auto "debugexit.png"
        action Return()