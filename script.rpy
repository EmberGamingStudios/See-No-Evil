label splashscreen:
    menu:
      "You are playing an unstable development build. May contain bugs, incomplete assets, and missing portions. \nGame is subject to change. \nPlease report any issues to the developer."
      "I understand.":
        jump choice0_truth

    label choice0_truth:
      $ menu_flag = True

      jump choice0_done

    label choice0_done:

    menu:
      "This game is not suitable for children or those who are easily disturbed. \nAre you 17 years or older?"
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

transform moveright:
  linear 0.5 xpos 1.0
label start:

    window hide
    play music "ssh.mp3"
    scene disclaimer 1 with dissolve
    pause 5.0
    scene disclaimer 2 with dissolve
    pause 5.0
