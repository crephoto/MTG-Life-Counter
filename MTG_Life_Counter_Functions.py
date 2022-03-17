
# This gets the number of players 
from numpy import true_divide


def startup():
    players = 0
    while players<2 or players>6:
        players = input("How many people are playing (max6) ")
        try:
            players = int(players)
        except ValueError:
            print("That isn't an Integer, Try again")
            players = 0
            continue
        if players>6 or players<2:
            print("Too many or too little players, Try again")
    return(players)

# This takes the number of players and returns a list with starting life, this will correspond to a player in the Players list
def setup(player_num):
    advance = False
    life = []
    while advance == False:
        life_count = input("How much life should everyone start with? ")
        try:
            life_count = int(life_count)
        except ValueError:
            print("That isn't a whole number, Try again")
            continue
        if life_count < 0:
            print("That isn't a whole number, Try again")
            continue
        advance = True
    while player_num > 0:
        life.append(life_count)
        player_num += -1
    return(life)

# This returns a list of player names, the names will correspond to a life total in the Life list    
def player_names(player_num):    
        players = []
        for i in player_num:
            players.append(input(f'What is the name of player {i}? '))
        return(players)

# This takes a player's life and changes it by a user-determined ammount
def life_change(player, life):
    advance = False
    while advance == False:
        life_change = input("How much would you like your life to change ( to lose life add a -) ")
        try:
           life_change = int(life_change)
        except TypeError:
            print("That isn't an integer Try again")
            continue
        advance = True
    life += life_change
    if life <= 0:
        print(f'{player} has died')
    else:
        print(f'{lf(player, False, 0)} now has {lf(str(life, False, 0))} life')
    return(life)

# This will allow a user to activate other functions
def request_query(players, Life, player_num):
    advance = False
    print("What would you like to do?")
    while advance == False:
        action = input("type 1 for add/reduce life, 2 to roll a dice or flip a coin, 3 to change commander dammage ")
        action = int(action)
        if action!=1 and action!=2 and action!=3:
            print("That isn't a 1, 2, or 3, Try Again")
        else:
            advance = True
    if action == 1:
        player_index = input(f'Whose life should be changed? {lf(players)} ')
        player_index = players.index(player_index)
        Life[player_index] = life_change(players[player_index], Life[player_index])
    if action == 2:
        dice_roll()
    if action == 3:
        commander_dmg([], player_num)

# This will effectivley roll n, n sided dice or flip n coins  
def dice_roll():
    import random
    advance = False
    heads = 0
    HoT = ["Heads", "Tails"]
    side_list = []
    flipping = True
    while advance == False:
        sides = input("How many sides should there be? (2 for coinflip, 1 for consecutive coinflip) ")
        try:
            sides = int(sides)
        except ValueError:
            print("That wasn't a number, Try Again")
            continue
        advance = True
    if sides == 1:
        while flipping == True:
            end = random.choice(HoT)
            if end == "Tails":
                flipping = False
            else:
                heads += 1
        print(f'It landed on Heads {str(heads)} times')
    if sides==2:
        print("It landed on " + random.choice(HoT))
    if sides > 2:
        for i in range(sides):
            side_list.append(i) 
        print("it rolled a " + str(random.choice(side_list) + 1))

# This will format a list to look like a string when printed
def lf(list, cd, player_num):
    if cd == True:
        list = str(list).replace("[", "", 1)
        list = list.replace("]", "}", player_num)
        list = list.replace("]", "")
        list = list.replace("}", "]")
    else:
        list = str(list).replace("[", "")
        list = list.replace("]", "")
        list = list.replace("'", "")
    return(list)

def commander_dmg(dammage, player_num):
    advance = False
    while advance == False:
        decide = input("Type 1 to change commander dammage, type 2 to view current commander dammage ")
        if decide!="1" and decide!="2":
            print("That wasn't a 1 or 2 try again")
        else:
            advance = True
    if decide == "1":
        if dammage == []:
            dammage = [[0]*player_num-1]*player_num
            print(lf(dammage, True, player_num))

            


            

