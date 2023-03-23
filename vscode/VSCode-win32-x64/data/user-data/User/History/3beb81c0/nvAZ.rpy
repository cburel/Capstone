# The script of the game goes in this file.
init python:

    import pygame
    import math
    from enum import Enum

    # variables to track character stats
    strength = 0
    wisdom = 0
    knowledge = 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define warlord = Character("Me")
define commander = Character("The Commander")
define brother = Character("Brother")
define lady = Character("Mother")
define darkness = Character("The Darkness")

# transforms for character portrait alignment
transform midright:
    xalign 0.9
    yalign 0.05
transform midleft:
    xalign 0.1
    yalign 0.05
transform center:
    xalign 0.5
    yalign 0.05

# transforms for character portrait scale
image darkness neutral = im.Scale("darkness neutral.png", 1280, 720)


# The game starts here.
label start:
    # variables to track character branches
    python:
        canBreakRelic = False;
        rememberedPast = False;
        hasTrinket = False;

    # Stasis
    scene bg fieldburning
    with fade
    play music "/audio/cave.ogg"
    show screen gameUI

    "This is home for me: on the battlefield, fighting for our future."
    "For as long as I can remember, I've been in combat like this."
    "I'm hardly the only one so involved with it, but I'm one of the few who have achieved elite status."

    show brother neutral at midright
    with dissolve
    "My brother keeps talking to me privately about the war, about how badly he feels for the enemy."
    "Regardless of any misgivings, however, he's been practicing with his magic, growing more powerful by the day."
    menu:
        "I...."
        "Just hope he stays safe. {color=#f00}(+WIS){/color}":
            $ wisdom += 1
            "STR: [strength] | WIS: [wisdom]"
            jump staysSafe
        "Taught him everything he knows. {color=#f00}(+STR){/color}":
            $ strength += 1
            "STR: [strength] | WIS: [wisdom]"
            jump taughtHim

label staysSafe:
    "The battlefield is just as unforgiving."
    jump mysteries

label taughtHim:
    "I'm sure he's set for greatness. He's already set to surpass me, one day."
    jump mysteries
    
label mysteries:
    
    hide brother neutral
    with dissolve

    "That said, there are greater threats to us than attempts at rebellion from underprepared mortals."
    "There are dangers in this world, mysteries we were never meant to solve."
    "I'm told our enemies this time have the gods at their back."

    # Call to Adventure
    scene bg cave
    with fade
    "They keep a relic, divine in nature, that empowers them."
    "It was given to them eons ago, at the dawn of mortal civilization. It keeps them safe, watches over them."
    "Its destruction will weaken them enough to force their surrender, if not their destruction."
    "This is my appointed task."

    # Refusal of the Call
    "Yet, I'm unconvinced. This relic is a gift from the gods, after all. What could happen to us if we destroy it?"
    "I ponder this, staring out over the battlefield, until I turn at the sound of footsteps behind me."
    
    # Meeting the Mentor/Refusal of the Call
    scene bg fieldburning
    with fade
    show warlord neutral at midleft
    with dissolve

    warlord "Is this task not blasphemous?"

    show queen neutral at midright
    with dissolve

    commander "Perhaps. But it's worth the risk."
    commander "The gods hardly pay attention to the Lower Realms, after all."
    warlord "And if they do this time?"
    commander "They haven't intervened in millennia. I daresay this will be no different."
    warlord "Despite destroying a gift they've given to their chosen people?"
    commander "Indeed. Greater blasphemies haven't caught their attention."
    warlord "..."
    warlord "This..."
    warlord "...with all due respect, this seems like a terrible idea."
    commander "You worry too much. This will work, I assure you."

    hide queen neutral
    with dissolve

    "Her words don't help put my mind at ease."
    "If something goes wrong..."

    hide warlord neutral
    with dissolve

    "I shake my head and return to my tent. Maybe tomorrow, I'll feel better about this."
    
    menu:
        "When I return, I..."
        "Go on to bed. {color=#f00}(+STR){/color}":
            $ strength += 1
            "STR: [strength] | WIS: [wisdom]"
        "Take a while to reflect. {color=#f00}(+WIS){/color}":
            $ wisdom += 1
            "STR: [strength] | WIS: [wisdom]"
        "Read a couple of tomes my brother left for me.":
            $ knowledge += 1
                

    scene bg fieldburning
    with fade
    "I wake in the morning to find a harsher sun than before. It beats down with all the intensity of a raging fire."
    menu:
        "I..."
        "Pray quietly that all goes well. {color=#f00}(+WIS){/color}":
            $ wisdom += 1
            "STR: [strength] | WIS: [wisdom]"
        "Take the time to sharpen my sword. {color=#f00}(+STR){/color}":
            $ strength += 1
            "STR: [strength] | WIS: [wisdom]"
    
    "The clouds seem to wither under the heat."
    "May this go as well as my commander desires."

    # Crossing the Threshold
    scene bg forestouter
    with fade
    play music "/audio/forest.ogg"

    "I make my way to the cave where the relic lies. I can feel its power pulsing through the life around me, winding through the edges of the forest."
    "This is a sacred land."
    menu:
        "I..."
        "Steel myself and tread carefully. {color=#f00}(+WIS){/color}":
            $ wisdom += 1
            "STR: [strength] | WIS: [wisdom]"
        "Draw my blade and head inside. {color=#f00}(+STR){/color}":
            $ strength += 1
            "STR: [strength] | WIS: [wisdom]"
        "Investigate the area first, then cautiously enter. {color=#f00}(+WIS){/color}":
            $ wisdom += 1
            $ knowledge += 1
            "STR: [strength] | WIS: [wisdom]"

    # Tests, Allies, and Enemies
    scene bg forestinnerdark
    with fade
    "The forest itself seems to fight me, to turn me around at every chance it gets."
    "I suppose it makes sense. Nothing dies easily in these lands, let alone anything divine."

    python:
        if knowledge >= 1:
            renpy.jump("forestKnowledge")
        else:
            renpy.jump("forestPath")

