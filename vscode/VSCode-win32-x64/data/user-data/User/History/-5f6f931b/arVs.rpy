# The script of the game goes in this file.

init python:

    # variables to track player state
    insanity = 0
    hasSmallKey = False
    hasBigKey = False
    wentForestFirst = False
    wentDocksFirst = False
    wentAlleywayFirst = False

    # define flash effect for jumpscares
    flash = Fade(.1, 0, 0, color="#fff")

    # make the music channel not deafening
    _preferences.set_volume('music', 0.4)
    

# define image for use in dust particle effect
image dustparticle = im.Scale("gui/smoke3.png", 10, 10)

# DTW ADDED
image snow = Snow(im.Scale("gui/smoke3.png", 10, 10), max_particles=400, speed=15, wind=0, gravity=10,\
                  xborder=(0, 1920), yborder=(0, 1080), start=400)

# The game starts here.
label start:
    # DTW ADDED
    scene black
    show snow

    # DTW REMOVED
    #scene bg test
    show screen debugUI
    show screen dustFX

    menu sanityCheck:
        "Sanity Check!":
            $ insanity -= 1
        "Insanity Check!":
            $ insanity += 1
        "Start.":
            jump startofstory
        "End.":
            jump endGame
#        "Debug Current Problem Scene.":
#            jump docks

    "Check the debug screen."
    jump sanityCheck

label endGame:
    # This ends the game.
    return

label startofstory:
    #hide screen debugUI
    #show screen dustFX
    play music "audio/scary-spooky-creepy-horror-ambient-dark-piano-cinematic-SoundGalleryByDmitryTaras.mp3"


    scene bg townoutskirts with fade
    "This is home, now: a quiet town on the edge of a dark forest."
    "However, there seems to be no one here."
    "It's so quiet."
    "It's {i}too{/i} quiet."

label wheretogo:
    scene bg townsignpost with fade
    "Where to go?"

    menu townareas:
        "The alleyway":
            jump alleyway
        "The docks":
            jump docks
        "The forest":
            python:
                if insanity <= 3:
                    renpy.jump("forest")
                else:
                    renpy.jump("forestCreepy")

# ---------------------------- alleyway ----------------------------
label alleyway:
    scene bg closedalleydoor with fade
    with fade

    python:
        if wentDocksFirst == False and wentForestFirst == False:
            wentAlleywayFirst = True

    "Nestled between the stone walls, blocking the way off, is a closed door."
    
    menu mysteryDoor:
        "Investigate.":
            "The door has runic carvings etched into its frame. Something unsightly seeps from underneath it."
            jump mysteryDoor
        
        "Open it.":
            python:
                if hasBigKey == False:
                    renpy.say(narrator, "It's locked.")
                    renpy.jump("mysteryDoor")
                else:
                    renpy.jump("behindAlleyDoor")
            
        "Leave.":
            jump itemInAlley

label behindAlleyDoor:
    scene bg behindalleydoor with fade
    "You use the big key and swing the door open."
    "The puddle on the floor sticks to your shoes as you walk through it."
    "It reeks."
    menu:
        "Keep going.":
            $ insanity += 1
            jump behindAlleyDoorContinue
        "Turn back.":
            jump wheretogo

label behindAlleyDoorContinue:
    "The path is stained."
    "It leads to a dead end."
    "There's something sprawled in the corner."

    menu lookDeadThing:
        "Look.":
            jump deadThing
        "Leave.":
            jump itemInAlley

label deadThing:
    scene bg deadthing with fade #make art for this
    $ insanity += 3
    "It's dead."
    python:
        if insanity >= 5:
            renpy.jump("deadThingInsanity")
        else:
            renpy.jump("lookDeadThing")

label deadThingInsanity:
    scene bg deadthing with vpunch
    "It moves."
    with vpunch
    with vpunch
    "It moves. {color=#ff0000}It moves.{/color}"
    "...It's still."

label itemInAlley:
    scene bg keyonstreet with fade
    with fade
    "The alley darkens and the wind picks up."
    "Something small lays on the ground."
    python:
        if hasSmallKey == False:
            renpy.jump("smallKey")
        else:
            renpy.jump("emptyStreet")

    menu smallKey:
        "Pick it up.":
            "It's a key."
            $ hasSmallKey = True
            jump keyMenu

        "Leave it.":
            $ insanity += 1
            "It glints a little brighter in the moonlight."
            jump smallKey
    
    menu keyMenu:
        "Return to the door.":
            scene bg closedalleydoor
            with fade
            "The key doesn't fit."
            "There's nothing more to do here."
            jump backOnStreet

        "Exit the alleyway.":
            jump backOnStreet

