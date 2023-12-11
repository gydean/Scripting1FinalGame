# chapter one
# intro, drink, talk, gamble, introduce jobs

import charactersetup
import settings
from random import randint
import achivements




# All my fricking functions for this chapter....includes dialogue and micro-options

#######################################

# Buy a drink
def buy_a_drink():
      print("\033[97mYou sit down on a sleek barstool and a bar bot slid over to serve you.",
      "\n\"What can i get for you?\" it asked, with its smooth white plastic face. There was only a rather off-putting LED smiley face projected onto the face.",
      "\n\"Eh...I'll have a chervar...on the rocks...\"",
      "\n\"Coming right up,\" it chirped synthetically.",
      "\nIt then turned around, grabbed a few ingredients, funneled it into itself and then turned back around, to serve the drink from the mixing compartment in it's chest.",
      "\nIt didn't even take a minute, and there was a even little artificial cherry on top of the round ice just how you liked it.")
      settings.money = settings.money - 10
      print("\n[\033[92m10 credits\033[97m] have been subtracted from your account. Your balance is now\033[92m", settings.money,"\033[97m]")
      print("\nYou took the glass in your hand tentatively, taking a small sip."
      "\nIt was perfect. it was always perfect. you've always found non-human service a bit uncanny. Sure, it was fast and efficient, but sometimes too much so.",
      "\nBut enough on that. You're not here to introspect. With a sigh, you took another small sip from your drink.",
      "\nYou notice there is a lady next to you. She seems to be in her mid 20s, and has a ghost of as scowl on her face as she looked wearily at her drink.")

#######################################

# Talk to the lady
def talk_to_her():
    # to avoid repeats if player is male and 50+
    # i probably coded this miserably BUT OH WELL LOL
    talked_to_her = 0

    # response if old (includes if male too)
    if charactersetup.player_age > 50:
        print("You look over at her and asked, \"What's with the sad face?\"",
              "\nShe looked over with a scowl on her face. \"None of your damn business.\" and she curtly looked back to her drink grouchily.",
              "\n\"Well sheesh, sorry kid...\" you muttered under your breath sarcastically.",
              "\nPeople these days...")
        input("\n\n\033[93mEnter any key to continue.\033[97m\n")
        if charactersetup.player_gender == "Male":
            achivements.sugar_daddy_failed = "Sugar Daddy Failed Edition (get ignored cuz of your AGE and GENDER u_u)"
            talked_to_her = 1

    # response if male (and not old)
    if charactersetup.player_gender == "Male" and talked_to_her != 1:
          print("You look over at her and asked, \"What's with the sad face?\"",
            "\nShe looked over with a scowl on her face. \"None of your damn business.\" and she curtly looked back to her drink grouchily.",
            "\n\"Well sheesh, sorry,\" you muttered under your breath sarcastically. And mentally added \"bitch\"",
            "\nPeople these days...")
          achivements.bish = "Bish (get ignored by lady)" # dang the sexism u_u
          input("\n\n\033[93mEnter any key to continue.\n\033[97m")

    # response if female
    if charactersetup.player_gender == "Female":
        print("You look over at her and asked, \"What's with the sad face?\"",
               "\nShe stiffened, and gave a confused look. She looked at you for a moment skeptically, but then her expression softened.",
               "\n\"Heh, just stupid relationship problems,\" She joked weakly.",
               "\nYou offered a sympathetic smile, \"Those always suck...\"",
               "\n\"No shit...nothing I can do about it...can't do much about it even if I wanted too. He's so untouchable...\" She groaned and rolled her eyes.",
               "\nYou were a little confused, \"What do you mean...?\"",
               "\n\"Would you believe me if i told you I was dating the oh-so-famous Wynter?\"",
               "\n\"Really??\" Micheal Wynter was a famous (perhaps infamous) young CEO/inventor."
               "\nHe was known for his eccentric robotics projects and his non-stop controversial social media posts.",
               "\n\"Mmhm, but he's a jerk. Never has time for me, or anyone, other than his stupid robots. Maybe it's retribution that \033[95mone of his robots finally went rogue\033[97m...\"",
               "\n\"...??\"",
               "\"Oh, forgot that wasn't out the loop yet,\" She shrugs. \"Well, I hope it gets out soon. Would love to see how he'll rebound from this.\"",
               "\nShe sighed and continued. \"Would leak it myself, but he literally made me sign an NDA. Can you believe that?? Making your own girlfriend sign an NDA??\"",
               "\nYou winced empathically, \"Ah...\"",
               "\n\nYou and the lady, who's named you learned to be Rosiri, continued to exchange some small talk until she had to leave.",
               "\nIt was a nice little distraction, but you probably should find something better to do.")
        achivements.good_listener = "Good Listener (successfully talk to lady)"
        input("\n\n\033[93mEnter any key to continue.\033[97m\n")

    # response if ???
    if charactersetup.player_gender == "???":
        print("You look over at her and asked, \"What's with the sad face?\"",
               "\nShe stiffened, and gave a confused look. She looked at you for a moment skeptically, but then her expression softened.",
               "\n\"Heh, just stupid relationship problems,\" She joked weakly.",
               "\nYou offered a sympathetic smile, \"Those always suck...\"",
               "\n\"No shit...nothing I can do about it...can't do much about it even if I wanted too. He's so untouchable...\" She groaned and rolled her eyes.",
               "\nYou were a little confused, \"What do you mean...?\"",
               "\n\"Would you believe me if i told you I was dating the oh-so-famous Wynter?\"",
               "\n\"Really??\" Micheal Wynter was a famous (perhaps infamous) young CEO/inventor."
               "\nHe was known for his eccentric robotics projects and his non-stop controversial social media posts.",
               "\n\"Mmhm, but he's a jerk. Never has time for me, or anyone, other than his stupid robots. Maybe it's retribution that \033[95mone of his robots finally went rogue\033[97m...\"",
               "\n\"...??\"",
               "\"Oh, forgot that wasn't out the loop yet,\" She shrugs. \"Well, I hope it gets out soon. Would love to see how he'll rebound from this.\"",
               "\nShe sighed and continued. \"Would leak it myself, but he literally made me sign an NDA. Can you believe that?? Making your own girlfriend sign an NDA??\"",
               "\nYou winced empathically, \"Ah...\"",
               "\n\nYou and the lady, who's named you learned to be Rosiri, continued to exchange some small talk until she had to leave.",
               "\nIt was a nice little distraction, but you probably should find something better to do.")
        achivements.good_listener = "Good Listener (successfully talk to lady)"
        input("\n\n\033[93mEnter any key to continue.\033[97m\n")

