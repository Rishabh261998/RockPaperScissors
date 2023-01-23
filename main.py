from Computer import *
from Player import *
from Hand import *
from RockPaperScissors import *


def main():
    """This function implements the high level design of the rock, paper, scissors game"""
    rock_paper_scissors = RockPaperScissors()
    player = Player()
    computer = Computer()
    # while loop for continue playing the game until the player wants to stop
    while rock_paper_scissors.playing:
        player_choice = player.get_choice()
        computer_choice = computer.get_choice()
        # Here we print the player and computer current hand
        print(f"The player chose {Hand(player_choice).name}")
        print(f"The computer chose {Hand(computer_choice).name}")
        _ = rock_paper_scissors.get_game_winner(player_choice, computer_choice)
        player.update_score(rock_paper_scissors.player_score)
        computer.update_score(rock_paper_scissors.computer_score)
        # Here we print the player and computer current score
        print(f"The current score of Player is {player.get_score()}")
        print(f"The current score of Computer is {computer.get_score()}")
        is_playing = rock_paper_scissors.get_playing()
        rock_paper_scissors.update_playing(is_playing)
    # output the winner after all the games
    rock_paper_scissors.get_match_winner()


if __name__ == '__main__':
    main()
