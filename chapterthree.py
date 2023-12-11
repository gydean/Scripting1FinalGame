# FINALLY THE GAME
import chapterthree
import chaptertwo
import settings
import achivements


damaged = False
bonus = False

# player chooses to go through the front
def the_front():
    print("You walk into the front doors carefully.",
          "\nThere many boxes stacked up everywhere, but there was a path of knocked over boxes in the middle...that led up to where the android was at.",
          "\nYou could see it just standing there. It seems to be spazing out, clutching it's head and quietly muttering something over and over.",
          "\nThe screen on it's head was full of static.",
          "\nYou freeze, hoping it didn't notice you yet.",
          "\nBut it was too late. it perked up and immediate fixed it's eyeless gaze upon you.",
          "\nWhatever it was muttering before slowly started to increase.",
          "\n\"USELESS,\" it seemed to chant. \"USELESS, USELESS, USELESS\"",
          "\nAt the fourth shriek it starts moving towards you. slow at first but slowly picking up pace."
          "\nFor a second you freeze in shock, and then you instinctively scramble for your weapon, flip off the safety and shoot---")

    # how affective their defense is varies on their equipment
    if chaptertwo.player_weapon == "Rifle":
        print("\nYou open fire with your", chaptertwo.player_weapon, "and only after a blowing through half your mag were you finally able to stop the rampaging android.",
              "\nFor a moment, you just stood there, panting hevaily, staring down at shock at the mangled robotic body before you.",
              "\nAfter regaining your bearings, you roll the android over to see it's chassis pelted with bullet holes.",
              "\nYou wince. You're probably not going to get that bonus...",
              "\nBut what's done is done, now you just have to get in contact with your client for the retrieval steps.")
        chapterthree.damaged = True

    if chaptertwo.player_weapon == "Shotgun":
        print("\nYou open fire with your", chaptertwo.player_weapon,
              "\nIt took a couple slugs to the android's face and body for it to fully collapse",
              "\nFor a moment, you just stood there, panting heavily, staring down at shock at the mangled robotic body before you.",
              "\nAfter regaining your bearings, you roll the android over to see its faceplate shattered and its chestplate cracked.",
              "\nYou wince. You're probably not going to get that bonus...",
              "\nBut what's done is done, now you just have to get in contact with your client for the retrieval steps.")
        chapterthree.damaged = True

    if chaptertwo.player_weapon == "Pistol":
        print("\nYou open fire with your", chaptertwo.player_weapon,
              "\nHowever, your handgun couldn't  effectively penetrate the target at that range and all you ended up with an empty mag and a rapidly advancing android.")
        if chaptertwo.player_tool == "EMP":
            print("\nSomehow, in your panic, you suddenly remembered you brought an EMP grenade with you."
                  "\nYou hastily got it out and activated it in your head, as the android was so close to grabbing your face at this point.",
                  "\nThere was a sudden zap and your heart skipped a beat or two from the discharge. You collpased, but so did the android.")
            settings.health = settings.health - 25
            print("[You lost 25 health. Remaining health is", settings.health, "]")
            print("\nAfter a moment of regaining your bearings, you slowly sat up and saw that android was now powered off...smoking a little too in the head.",
                  "\nYou sighed in relief. That isn't too much damage right...?"
                  "\nYou pulled out your phone to call the client but then realized..."
                  "\nYou groaned, your phone's screwed too of course. But your earnings should be enough to get you a new one...")
            # print("....and now you ruined all your tech with you") <-- old line
            achivements.your_phone = "RIP Phone (use EMP grenade poorly)"
            chapterthree.bonus = True
        else:
            print("\nYou have nothing else to defend yourself with, so you turn tails and try to make a run for it.",
                  "\nBut by that point, the android was in some sort of uncanny sprint and caught up to you quickly.",
                  "\nIt charged into you almost clumsily, but pinned you down with great force."
                  "\nYou yelped in fright but before you could even think to do anything else, you felt a strong pressure on your neck and--",
                  "\nCRRACK! The android had crushed your neck.")
            settings.health = settings.health - 9999


