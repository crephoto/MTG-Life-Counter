
# This gets the number of players 
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
        players.append(input("What is the first player's name? "))
        players.append(input("What is the second player's name? "))
        if player_num >= 3:
            players.append(input("What is the third player's name? "))
        if player_num >= 4:
            players.append(input("What is the fourth player's name? "))
        if player_num >= 5:
            players.append(input("What is the fith player's name? "))
        if player_num == 6:
            players.append(input("What is the sixth player's name? "))
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
    print(f'{player} now has {str(life)} life')
    return(life)

# This will allow a user to activate other functions
def request_query(players, Life):
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
        player_index = input(f'Whose life should be changed {players}? ')
        player_index = players.index(player_index)
        life_change(players[player_index], Life[player_index])

# This will effectivley roll n, n sided dice or flip n coins  
def dice_roll():
    pass

# This will format a list to look like a string when printed
def list_formating(list):
    pass
