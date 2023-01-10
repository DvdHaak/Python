# Functie board aanmaken
def print_board_ttt(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# functie scoreboard tonen
def print_scoreboard_ttt(scoreboard_ttt):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(scoreboard_ttt.keys())
    print("\t   ", players[0], "\t    ", scoreboard_ttt[players[0]])
    print("\t   ", players[1], "\t    ", scoreboard_ttt[players[1]])
 
    print("\t--------------------------------\n")
 
# Functie kijken of iemand gewonnen heeft.
def win_check(player_pos, cur_player):
 
    # Alle mogelijke win combinaties
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop "soln" kijk voor winnende combinaties behaald.
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Geef de waarde "True" terug als er iemand gewonnen heeft.
            return True
    # Geef de waarde "False" terug als er nog niemand heeft gewonnen.       
    return False       
 
# Functie om te kijken of er gelijkspel behaald is.
def draw_check(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Functie voor een TTT(Tic Tac Toe) game
def single_game(cur_player):
 
    # Represents the TTT
    values = [' ' for x in range(9)]
     
    # Slaat de lokaties op voor X en O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop voor een TTT game.
    while True:
        print_board_ttt(values)
         
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Aanpassen game informatie.
 
        # Aanpassen grid status.
        values[move-1] = cur_player
 
        # Aanpassen player positie
        player_pos[cur_player].append(move)
 
        # functie call voor een winnnaar.
        if win_check(player_pos, cur_player):
            print_board_ttt(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        # functie call voor gelijkspel
        if draw_check(player_pos):
            print_board_ttt(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Verander player van TTT
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
    # Slaat op wie welke TTT kiest.
    cur_player = player1
    player_choice = {'X' : "", 'O' : ""}
    options = ['X', 'O']
 
    # Slaat het scoreboard op.
    scoreboard_ttt = {player1: 0, player2: 0}
    print_scoreboard_ttt(scoreboard_ttt)
 
    # Game Loop voor meerdere TTT spellen.
    # The loop loopt tot 1 van de spelers stopt. 
    while True:
 
        # Player keuze menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception voor een "CHOICE" input.
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        # Condities voor spelers keuze
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard_ttt(scoreboard_ttt)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Bewaard de uitkomst van een losse TTT game.
        winner = single_game(options[choice-1])
         
        # Aanpassen scoreboard met de winnaar.
        if winner != 'D' :
            player_won = player_choice[winner]
            scoreboard_ttt[player_won] = scoreboard_ttt[player_won] + 1
 
        print_scoreboard_ttt(scoreboard_ttt)
        # Verandert speler van TTT.
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1