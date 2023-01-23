class RockPaperScissors:
    """
    This class stores all the required attributes for the RockPaperScissors match played between player and computer
    """
    def __init__(self):
        """
        The constructor for the RockPaperScissors class.
        """
        # `player_score` and `computer_score` stores the player's and computer's current score
        # `playing` stores the value if the player wants to continue playing or not
        self.player_score = 0
        self.computer_score = 0
        self.playing = True

    def get_match_winner(self):
        """This function checks and prints the winner"""
        if self.player_score == self.computer_score:
            print("Match ended in a Tie!")
        elif self.player_score > self.computer_score:
            print("Player won the Match!")
        else:
            print("Computer won the Match!")

    def get_game_winner(self, player_choice, computer_choice):
        """
        This functions uses the current player and computer choice to print and return the winner.

        Parameters:
            player_choice (int): The current choice of the player
            computer_choice (int): The current choice of the computer

        Returns:
            winner(int): value to store a tie, player won or computer won
        """
        if player_choice and computer_choice:
            if player_choice == computer_choice:
                print("The game ended in a Tie!")
                return 0
            elif (player_choice - computer_choice) % 3 == 1:
                print("Player Won!")
                self.player_score += 1
                return 1
            else:
                print("Computer Won!")
                self.computer_score += 1
                return -1
        else:
            return -2

    def update_playing(self, value):
        """Setter for the parameter playing"""
        if value == 2:
            self.playing = False
        else:
            self.playing = True

    def get_playing(self):
        """Getter for parameter playing"""
        while True:
            try:
                self.playing = int(input("Enter 1 to continue playing, 2 to end: "))
                if self.playing not in [1, 2]:
                    print("The value should be either 1 or 2")
                else:
                    break
            except ValueError:
                print("The value entered is invalid. The value should be a numeric value.")
        return self.playing