label forestKnowledge:
    "There's something on the path, here..."
    menu:
        "Pick it up.":
            "It's some little trinket. I place it in my pocket and continue onwards."
            $ knowledge += 1
            $ hasTrinket = True;
            jump forestPath
        "Leave it alone.":
            "I ignore it and return to my task."
            jump forestPath


label forestPath:
    python:
        if wisdom >= 3:
            renpy.jump("forestWisdom")
        elif strength >= 3:
            canBreakRelic = True;
            renpy.jump("forestStrength")
        else:
            renpy.jump("forestNeutral")

label forestWisdom:
    "However, there is no mistaking the path, lit with the energy of the divine."
    "I can sense it easily. The gods cannot hide their relic from me, even if they tried."
    "I'm not even convinced they're trying at all."
    "Still, I take my steps carefully. There's no sense in recklessness."
    "One false move could spell my end."
    "Despite the clear way forward, something pricks at the back of my mind."
    "It seeds doubt in the shadows of my consciousness."
    menu:
        "I..."
        "Press on.":
            jump forestCave
        "Turn back.":
            jump forestNeutral

label forestStrength:
    "Beasts hinder my path with every step."
    "However, they fall easily beneath my blade. They're nothing before me."
    "Nothing at all can stand before my might."
    "Still, I tread carefully. This is still the land of the gods."
    "I cannot afford to be careless."
    "Something in the back of my mind whispers doubt to me."
    "It seeds it in the shadows of my consciousness."
    jump forestCave

label forestNeutral:
    "I become hopelessly lost in the forest's depths."
    "Days turn into nights, and the sounds of fighting grow ever more distant."
    "I remember the distant past, when such quests were but adventures I read about in storybooks given to me by my mother."
    show lady neutral at midright
    with dissolve
    "She always knew how much I thrived on such tales, stories of valor, heroes and glory."
    "She told me of ancient legends and myths, where the ones who prevailed where the ones who protected the weak."
    "She sought to raise us like those ancient heroes. She wanted us to be worth talking about. Worth remembering. Worth praising."
    "...If nothing else, I can at least find solace remembering her gentle grace."
    python:
        rememberedPast = True;
    "With renewed vigor, I continue my search."
    "Eventually, deep within the heart of the forest and surrounded by ancient, gnarled trees, I arrive at my destination."

label forestCave:
    # Approach to the Inmost Cave
    scene bg cave
    with fade
    play music "/audio/chantingspirits.ogg"
    "I find the relic humming quietly upon its pedestal."
    "It's a quiet, gentle hum, singing as if it's always been here, and always will be."
    "I know this thing has been in this cave since ages long past, and could be forevermore."
    "I know the enemy relies on it, and will surely die if I destroy it."
    
    python:
        if canBreakRelic == True:
            renpy.jump("canBreak")
        else:
            renpy.jump("cannotBreak")

label canBreak:

    "My grip tightens on the hilt of my sword."
    "I know I easily can break it."

    menu:
        "And..."
        "I wonder if I should. {color=#f00}(+WIS){/color}":
            $ wisdom += 1
            "STR: [strength] | WIS: [wisdom]"
            jump falter
        "I don't even hesitate. {color=#f00}(+STR){/color}":
            $ strength += 1
            "STR: [strength] | WIS: [wisdom]"
            jump breakIt