#######################################

# story text
def ignore_her():
    print("Chatting would strangers would be a waste of your time. \nYou decided to ignore her and continued sipping at your drink.")
    input("\033[93m\n\nEnter any key to continue.\n\033[97m")

#######################################

# more story text
def look_around():
      print("You decided to take in your surroundings a little longer."
            "\nThere was a TV in the back broadcasting the lasted Wire N Steel match, a to-the-\"death\" robot fight show."
            "\nThe holo below to the TV streamed the current bets on who'd win."
            "\nYou watch as many people clustered around the TV in anticipation, and as the bets on the holo trickle up.")

#######################################

# picking a winner
def place_a_bet():
    print("\033[97mJust for the heck of it, you decided to place a bet. You currently have\033[92m", settings.money,
          "credits\033[97m on hand.",
          "\n\nThere seems to be two champions clashing tonight...",
          "\n A meat grinding looking robot named \033[93mPULLED PORK\033[97m",
          "\n And a sleek spiny avian looking robot named \033[93mRAZORBEAK\033[97m",
          "\n\nRather cringe names. Almost sounds like a strange reference to two different sci-fi medias...",
          "\n\nWhatever. Which one do think you will win?")
    print("\033[93m1. PULLED PORK \n2. RAZORBEAK \033[97m")

    # players choice
    winner_choice = int(input())

    # if wrong user input
    while winner_choice != 1 and winner_choice != 2:
        if winner_choice != 1 and winner_choice != 2:
            print("Please pick either 1 or 2!")
            print("\033[93m1. PULLED PORK \n2. RAZORBEAK\033[97m")
            winner_choice = int(input())

    # to display players choice in text
    fighter_name = ""

    if winner_choice == 1:
        fighter_name = "\033[93mPULLED PORK\033[97m"
    if winner_choice == 2:
        fighter_name = "\033[93mRAZORBEAK\033[97m"

    # betting time baby
    print("Now, how much do you want to bet? Your current balance is\033[92m", settings.money, "credits\033[97m")

    bet = int(input())

    # if player bets more than 1000
    while bet > settings.money:
        if bet > settings.money:
            print("Dude you can't bet more than you have!!")
            print("Pick another amount. Your current balance is\033[92m", settings.money, "credits\033[97m")
            bet = int(input())

    # some sillies if user picks extremes
    if bet == settings.money:
        print("Damn, you really want to bet that much? Okay...")
        achivements.risk_taker = "Risk Taker (bet all money)"

    # some more sillies
    if bet == 1:
        print("Coward...but anyway.")
        achivements.playing_it_safe = "Playing It Safe (bet just one credit)"

    # im not sure how to check if player put a negative number (it'd register as a string cuz "-")...

    # OK INSERT WAIT TIME HIGHLIGHT IMPORTANT INFO
    print("\n You place\033[92m", bet, "credits\033[97m on ", fighter_name, ", and sat at a table, watching the match.")
    input("\n\n\033[93mEnter any key to continue.\n\033[97m")
    print("\nThe match, as they all are, was over hyped, and your attention soon drifted to the nearby conversations.",
          "\nYou couldn't help but overhear two nerds with their laptops sitting at a side booth."
          "\nThey seemed to be talking about \033[95msome android on the loose\033[97m. You frown, you haven't heard about that.",
          "\nThey continued to speculated what happened, whether it had gone rogue or was being remotely controlled.", # highlight rogue/controlled part?
          "\nYou mentally tucked that info away, you should look into it later.",
          "\n\nSuddenly the room burst into a mix of cheers and boos, and you look up to see the match had ended...")

    # to allow for spacing things out, so code doesnt info dump user
    input("\n\n\033[93mEnter any key to continue.\033[97m\n")

    ##############
    # picking a winner, and then telling if user got it right or wrong, add/subtracting wins/losses accordingly
    razorwin = "nothing"
    pullwin = "nothing"
    pulled_pork = 1
    razorbeak = 2

    winner = randint(1, 2)
    # print(winner) <-- for testing

    if winner == razorbeak:
        print("\033[93mRazorbeak won!\033[97m ]")
        razorwin = "win"
        pullwin = "lose"

    elif winner == pulled_pork:
        print("\033[93mPulled Pork won!\033[97m ]")
        pullwin = "win"
        razorwin = "lose"

    # dumb stupid complicated if/else statements on how it sees if you win or not
    # i need to simplify this but my brain cannot

    # player wins
    if pullwin == "win" and winner_choice == 1:
        settings.money = settings.money + bet
        print("\033[97mWoah! You won!")
        print("[Your balance is now\033[92m", settings.money, "credits\033[97. ]")
        achivements.progambler = "Pro-Gambler (win bet)"

    if razorwin == "win" and winner_choice == 2:
        settings.money = settings.money + bet
        print("\033[97mWoah! You won!")
        print("[Your balance is now\033[92m", settings.money, "credits\033[97. ]")
        achivements.progambler = "Pro-Gambler (win bet)"

    # player loses
    if pullwin == "lose" and winner_choice == 1:
        settings.money = settings.money - bet
        print("\033[97mDang sucker, you just lost")
        print("[You lost\033[91m", bet, "credits\033[97m. Your balance is now\033[92m", settings.money,"credits\033[97m. ]")

    if razorwin == "lose" and winner_choice == 2:
        settings.money = settings.money - bet
        print("\033[97mDang sucker, you just lost")
        print("[You lost\033[91m", bet, "credits\033[97m. Your balance is now\033[92m", settings.money,"credits\033[97m. ]")

