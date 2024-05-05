# Dice game 
import random
# Iniziation of dice 
dice_faces_1 = (1,2,3,4,5,6)
dice_faces_2 = (1,2,3,4,5,6)
dice_faces_3 = (1,2,3,4,5,6)

with open("dice_results.txt", mode = "w") as output_connection: 
    output_connection.write(f'Tuple Out Dice Game') 


#players input their name 
player_1 = input("what is your name player 1 ?\n")
player_2 = input("what is your name player 2 ?\n")


results_player = {player_1:0, player_2:0}