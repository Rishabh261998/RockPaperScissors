class Player:
    """
    This is a class for the Player, it contains all the attributes and methods required for the player.
    """
    def __init__(self):
        """
        The constructor for the Player class.
        """
        # `choice` stores the player's current hand, `score` stores the player's score till now
        self.choice = 0
        self.score = 0

    def get_choice(self):
        """
        This functions gets the input from the player for the current hand to play.

        Returns:
            choice(int): current player hand
        """
        while True:
            try:
                hand = int(input("Please enter 1 for ROCK, 2 for PAPER and 3 for SCISSORS: "))
                # Here we check if the input provided by user is valid or not
                if 1 <= hand <= 3:
                    break
                else:
                    print("The value entered is invalid. The value should be between 1 and 3")
            except ValueError:
                print("The value entered is invalid. The value can only be numeric.")

        self.choice = hand
        return self.choice

    def get_score(self):
        """This is the getter for player's current score"""
        return self.score

    def update_score(self, value):
        """Setter to update the player's score"""
        self.score = value




