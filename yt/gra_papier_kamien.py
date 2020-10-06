# Gra papier kamien dwóch zawodników in english

result_first_player = 0
result_second_player = 0

options = ['rock','paper','scissors']

def choice(player_info):
    while True:
        player_choice = input(f"{player_info}! Enter your choice[rock/paper/scissors]: ")
        if player_choice.lower() in options:
            return player_choice
#------------------------------------------------------------------------------------------
def battle(first_player,second_player):
    if (first_player.lower() == second_player.lower()):
        print("Draw")
        return 0
    wynik = {
        ('rock','scissors'):1,
        ('scissors','paper'):1,
         ('paper','rock'):1
        }
    return wynik.get((first_player,second_player),-1)
#------------------------------------------------------------------------------------------

while result_first_player!=3 and result_second_player!=3:

    first_player = choice("Player 1")
    second_player = choice("Player 2")
    result = battle(first_player,second_player)
    if result == 1:
        print("Player 1 won round")
        result_first_player +=1
    elif result == -1:
        print("Player 2 won round")
        result_second_player +=1

if result_first_player > 2:
    print("Player 1 won game")
else:
    print("Player 2 won game")




