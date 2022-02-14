'''from itertools import count'''


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
    while player_num >= 0:
        life.append(life_count)
        player_num += -1
    return(life)
    
def player_names(player_num):    
        players = []
        players = input("What is the first player's name? ")
        players = input("What is the second player's name? ")
        if player_num >= 3:
            players = input("What is the third player's name? ")
        if player_num >= 4:
            players = input("What is the fourth player's name? ")
        if player_num >= 5:
            players = input("What is the fith player's name? ")
        if player_num == 6:
            players += input("What is the sixth player's name? ")
            return(players)

def life_change(player, life):
    advance = False
    while advance == False:
        life_change = input("How much would you like your life to change ( to lose life add a -)")
        try:
           life_change = int(life_change)
        except TypeError:
            print("That isn't an integer Try again")
            continue
        advance = True
    life += life_change
    print(f'{player} now has {str(life)} life')
    return(life)
    