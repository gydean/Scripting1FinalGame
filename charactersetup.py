# welcome player and get basic info from them

# player variables
player_name = ""
player_gender = ""
player_pronouns = 0
player_age = 0
player_weapon = ""

# customization loop variable
customizing = True

# stop prompting character set up code after making a profile
# I ACTUALLY MIGHT NOT NEED THIS, but it will stay for now
# currently does nothing
character_done = False

# greeting
print("\033[97mWelcome to my silly interactive story!")


#######################################

# customization

while customizing == True:

    # character name
    print("Please enter your character's name! (min 2 letters, max 10 letters)")
    player_name = input()
    player_name = player_name.title()

    while len(player_name) > 10 or len(player_name) < 2:
        if len(player_name) > 10:
            print("That name is too long!")
            print("Please enter your character's name! (min 2 letters, max 10 letters)")
            player_name = input()
            player_name = player_name.title()

        if len(player_name) < 2:
            print("That name is too short!")
            print("Please enter your character's name! (min 2 letters, max 10 letters)")
            player_name = input()
            player_name = player_name.title()

    # if player tries to put a number
    if player_name.isdigit():
        while player_name.isdigit():
            print("You can't have numbers in a name!")
            print("Please enter your character's name! (5 letter limit)")
            player_name = input()
            player_name = player_name.title()


    #######################################

    # character gender
    print("What is your character's gender? Choose a number.")
    print("1. Male \n2. Female\n3. frick gender")

    gender = int(input())  # come back later and do some code in case someone types in letters instead

    # player picks invalid option
    if gender < 1 or gender > 3:
        while gender < 1 or gender > 3:
            print("Please choose one of the options!")
            print("1. Male \n2. Female\n3. frick gender")
            gender = int(input())

    # gender options
    if gender == 1:
        player_gender = "Male"
        player_pronouns = 1

    if gender == 2:
        player_gender = "Female"
        player_pronouns = 2

    if gender == 3:
        player_gender = "lol what"
        player_pronouns = 3

    #######################################

    # age for character, doesn't affect gameplay ACTUALLY MAYBE IT MIGHT LOL FLIRTING?!
    print("How old is your character? Please pick an age from 18-60.")

    age = int(input())  # come back later to code for if someone puts letters

    # player picks invalid option
    if age < 18 or age > 60:
        while age < 18 or age > 60:
            print("Please pick a age from 18-60!")
            age = int(input())

    # set input as age
    player_age = age

#######################################

    # print final results
    print("Great! Your character is all set!")
    #print("Name:", player_name.title(), "\nGender:", player_gender, "\nAge:", player_age, "\nWeapon:", player_weapon)
    print("Name:", player_name.title(), "\nGender:", player_gender, "\nAge:", player_age)

    # allow for redos
    print("Do you want to redo your customization? Y/N")
    choice = input()

# THIS CODE ISNT WORKING UGGHGGHH
    # # player inputs an int
    # if choice.isdigit():
    #     while choice.isdigit():
    #         print("That's not a valid option")
    #         print("Do you want to redo your customization? Y/N")
    #         choice = input()
    #
    # # not an int or y/n - WHY ISNT THIS WORKING *violently sobs*
    # if choice != "y" or choice != "yes" or choice != "Y" or choice != "Yes" or choice != "YES" or choice != "yES" or choice != "yeS" or choice != "yEs" or choice != "n" or choice != "N" or choice != "no" or choice != "No" or choice != "NO" or choice != "nO":
    #     while choice != "y" or choice != "yes" or choice != "Y" or choice != "Yes" or choice != "YES" or choice != "yES" or choice != "yeS" or choice != "yEs" or choice != "n" or choice != "N" or choice != "no" or choice != "No" or choice != "NO" or choice != "nO":
    #         print("Please enter either Y/N!")
    #         choice = input()

    # i should just to an else statement!?!?!?!??!!?

    # y/n input
    if choice == "y" or choice == "yes" or choice == "Y" or choice == "Yes" or choice == "YES" or choice == "yES" or choice == "yeS" or choice == "yEs":
        customizing = True
    if choice == "n" or choice == "N" or choice == "no" or choice == "No" or choice == "NO" or choice == "nO":
        customizing = False
    # else:
    #     print("Please enter either Y/N!")
    # egh this would be weird

#######################################

# start the game
# im so tired, i'll figure some dumb logic for if player doesn't choose y/n later (maybe)
print("Awesome! Are you ready to begin " + player_name.title() + "'s adventure? Y/N")

begin = input()

# yeeeeee
if begin == "y" or begin == "yes" or begin == "Y" or begin == "Yes" or begin == "YES" or begin == "yES" or begin == "yeS" or begin == "yEs":
    print("Let's go!")
    character_done = True
    # next file will run from play.py!!!!!

# nayyyyy
if begin == "n" or begin == "N" or begin == "no" or begin == "No" or begin == "NO" or begin == "nO":
    print("Uh...............okay then. Bye!")
    quit()

# COME BACK AND EDIT OUTPUT TO LOOK NICER