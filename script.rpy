label splashscreen:
    menu:
      "{cps=10000}You are playing an unstable development build. May contain bugs, incomplete assets, and missing portions. \nGame is subject to change. \nPlease report any issues to the developer."
      "I understand.":
        jump choice0_truth

    label choice0_truth:
      $ menu_flag = True

      jump choice0_done

    label choice0_done:

    menu:
      "{cps=10000}This game is not suitable for children or those who are easily disturbed. \nAre you 17 years or older?"
      "Yes":
        jump choice1_truth
      "No":
        $ renpy.quit()

    label choice1_truth:
      $ menu_flag = True

      jump choice1_done

    label choice1_done:
return

define config.mouse = {"default" : [("images/mouse 2.png", 0, 0)]}
define v = Character("V")
default preferences.text_cps = 100


transform moveright:
  linear 0.5 xpos 1.0
label start:

    window hide
    play music "ssh.mp3"
    scene disclaimer 1 with dissolve
    pause 5.0
    scene disclaimer 2 with dissolve
    pause 5.0
    scene unix 1
    pause 1.0
    scene glitch 1 with dissolve
    pause 2.0
    scene 1

    "The worker drone’s eyes appear on their broken visor, looking around, almost panicked."
    "They couldn’t speak.{w} Not yet."
    "They start wiggling their way out of the dead worker they were trapped under, shoving the corpse off when their arms were free."
    "Starting to climb, they felt something land on their shoulder."
    "A crow."
    "It just stared at them with a weird look in its eyes…"
    "Then,{w} the crow flew off their shoulder and perched up on the edge of the heap of drones they’re climbing."
    "The drone starts to climb with more of a rushed pace, finally making it to the top, until, suddenly,{w} they’re deactivating."


    return