label falter:

    # The Ordeal in the Abyss/Facing the Shadow Self
    "I falter, fearing what lies ahead should I do so."
    "Something gnawing in the back of my mind tells me not to."
    jump empathy

label breakIt:

    "With a steady hand and a decisive blow, I cast the doubt into the depths of my mind and strike the relic."
    jump destroyRelic

label destroyRelic:

    # Apotheosis
    stop music
    play sound "/audio/bottlebreak.wav"
    "It shatters like glass, hum falling silent, glow fading like the last glimmer of a dying firefly."
    "My blood boils in my veins for a fleeting moment, igniting fire within me."
    "Then, the fire dies, and in its place lies a hollow, tingling numbness."
    python:
        isForsaken = True
    "Originating from the relic's pedestal, I feel a wave of energy swallow the land."

    # The Ultimate Boon
    "In the shadow of that wave, I feel the land itself crumble."

    # Refusal of the Return
    "This feels wrong, like I've committed some grave mistake, or like the gods themselves have turned away from me."
    "Or, worse yet, like all their eyes have trained upon me, all at once."
    "I turn back to the mouth of the cave, back towards the light of day."
    "I..."
    menu:
        "Pause where I am.":
            jump stayInCave
        "Exit the cave.":
            jump exitCave

label stayInCave:
    "I hesitate."
    "That creeping doubt lingers in the back of my mind."
    "It slithers into the forefront of my consciousness, wrapping its coils around my thoughts like a snake."

    show darkness neutral
    with dissolve
    darkness "So it ends."
    darkness "So they {color=#f00}die.{/color}"
    darkness "{color=#f00}You have killed them.{/color}"
    darkness "{color=#f00}You have killed everything.{/color}"
    hide darkness neutral
    with dissolve

    jump exitCave

label cannotBreak:

    "But..."
    "I'm not sure I even can."

    python:
        if rememberedPast == True:
            renpy.jump("empathy")
        else:
            renpy.jump("twistRelic")

label empathy:

    "I'm not sure I even {i}should.{/i}"
    "The enemy is the enemy, but they're still alive."
    "They're still... people."
    "At what cost to myself do I destroy everything?"
    "Commit deicide?"
    "Commit {color=#f00}genocide?{/color}"
    "I stare at the relic. It stares back into me."
    menu:
        "I..."
        "Change it.":
            jump twistRelic
        "Leave it.":
            jump leaveIt

label twistRelic:
    "Maybe I can change it."
    "Maybe I can twist it to my advantage, put it to use for our people, instead."
    "My own magic may not be able to extinguish that of a god, but surely I can change it."
    "I place my hand on the relic. It pulses under my palm."
    "I take a deep breath and attune my magic to that of its own."
    "In a split second, everything goes wrong."
    jump destroyRelic
    
label leaveIt:
    "I watch the relic for what seems like an eternity."
    "It's mesmerizing, soothing to the soul."
    "How could I ever destroy it? It breathes peace and tranquility."
    menu:
        "And I..."
        "Will remain with it.":
            jump stayWithRelic
        "Must leave.":
            jump leftRelic

# --------------------- ENDING: stay with relic -----------------

label stayWithRelic:
    "I settle down at the foot of the pedestal."
    "This is the calmest I've ever been in my life."
    "I can only imagine what horrors awaited me if I'd destroyed it."
    "Damn the war. It's no longer my concern."
    "May the enemy win, for all I care."
    "Perhaps, if the gods themselves blessed them with this divine thing, then they deserve to win."

    return

# --------------------- / ENDING: stay with relic -----------------

# --------------------- ENDING: left relic -----------------

label leftRelic:
    "I turn to exit the cave. The doubt in my mind subsides as I do."
    "This is the only correct choice. I just know it."
    "My commander won't be pleased, but perhaps she doesn't need to know."
    "Perhaps... I can stay in the forest, instead, away from everything else, and away from this infernal war."

    scene bg forestinner
    with fade
    play music "/audio/forest.ogg"
    "My mind wanders as I leave the cave, again entering the forest."
    "This sacred place hums with tranquility in a way I hadn't heard before."
    "I settle at the foot of an ancient tree, branches gnarled and reaching across the sky."
    "Forget the war. Forget the violence, the rage and bloodshed."
    "This is where I'll stay. Now, and forevermore."
    
    return


# --------------------- / ENDING: left relic -----------------