# player chooses to go through window
def the_window():
    print("\033[97mThere was a window on the side of the building. It was up pretty high, but there was a old dumpster under it.",
          "\nYou can probably scale it and reach the window. The window was already conveniently broken.",
          "\nYou take a deep breath and scale the stinky dumpster. With a leap, you reach the window ledge and haul yourself up.",
          "\nYou don't have foothold on the windowsill so you're just going to have to pull yourself through the window.",
          "\nYou pull yourself through, and in the split second as you go over, you realize there's nothing below you.",
          "\nWell, except for the floor of course.",
          "\nYou plummet down and break one of your legs and arms.",
          "\nRendered helpless in pain, you just laid crumbled there on the floor, dazed.",
          "\nThough blood was roaring in your ears, you could hear mechanical noises nearby.",
          "\nShit, that's got to be the robot. Those noises grew near until you saw a staticky face looming over you.",
          "\n\"\033[1mENTITY?\033[0m\033[97m\" it seemed to garble.",
          "\nYou could do nothing."
          "\nIt silently stared at you for a moment, as if calculating it's next move.",
          "\nThen all of a sudden it shrieked. \"\033[1mUSELESS. USELESS. USELESS.\033[0m\033[97m\"",
          "\nIt raised it's metal primitive leg and the last thing you saw was it's foot plummenting down towards your face.")
    achivements.bro_why = "Bro Why (die via self defenestration)"
    settings.health = settings.health - 9999