#######################################

# get job message
# FINALLY GET TO STORY PROGRESS LOL
def get_job():
    print("You suddenly are interrupted by the buzz of your phone. You slip it out of your pocket to check it out.",
          "\nIt appeared you got a encrypted message. You unlocked your phone and opened the app.",
          "\nThe contents of the message was currently gibberish, but you ran your private key through and decoded its contents.",
          "\nAh yes, it was from\033[95m Unyx\033[97m, your handler, and it seems like he a job for you.",
          "\nFinally, something useful to do.")
    input("\033[93m\n\nEnter any key to continue.\n\033[97m")



#######################################

# read message
def read():
    print("\nIt read:"
          "\n\"" + charactersetup.player_name +",",)
    print("\nGot a new job for you. Our client needs you to \033[95mretrieve a lost robot\033[97m for them. The award is \033[92m25000 credits\033[97m.",
          "\nThey didn't disclose much, but it apparently \"wandered off\". It is not functioning correctly so be careful.",
          "\nThe client prefers if the target is undamaged and will provide a bonus if you can pull that off.",
          "\nI know, a trivial task, but I suspect this \033[95mrobot is dangerous\033[97m, but the client refused to confirm that.",
          "\nI also think we're not the first people they've contacted about this...perhaps the others have failed...",
          "\nI understand if you want to pass this one over. However, if you do want to take this on, I attached the last known location of the target.",
          "\nHappy hunting and be careful.\"")
    input("\033[93m\nEnter any key to continue.\033[97m\n")
    print("\nAs suspicious as the job seems, you're bored (and perhaps stupid) enough to give it a shot.",
          "\nUynx is probably just being paranoid anyway. Anyway, it's best you head home to get geared up.")
    input("\033[93m\nEnter any key to continue.\033[97m\n")