label exitCave:
    # The Road Back Home
    scene bg forestinner
    with fade
    play music "/audio/forest.ogg"
    "I exit the cave and make my way back through the forest. It's quiet, now."
    "The grass withers under my feet as I walk. Trees bend and sway and crack as I pass by."
    "The sky has turned. The clouds look as if they're ready to break open at any moment."
    "The shadows look a little darker, feel a little deeper, as if some terrible void watches me from within."
    "That {color=#f00}thing{/color} in the back of my mind prods at me. It just won't leave me be."

    # Master of Two Worlds
    "I don't know what happened to me when I destroyed the relic, but I know something has changed within me."
    "I feel it simmering in my blood. It burns, cutting to my core."
    "I can barely breathe. My vision clouds, my head swims."
    menu:
        "I..."
        "Pause for a moment.":
            jump catchBreath
        "Press onwards.":
            jump keepGoing


label catchBreath:
    "I slump against an ancient tree trunk. Its bark crumbles at my touch."
    "I desperately try to catch my breath, there in the thick of the forest."
    "I glance up, to the canopy. The light filtering down glows a sickly green."
    "The forest is dying. I know this, though I don't know how I do."
    "I'm tempted to stay here and die with it."
    menu:
        "I..."
        "Close my eyes.":
            jump closedEyes
        "Get back up.":
            "I toss the thought aside, and shakily return to my feet."
            jump keepGoing

label closedEyes:
    "The chill of the forest overwhelms me. All warmth is gone."
    "I'm so tired."
    "Whatever power was thrust upon me, it was never meant for my kind."
    menu:
        "..."
        "Give up.":
            jump death
        "Get up.":
            jump keepGoing

label death:
    "I lay there, against the tree, for what my mind perceives as eons."
    "I feel the shadows licking at the trees, strangling them. They're haunting. There is no rest, here."
    "...But maybe I'll find mine, anyway."
    "In my last moments, I think of my past. My family. My successes, my failures."
    "All has led me here, to this forest and this moment, to die."
    "I feel myself slip away."
    "Here, at the end of all things, I'm left only with regret."
    return

label keepGoing:
    "I stand. I keep going. I must get back, report my success."
    "However, I can't shake the sinking feeling that something has gone horribly wrong."
    "The birds that once flooded this forest with their songs are nowhere to be heard."
    "The beasts that once hindered my path are nowhere to be seen."
    "The land is eerily silent, as if it has died, itself."
    "The silence is deafening. My ears ring in a vain attempt to find some sort of sound."

    # Return with Special Knowledge
    scene bg field
    with fade
    play music "/audio/cave.ogg"
    "When I step out of the thickets, I see that the world has turned, and the land is barren and empty of all things..."
    "{color=#f00}...including the people.{/color}"
    "What happened?"
    "What have I done?"
    "I stand there, atop the hillside, staring out over a battlefield lost to all known things."
    "What do I do now?"
    "I stay still for a long time, trying to think of something - anything - that can change this."
    "I have nothing. I can't go back in time to stop myself. I can't bring anyone back."
    "...Can I?"
    "I wander to our encampment. As expected, it's empty."
    menu:
        "But maybe..."
        "Go to my brother's tent.":
            jump brothersTent
        "Go to my commander's tent.":
            jump commandersTent

# ------------------- ENDING: brother -----------------------------------

label brothersTent:
    "I peer inside. Per usual, it's cluttered with magical trinkets and tomes."
    "One in particular catches my eye: a book on the divine."
    "I pick it up and open it. It's filled with theories and incantations."
    "I know these spells, somehow. They're familiar, though I know I've never before seen them in my life."
    "One of them speaks of reversing the effects of tragedy - any tragedy."
    "That's exactly what I'm looking for."
    menu:
        "Cast the spell.":
            python:
                if (wisdom >= 3):
                    renpy.jump("brothersReturn")
                else:
                    renpy.jump("notReturn")

label brothersReturn:
    "I cast the spell and wait. The tome crumbles to ash in my hand, but nothing seems to happen."
    "I wait a little longer, then a little longer still..."
    "The sun falls below the horizon, and I finally exit the tent."
    "Maybe such divine spells don't work from the fingertips of the unholy."
    "I return to my own tent and sit, melancholy, on my cot. I suppose I'm alone, now, forever."
    "I ponder this until the sun again rises, blood-red and angry, over the mountains."
    "Then, I hear footsteps."

    show brother neutral at midright
    with dissolve
    "I've never been more relieved to see someone in my life."

    show warlord neutral at midleft
    with dissolve
    warlord "It worked."
    brother "What worked? What happened?"
    brother "Where is everyone?"
    warlord "...Gone."
    brother "Gone? Gone where? How?"
    menu:
        "Tell him.":
            jump toldHim
        "Don't tell him.":
            jump didntTellHim

