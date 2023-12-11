import chaptertwo
import achivements
import settings
import charactersetup
# import chapterone # for message function cuz im lazy
# EDIT: GAH NO THAT WAS EVIL DONT DO THAT OR ELSE IT'LL RUN ALL OF CHAPTER 1????

player_weapon = ""
player_tool = ""
customizing = True

#######################################

# character weapon
def pick_a_weapon():
    print("Pick your weapon. Choose a number.")
    print("\033[93m1. Pistol \n2. Semi-Auto Rifle \n3. Shotgun\033[97m")
    # make sure in later game it's referred in lowercase <-- edit: huh what does that mean

    # come back later and do some code in case someone types in letters instead <-- edit: NO IM TOO TIRED IT'S 1 AM
    weapon = int(input())

    # player picks invalid option
    if weapon < 1 or weapon > 3:
        while weapon < 1 or weapon > 3:
            print("Please choose one of the options!",
                  "\n\033[93m1. Pistol",
                  "\n2. Semi-Auto Rifle",
                  "\n3. Shotgun\033[97m")
            weapon = int(input())

    # weapon options
    if weapon == 1:
        chaptertwo.player_weapon = "Pistol"
        achivements.pew_pew = "Pew Pew (pick a pistol)"

    if weapon == 2:
        chaptertwo.player_weapon = "Rifle"

    if weapon == 3:
        chaptertwo.player_weapon = "Shotgun"

#######################################

def pick_a_tool():
    # character tool
    print("Pick a tool:",
          "\n\033[93m1. EMP Grenade",
          "\n2. HaK-mADe-EZ Gadget",
          "\n3. a mop. yes. a literal old mop. slightly musty.\033[97m")
    tool = int(input())

    if tool == 1:
        chaptertwo.player_tool = "EMP"
    if tool == 2:
        chaptertwo.player_tool = "HaK-mADe-EZ Gadget"
    if tool == 3:
        chaptertwo.player_tool = "mop"

########################################

# OK ONTO THE "STORY" OF CHAPTER 2

########################################
# gives character an alternative to getting and reading job message
if settings.branch_one == 2:
    print("You decided to head home. Drinking is overrated anyway.",
          "\nAs you were heading home, you get a message on your phone.",
          "\nYou check it out to see it is from\033[95m Unyx\033[97m, you're handler. It appears he has a job for you.")

    input("\n\n\033[93mEnter any key to continue.\033[97m\n")

    print("\nThe message reads: \n",
          charactersetup.player_name, ",",
          "\nGot a new job for you. Our client needs you to retrieve a lost robot for them. The award is 25000 credits.",
          "\nThey didn't disclose much, but it apparently \"wandered off\". It is not functioning correctly so be careful.",
          "\nThe client prefers if the target is undamaged and will provide a bonus if you can pull that off.",
          "\nI know, a trivial task, but I suspect this robot is dangerous, but the client refused to confirm that.",
          "\nI also think we're not the first people they've contacted about this...perhaps the others have failed...",
          "\nI understand if you want to pass this one over. However, if you do want to take this on, I attached the last known location of the target.",
          "\nHappy hunting and be careful.")
    print("\nAs suspicious as the job seems, you're bored (and perhaps stupid) enough to give it a shot.",
          "\nUynx is probably just being paranoid anyway. Anyway, it's best you that you're heading home. You'll need to gear up.")
    input("\n\033[93mEnter any key to continue.\n\033[97m")

# implies player has played chapter 1
else:
    # do i even need this or what o-|-<
    pass



print("\n[\033[93mYou arrive home\033[97m]")

print("\nOkay, time to first select your weapon. While of course you don't want to have to use them so you can get the bonus,"
      "\nbut given what Uynx said, it's best to bring something just in case things get hairy. You head over to your weapon stash...\n")
pick_a_weapon()

print("\nNow, you'll probably need something else to get the robot with that won't cause too much damage.",
      "\nYou decide to go check your tools to see if anything would be helpful...")
pick_a_tool()

print("\n\nAll geared up! Your current loadout is:",
      "\n\033[93mWeapon:", player_weapon,
      "\nTool:", player_tool)

print("\n\033[97mWould you to redo your selection? Y/N")
choice = input()
if choice == "y" or choice == "yes" or choice == "Y" or choice == "Yes" or choice == "YES" or choice == "yES" or choice == "yeS" or choice == "yEs":
    customizing = True
if choice == "n" or choice == "N" or choice == "no" or choice == "No" or choice == "NO" or choice == "nO":
    customizing = False

while customizing == True:
    pick_a_weapon()
    pick_a_tool()
    print("\n\nYour current loadout is:",
          "\n\033[93mWeapon:", player_weapon,
          "\nTool:", player_tool)
    print("\n\033[97mWould you to redo your selection? Y/N")
    choice = input()
    if choice == "y" or choice == "yes" or choice == "Y" or choice == "Yes" or choice == "YES" or choice == "yES" or choice == "yeS" or choice == "yEs":
        customizing = True
    if choice == "n" or choice == "N" or choice == "no" or choice == "No" or choice == "NO" or choice == "nO":
        customizing = False

print("\nYou're now ready to go.",
      "\nDouble checking you got all that you need, you set up your navigation on your phone and started to head to your target's location.")
input("\n\n\033[93mEnter any key to continue.\n\033[97m")