#######################################

# game stuff now, calls all the functions in order
print("You head over the closest bar across the street. It's neon sign glimmered The Vennel.",
      "\nIt seemed busy inside, you could hear the muted the sound of voices and glasses clinking.",
      "\nYou enter the bar, because the writer can no longer think of anything more descriptive to write about.",
      "\nIndeed, the bar was busy. Not so much on the actual counter itself. Most of the activity was more towards the side with the sit-down areas.")

print("\033[93m","1. Buy a drink",
      "\n2. Look around\033[97m")

choice_1 = int(input("Please pick 1 or 2\n"))

# buy a drink
if choice_1 == 1:
    # route one
    buy_a_drink()


    # talk to her?
    print("\033[93m1. Talk to her", "\n2. Ignore her\n\033[97m")

    choice_talk_to_her = int(input())

    if choice_talk_to_her == 1:
        talk_to_her()
        get_job()
        read()

    elif choice_talk_to_her == 2:
        ignore_her()
        get_job()
        read()

# look around
elif choice_1 == 2:
    # snooper
    look_around()
    # looking_around += 1 <-- do i need?

    # gamble or drink choice
    print("\033[93m1. Join in on the betting", "\n2. Pah, go buy a drink instead\n\033[97m")

    choice_gamble = int(input())

    # mm yes 50/50 risk
    if choice_gamble == 1:

        place_a_bet()

    # screw gambling lets buy a drink
    elif choice_gamble == 2:

        buy_a_drink()

        # talk to her?
        print("\033[93m1. Talk to her,", "\n2. Ignore her\033[97m")

        # talk to her code reused from above
        choice_talk_to_her = int(input())

        if choice_talk_to_her == 1:
            talk_to_her()
            get_job()
            read()

        elif choice_talk_to_her == 2:
            ignore_her()
            get_job()
            read()

    # kinda dumb way to do this BUT LETS DO IT
    if settings.money > 1000:
        print("\033[97m\nYou chuckle to yourself. Well, that minor excursion was fruitful.\n")
        get_job()
    elif settings.money < 1000:
        print("\033[97m\nYou cursed under your breath. Well, that was a waste of your time.\n")
        get_job()
    # implies they skipped gamble
    else:
        # UH WHAT DO I DO HERE?
        # is this necessary o-|-<
        pass
        # print("normal tie in")

    # read the message
    read()




# I NEED TO GO BACK TO GAMEPLAY PART AND PUT IN LOOPS TO PREVENT MISCLICK/INVALID INPUT
# ....if i have time........