label toldHim:
    "I recount the events that brought us to this end... everything, the relic, the destruction, the vanishing."
    "He's quiet for a long moment."
    brother "Oh."

    jump endWorldBrother

label didntTellHim:
    warlord "It's too much to explain. Just know..."

    jump endWorldBrother

label endWorldBrother:
    brother "Right."
    warlord "It's..."
    brother "The end of all things."

    python:
        if hasTrinket:
            renpy.jump("fixThingsBrother")
        else:
            renpy.jump("endBrother")

label fixThingsBrother:
    warlord "Yes."
    "We turn to the sun, watching it rise over the land."
    "Absent-mindedly, I pull the trinket from the forest out of my pocket."
    "The sun glints off of it, like a brilliant light in the dark."
    brother "Hey. That's a divine token..."
    warlord "A what?"
    brother "It can undo this. Undo... whatever the gods did, here."
    brother "Only if you're willing to sacrifice yourself, though."
    "I stare at the small thing in my hand."
    brother "I can't ask that of you."
    warlord "You don't have to. It's my decision."
    menu:
        "Undo everything.":
            jump sacrificeSelf
        "Throw it away.":
            jump endBrother
    return

label endBrother:
    "We both fall silent."
    "There's nothing else to be done."
    "We turn to the sun, watching it rise over the land, staining the countryside in light too sickly to be right."
    "At the end of the world, at least we have each other."
    return

# ------------------- / ENDING: brother -----------------------------------

label sacrificeSelf:
    "I take a shaky breath and will the token to life."
    "It shines with brilliance, with all the divine energy I before destroyed."
    "With my final breaths, I look to the one beside me, and as I fade into nothing, I know..."
    "This is the only decision I've made today that's been right."
    return


# ------------------- ENDING: commander -----------------------------------

label commandersTent:
    "I peer inside. Per usual, it's cluttered with tactical maps and notes and orders from on high."
    "One particular book, however, catches my eye."
    "I pick it up and open it. It's filled with studious notes on the gods and their miracles."
    "Some of the notes are scribbled next to spells."
    "I know these spells, somehow. They're familiar, though I know I've never before seen them in my life."
    "One of them speaks of reversing the effects of divine intervention."
    "That's exactly what I'm looking for."

    menu:
        "Cast the spell.":
            python:
                if (strength >= 3):
                    renpy.jump("commandersReturn")
                else:
                    renpy.jump("notReturn")

label commandersReturn:
    "I cast the spell and wait."
    "The tome crumbles to ash in my hand, but nothing seems to happen."
    "I wait a little longer, then a little longer still..."
    "The sun falls below the horizon, and I finally exit the tent."
    "As I turn to return to my own, I hear a familiar voice behind me."

    show queen neutral at midright
    with dissolve
    "I've never been more relieved to see someone in my life."

    show warlord neutral at midleft
    with dissolve
    warlord "It worked."
    commander "So I see."
    commander "Normally, this is the part where I'd commend you. However..."
    warlord "I know. Everyone's gone."
    commander "This... was not what I was expecting."
    warlord "The end of all things."
    commander "Yes."
    "We both turn to face the setting sun, falling silent."

    python:
        if hasTrinket:
            renpy.jump("fixThingsCommander")
        else:
            renpy.jump("endCommander")

label fixThingsCommander:
    "Absent-mindedly, I pull the trinket from the forest out of my pocket."
    "The sun's final light glints off of it, like a brilliant beacon in the dark."
    commander "Ah. A divine token..."
    warlord "A what?"
    commander "Another divine relic. It can undo the damage we've done."
    commander "But only if you're willing to sacrifice yourself."
    "I stare at the small thing in my hand."
    commander "I cannot ask that of you."
    warlord "You don't have to. It's my decision."
    menu:
        "Undo everything.":
            jump sacrificeSelf
        "Throw it away.":
            jump endCommander
    return

label endCommander:
    "There's nothing else to be done."
    "At the end of the world, at least we're not completely alone."

    # This ends the game.
    return

# ------------------- / ENDING: commander -----------------------------------

# ------------------- ENDING: alone --------------------------------------

label notReturn:
    "In a blinding flash, the tome in my hand burns to a crisp."
    "It leaves behind only ash, staining my fingers and leaving an acrid stench in the air."
    "In that moment, I know only one thing, though I can't explain how I know."
    "I am alone."
    "I am alone, forever."
    return

# ------------------- / ENDING: alone --------------------------------------