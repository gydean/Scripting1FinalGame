# set the stage and give the starting options.

import charactersetup
import settings


# Introduction
print("\033[97m It's the year 2XXX. Your name is\033[95m", charactersetup.player_name,"\033[97mand you're a simple \"contractor\".",
      "Justice is screwed at this point.",
      "\nIt only serves the upper city, leaving the lower city and the outskirts to shit.",
      "\nSo, many folk took it upon themselves to keep order their own way...",
      "by either doing it themselves or hiring \"contractors\" to do if for them.",
      # next paragraph
      "\nUnlike most contracters in your league, not too decked on cybernetics, and still can hold you're own in a good ol fist fight.",
      "\nIt gives you to advantage being mostly unhackable. Downside is, you're not armed to the teeth built in weapons and death defying tech.",
      "\nBut that doesn't really bother you. You are in good shape and that's all that matters."
      "\n\n[\033[97m you have\033[92m", settings.health, "health\033[97m so far ]"
      # next paragraph
      "\n\nAnyway, the night is your own. You got some time to kill, people to kill, and just avoid getting yourself killed",
      "\nYou currently don't have any jobs so you can either do one of the following:")
print("\n\n",
      "\033[93m1. Go to bar\n", # enter_bar
      "\033[93m2. Screw the bar\033[97m") # start_early

# first branch, start at chapter one or chapter two

p_choice = int(input("\n(Please select 1 or 2)\n\n"))

if p_choice != 1 and p_choice != 2:
    while p_choice != 1 and p_choice != 2:
        print("Please choose one of the options!")
        print("\033[93m1. Go to bar\n\033[97m",
      "\033[93m2. Screw the bar\033[97m")
        # old dialogue:  Let's get this shit started already (shit as in game or job lol)
        p_choice = input()

# this will help make sure to give a summary to those who skip to chapter 2
# player goes to chapter 1
if p_choice == 1:
    settings.branch_one = 1
    import chapterone
# player goes to chapter 2
if p_choice == 2:
    settings.branch_one = 2
    import chaptertwo
