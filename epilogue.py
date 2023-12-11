# print out achivements
# put them in a special list to be exported in play.py

import achivements
import chapterthree
import settings

# reward the player money if they won
if chapterthree.outcome == "won":
    print("\nCongrats! you won the game!!")
if chapterthree.damaged == True:
    print("\nYou got 25000 credits for completing the job.")
    settings.money = settings.money + 25000
    print("[\nYou now have a balance of\033[92", settings.money, "credits.\033[97]")

if chapterthree.bonus == True:
    print("\nYou got \033[9225000 credits\033[97], and a bonus of\033[92 10000\033[97] for completing the job.")
    settings.money = settings.money + 25000 + 10000
    print("\n[You now have a balance of\033[92", settings.money, "credits.\033[97]")

# print all achievements
print("\nCheck out all the achievements you unlocked in this playthrough! \n")
print("\nAchievements Unlocked:")

# take all achievements and put it in a list to print nicely
achivementsListAgain = [achivements.bish,  achivements.sugar_daddy_failed, achivements.good_listener,
                        achivements.progambler, achivements.risk_taker, achivements.playing_it_safe,
                        achivements.pew_pew, achivements.bro_why, achivements.insert_black_hackerman_meme,
                        achivements.mop_apprentice, achivements.mop_master, achivements.your_phone]

for a in achivementsListAgain:
    if a == "":
        pass
    else:
        print("\033[93m", a, "\033[97munlocked!")

# random tip to encourage players to play again jkshfjksd
print("\nTip: Try using with different traits and choices to discover all the achievements!\n")