# player chooses to go through the back
def the_back():
    print("You decided to stay more on the stealthy side and go in from the back.",
          "\nYou carefully make your way to the back enterance and slip through. So far, you haven't caused any commotion.",
          "\nYou can't see the android just yet given all the old stacked up boxes everywhere. It's almost like a maze.",
          "\nYou think about what to do...\n")

    # if player has hak gadget equipped
    if chaptertwo.player_tool == "HaK-mADe-EZ Gadget":
        print("\nYou suddenly realize that is the perfect distance to use your", chaptertwo.player_tool, "to remote hack the robot.")
        input("\n\n\033[93mEnter any key to continue.\n\033[93m")
        # hacking
        print("Since you got your hak-made-ez, this is the perfect position to use it.",
              "\nYou pull it out and start tapping away. It's basically a small computer dedicating to sending out malicious scripts to any nearby devices it can pick up on the network.",
              "\nYou let it run for a moment, hoping that the android is still connected to the internet and it's firewall dumb enough to fall victim to your digital attacks.",
              "\nYou only ran scripts to try to overload the android's system and force it to shut down.")
        input("\nEnter any key to continue.\n")
        print("\nAfter a few minutes of tensed silence, the gadget sudden lets out a shrill ping to mark it's completion.",
              "\nYou flinch in surprise and drop the gadget, you curse under your breath and pick it up hastily.",
              "\nFor a moment, you just freeze and listen. If the cyberattack didn't work, the android probably would've responded in some way to your sudden noise.",
              "\nHowever, you could hear nothing. Cautiously, you stand up and slowly make your way through the box maze. After awhile you stumble upon the robot.")
        input("\n\n\033[93mEnter any key to continue.\n\033[93m")
        print("\nIt was standing still, powered off. You sigh in relief and you get closer to get a better look at it.",
              "\nIt was a white android, sleek and slender in design. You haven't seen such an elegant robot design before. It had a simple blank faceplate.",
              "\nYou gave it a little poke, just out of curiosity. Nothing happened thankfully.",
              "\nYou couldn't help but wonder if this was that same android that you heard at the bar that got lose. It must be...",
              "\nBut enough about that. You got the job done, and now you just need to contact the client to see how they want their robot taken back.")
        achivements.insert_black_hackerman_meme = "Insert-Black-Hackerman-Meme-Here (hack the android)"
        chapterthree.bonus = True

    # if player has emp equipped
    if chaptertwo.player_tool == "EMP":
        print("If you were to get closer to android, just so that you can peak at it, you might just be able to use your EMP grenade successfully.",
              "At that, you started to slowly creep your way through the box maze."
              "As you got closer and closer to where your map had indicated, the more knocked over boxes you found. Interesting...",
              "The moment you caught a glimpse of the android just past the corner of some boxes, you stop.",
              "You arm your EMP for 3 seconds and...throw!")
        input("\n\n\033[93mEnter any key to continue.\n\033[93m")
        print("The EMP grenade clattered to the android's feet and the robot looked down at it in delayed analysis.",
              "\nHowever, before it could do anything, the EMP went off and gave the android a good shock. It buckled to the floor.",
              "\nYou rush over in triumph and double check it is really down. It is, and you sigh in relief."
              "\nNow, time to call the clients for the next few steps...")
        chapterthree.bonus = True

    # if player has mop equipped
    if chaptertwo.player_tool == "mop":
        print("Since your tool of choice was a mop, you're going to have to improvise on what you're next steps are going to be.")
        print("\n\033[93m1. Sneak closer \n2. Climb the boxes\033[97m")
        mop_choice = int(input())
        if mop_choice == 1:
            print("Given the close-range nature of a mop, you're going to have to get a lot closer to the android to affectively make use of it.",
                  "\nYou start to sneak through the box maze carefully, holding your mop close to yourself to avoid knocking anything over clumsily.",
                  "\nAs you got closer and closer to where your map had indicated, the more knocked over boxes you found.",
                  "\nThe moment you caught a glimpse of the android just past the corner of some boxes, you stop.",
                  "\nYour grip tightens on the mop and you mentally run through you're plan of attack.",
                  "\nYou knew most of the robots most important sensory devices were stored in their head...")
            input("\n\n\033[93mEnter any key to continue.\n\033[93m")
            print("\nYou decided to rush it, going to attack it from behind. The android suddenly turned around to face you.",
                  "\nFreaked out, you swung out the stick part of the mop and slammed it into it's head.",
                  "\nWith it's sensory devices thrown askew from the sudden impact, the android stumbled back.")
            input("\n\n\033[93mEnter any key to continue.\n\033[93m")
            print("\nYou took this opening to take out it's knees, bringing it to the ground.",
                  "\nYou noticed there was small gap between the back of it's head and just under the top of its neck for rotary movement.",
                  "\nWith a smirk, you rammed the mop side of mop into that part, really digging it in there.",
                  "\nThe android started to spaz out and you had to keep it down with one foot to prevent it from trying to escape.",
                  "\nAfter aggressively wriggling the mop deep into the back of the head, it must have done something because the android went limp."
                  "\nTrimuph, you stepped off the android and crouched down to double check. You're not sure how it worked, but it did. And that's all that matters to you!")
            achivements.mop_master = "Mop Master (use a mop like a pro)"
            chapterthree.bonus = True

        if mop_choice == 2:
            print("You suddenly get the urge to climb the books. Perhaps it will give you an advantage over the android.",
                  "\nYou found some good stable boxes and started to scale them. Once you reached the higher levels, you were able to travel across them just like a maze.",
                  "\nYou nearly lost your balance a few times, but it sure was fun. You were able to spot the android towards the center of the building.",
                  "\nAs you attempted to make your way over, one of the boxes at the base of the ones you were on shifted out of place.",
                  "\nYou panicked and tried to get on top of another stack, but that only caused that one to topple over.",
                  "\nYou ended up riding the collapsing boxes to the ground and landed awkwardly on the ground, hurting your right knee in the process.")
            settings.health = settings.health - 45
            print("\n[You lost \033[92m45 health\033[97m. Remaining health is\033[92m", settings.health,"\033[97m]")
            print("\nIt took you a moment to realize, but you had landed just about where the android was.",
                  "\nThe android had been knocked over by some fallen boxes but was getting back up. It then noticed you."
                  "\nFor a moment, it just stood there staring at you, as if it wasn't sure how you got there."
                  "\nBut then suddenly, it shrieked, \"ENTITY? Error. ENTITY.\"",
                  "\nYou couldn't understand what it was garbling, and attempted to get up, but the sharp pain in your knee kept you down.",
                  "\nIt ranted on, \"USELESS! USELESS\" and then it started stumbling towards you, chanting those words over and over.")
            input("\n\n\033[93mEnter any key to continue.\n\033[97m")
            achivements.mop_apprentice = "Mop Apprentice (tried using mop)"


            if chaptertwo.player_weapon == "Pistol":
                print("In a last second attempt to save yourself, you whip our your pistol and shoot it straight in the face.",
                      "\nWith a visceral noise, the faceplate shatters and the android collapses on top of you, still.",
                      "\nAfter getting over the shock of nearly dying, you shove it's body and wince at the it's facial damage.",
                      "\nThere goes your bonus...and as the adrenaline dies down, you are painfully reminded you probably busted your knee.",
                      "\nOh well, the job is done at least...time to call it in.")
                chapterthree.damaged = True
            else:
                print("You tried to crawl away, but it was futile. The robot grabbed your bad leg and pulled it, dragging you back.",
                      "\nYou scream in pain and tried kicking it away with your other leg.",
                      "\nHowever, it remained unbothered by your weak attempts and instead snapped your bad leg, driving your knee cap in and your shin up.",
                      "\nBy this point, you were so beyond dazed and so overwhelmed you felt nothing. You suddenly felt sick and almost started choking on your own vomit."
                      "\nThe android dropped your mangled leg and then stood over you, staring down at your limp half conscious body.")
                input("\n\n\033[93mEnter any key to continue.\n\033[97m")
                print("\n\"Useless\". It garbled, awkwardly crouching down beside you. It reached out it's hand and placed it gently over your heart."
                      "\nBut then it pushed. And it kept pushing until it made your chest cave in and your heart burst.")
                      #"\nYou are obviously dead by this point, but the android didn't fully get this till after it's hand flattened out your heart.")
                settings.health = settings.health - 9999