label backOnStreet:
    scene bg backonstreet with fade
    with fade
    "Something flickers in one of the streetlights."

    menu streetlight:
        "Look closer.":
            $ insanity += 1
            "It's gone. What was it?"
        "Look away.":
            $ insanity -= 1
            "Surely it's nothing important."

    "The key... it goes somewhere."

    scene bg wallnormal
    with fade
    menu useKey:
        "Try the hole in the wall.":
            python:
                if insanity >= 1:
                    renpy.jump("holeMoves")
                else:
                    renpy.jump("holeStationary")

label holeMoves:
    play sound "audio/monster-roar-NicknameLarry.mp3"
    scene bg walleye
    with flash
    with vpunch
    with hpunch
    "The stone twists and looks back at the intrusion."

    scene bg wallnormal
    "... It's back to normal."

    menu keyLeave:
        "Leave.":
            jump largeMoon

label holeStationary:
    scene bg wallnormal
    "Nothing happens."
    jump largeMoon

label largeMoon:
    scene bg largemoon with fade
    with fade
    "The air dampens. Was the moon always that large?"
    menu:
        "...":
            "Time to go back."
            jump wheretogo

label emptyStreet:
    scene bg emptyStreet
    with fade
    "...It's suddenly gone."
    $ insanity += 1

    jump wheretogo
# ---------------------------- /alleyway ----------------------------


# ---------------------------- docks ----------------------------
label docks:

    python:
        if wentAlleywayFirst == False and wentForestFirst == False:
            wentDocksFirst = True

    scene bg docks with fade #make art for this
    "The water is dark and the area smells musty."
    "One of the boats looks like it's been used recently."

    menu usedBoat:
        "Investigate.":
            "It's wet on the bottom."
            jump usedBoat
        "Leave.":
            jump backToDocks

label backToDocks:
    python:
        if insanity >= 2:
            renpy.jump("docksMoved")
        else:
            "There's nothing more to do here."
            renpy.jump("docksLeave")

label docksMoved:
    "Something moves in the shadows."
    menu docksMovedMenu:
        "Investigate.":
            "There's nothing there now."
            $ insanity += 1
            jump docksMovedMenu
        "Ignore it.":
            "Maybe it was a trick of the mind."
            jump docksLeave

label docksLeave:
    menu docksLeaveMenu:
        "...":
            "Time to go back."
            jump docksExit

label docksExit:

    python:
        if hasBigKey == False:
            renpy.jump("collectBigKey")
        else:
            renpy.jump("wheretogo")

label collectBigKey:
    "Something glints on one of the nearby posts as you pass by."
    menu docksKeyMenu:
        "Pick it up.":
            $ hasBigKey = True
            "It's a large key."
            "Maybe it goes somewhere."
            jump wheretogo
        "Leave it.":
            "It glints insistently in the moonlight."
            jump docksKeyMenu


# ---------------------------- /docks ----------------------------

# ---------------------------- forest ----------------------------
label forest:
    
    python:
        if wentDocksFirst == False and wentAlleywayFirst == False:
            wentForestFirst = True

    jump forestNormal

label forestNormal:
    scene bg forestoutskirts with fade #make art for this
    "The forest is dark and uninviting."
    "There's no sound, not even from evening birds."
    menu forestOutskirtsMenu:
        "Enter the forest.":
            jump forestInner
        "Turn back.":
            jump wheretogo

label forestInner:
    scene bg forestinner with fade #make art for this
    "Starlight barely filters through the trees."
    "If you look up, you can still see the moon."
    menu forestInnerMenu:
        "Look up.":
            jump lookAtTheMoon
        "Keep going.":
            jump forestDepths

label lookAtTheMoon:
    "It looms."
    $ insanity += 1

label forestDepths:
    scene bg templeoutside with fade #make art for this
    "An ancient temple peeks out from the grove."
    "There are footprints in the dirt leading to the entrance."
    menu:
        "Investigate.":
            jump temple
        "Leave.":
            jump wheretogo

# ---------------------------- /forest ----------------------------

# ---------------------------- creepy forest ----------------------------
label forestCreepy:
    scene bg forestcreepy with fade #make art for this
    "The forest is dark and uninviting."
    "There's no sound, not even from evening birds."
    "The shadows sink into each other."
    menu:
        "Look at them.":
            $ insanity += 2
            "They meld into a carpet over the forest floor."
        "Keep looking forward.":
            $ insanity += 1
            "Best not to think about it."

    jump forestOutskirtsMenu
