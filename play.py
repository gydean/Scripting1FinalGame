# ONE FILE TO PLAY THEM ALL *insert some lotr music idk*
# im a neat freak
# anyway!! just click play to run the game!!!
# it will execute all the game files in order and then finally print out game results if desired

##########################################
# basic imports

import datetime
import charactersetup
import settings


##########################################
# start actual story

import prologue

print(settings.branch_one)
if settings.branch_one == 1:
    import chapterone
    import chaptertwo
if settings.branch_one == 2:
    import chaptertwo

import chapterthree
import epilogue

##########################################

# make a nice list of strings to print out achievements
export_list = []
for a in epilogue.achivementsListAgain:
    if a == "":
        pass
    else:
        export_list.append("\t" + a + "\n")

# ask if player wants to save game details
save_game = input("\nWould you like to save a text file of your game stats and achievements? Please pick Y/N.\n")
print_it = False

if save_game == "y" or save_game == "yes" or save_game == "Y" or save_game == "Yes" or save_game == "YES" or save_game == "yES" or save_game == "yeS" or save_game == "yEs":
    print_it = True
if save_game == "n" or save_game == "N" or save_game == "no" or save_game == "No" or save_game == "NO" or save_game == "nO":
    print_it = False


# making save file
if print_it == True:
    save_file_name = input("Please name your file: ")
    save_file = save_file_name + '.txt'
    name = str(input("Please enter your first name: "))

    # writing everything to savefile
    with open(save_file, 'w') as file_object:
        file_object.write("Date: " + str(datetime.date.today()))
        file_object.write("\nPlayer: " + name)
        file_object.write("\nStatus: " + chapterthree.outcome)
        file_object.write("\n----------------------------------------")
        file_object.write("\nCharacter:")
        file_object.write("\n\tName: " + charactersetup.player_name)
        file_object.write("\n\tGender: " + charactersetup.player_gender)
        file_object.write("\n\tAge: " + str(charactersetup.player_age))
        file_object.write("\n\tWeapon: " + chaptertwo.player_weapon)
        file_object.write("\n\tTool: " + chaptertwo.player_tool)
        file_object.write("\n\tHealth: " + str(settings.health))
        file_object.write("\n\tMoney: " + str(settings.money))
        file_object.write("\n----------------------------------------")
        file_object.write("\nAchievements:\n")
        file_object.writelines(export_list)

# goodbye!
else:
    print("Thanks for playing!")
    exit()