##########################################

# Actual game
while settings.health > 0 and chapterthree.bonus == False and chapterthree.damaged == False:
    print("\033[97mYou arrive at the location. It appears to be an abandoned packaging warehouse. Odd.",
          "\nOn your map it indicates the target is inside, closer to the front of the building.",
          "\nYou analyze the exterior of the building quietly, trying to figure out your next move.",
          "\nThere is of course the front entrance. There is also a back entrance. Both seemed to have been unlocked.",
          "\nThere are also some exterior windows you could potentially reach."
          "\nHow do you want to enter the building?")
    print("\n\033[93m1. Through the front \n2. Through the back\n3. Through the window\n\033[97m")

    # which way do players want to enter choices
    enter_choice = int(input())
    if enter_choice == 1:
        the_front()
        # break <-- still needed?
    elif enter_choice == 2:
        the_back()
        # break <-- still needed?
    elif enter_choice == 3:
        the_window()


# what to say when character wins/dies
if settings.health <= 0:
     outcome = "failed"
     print("\n...well, you died. Mission failed. Life failed.")
     input("\n\n\033[93mEnter any key to continue.\n\033[97m")
else:
    if damaged == True:
        print("You got the job done...messily. But other than that, job successful.")
        outcome = "won"
        input("\n\n\033[93mEnter any key to continue.\n\033[97m")
    if bonus == True:
        print("You got the job done excellently. Mmm that bonus will be nice...")
        outcome = "won"
        input("\n\n\033[93mEnter any key to continue.\n\033[97m")