# ---------------------------- /creepy forest ----------------------------


# ---------------------------- temple ----------------------------
label temple:
    scene bg templelobby with fade #make art for this
    "You enter the temple."
    python:
        if insanity >= 3:
            renpy.jump("templeCreepy")
        else:
            renpy.jump("templeNormal")

label templeCreepy:
    scene bg templecreepy with fade #make art for this
    "It creaks in its walls."
    "Something pricks at the back of your mind."
    "You're being watched."
    menu:
        "Turn around.":
            "There's nothing there."
            $ insanity += 3
        "Keep course.":
            "Don't think about it."
            $ insanity += 1

    "Keep going..."
    "The temple winds on for ages."
    "Eventually, you find a door."
    scene bg templedoor with fade #make art for this
    python:
        if hasSmallKey == True:
            renpy.jump("trySmallKey")
        else:
            renpy.say(narrator, "It's locked. Maybe there's a key somewhere in town.")
            renpy.jump("templeNoKey")

label trySmallKey:
    menu trySmallKeyMenu:
        "Try the small key.":
            "It fits perfectly in the door."
            jump behindTempleDoor

label templeNoKey:
    menu templeNoKeyMenu:
        "Force the door.":
            $ insanity += 1
            jump forceTempleDoor
        "Return to town.":
            jump wheretogo

label forceTempleDoor:
    python:
        if insanity >= 7:
            renpy.jump("forceDoorInsane")
        else:
            renpy.say(narrator, "The door creaks but does not give.")
            renpy.jump("templeNoKeyMenu")

label forceDoorInsane:
    scene bg forcedoorinsane #make art for this
    "The door melts into goo and the walls sway."
    "You grow dizzy."
    jump alleyway
    

label templeNormal:
    scene bg templenormal with fade #make art for this
    "It's old and smells of moss."
    "There's water on the floor."
    menu:
        "Keep going.":
            jump templeNormalContinue
        "Turn back.":
            jump wheretogo
            

label templeNormalContinue:
    "The temple winds on for ages."
    "Eventually, you find a door."
    scene bg templedoor with fade
    python:
        if hasSmallKey == True:
            renpy.jump("trySmallKey")
        else:
            renpy.say(narrator, "It's locked. Maybe there's a key somewhere in town.")
            renpy.jump("templeNoKey")

label behindTempleDoor:
    scene bg behindtempledoor with fade #make art for this
    "The shadows deepen."
    "In the corner of the room is a pedestal."
    "It's lit by candles."
    menu:
        "Investigate.":
            jump templePedestal
        "Leave the temple.":
            jump endingLeftTemple

label templePedestal:
    scene bg templepedestal with fade #make art for this
    "...This isn't right."
    "The candles flicker."
    menu:
        "Run.":
            jump endingLeftTemple
        "RUN.":
            jump fledPanicked

# ---------------------------- /temple ----------------------------

# ---------------------- ending left temple --------------------

label endingLeftTemple:
    scene bg lefttemple with fade #make art for this
    "Turn. Leave. Get out of there. Something isn't right."
    "It whispers to you."

    scene bg leavingtown with fade #make art for this
    "The whole town is rotten."
    "With what is impossible to say."
    "Leave."
    "Leave, and never return."
    jump endGame

# ---------------------- /ending left temple --------------------

label fledPanicked:
    "{color=#f00}The shadows deepen.{/color}"
    "Leave."
    "Get out."
    "{color=#f00}GET OUT.{/color}"
    
    python:
        if insanity >= 10:
            renpy.jump("trappedInTemple")
        elif insanity < 10 and insanity >= 5:
            renpy.jump("leftInsane")
        else:
            renpy.jump("leftSane")

label trappedInTemple:
    scene bg trappedintemple with fade #make art for this
    "The temple winds on forever."
    "It never ends."
    "The shadows follow."
    "They swallow the path."
    "The entrance is sealed."
    "The walls are watching."
    "The ceiling is watching."
    "The temple is watching. {color=#f00}The temple is watching.{/color}"
    "{color=#f00}It never stops watching.{/color}"
    jump endGame

label leftInsane:
    scene bg leftinsane with fade #make art for this
    "The temple winds on."
    "The shadows follow."
    "They eat the path."
    "Finally, the entrance appears from the air."
    "Leave."
    "Leave this town, and never return."
    "Else, it will swallow you."
    jump endGame

label leftSane:
    scene bg leftsane with fade #make art for this
    "The temple winds on."
    "The entrance appears only after hours."
    "Leave."
    "Leave this town, and never return."
    jump endGame

