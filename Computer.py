from random import randint


class Computer:
    """
    This is a class for the Computer, it contains all the attributes and methods required for the computer.
    """
    def __init__(self):
        """
        The constructor for the Computer class.
        """
        # `choice` stores the computer's current hand, `score` stores the computer's score till now
        self.choice = 0
        self.score = 0

    def get_choice(self):
        """
        This functions gets the hand for the computer to play.

        Returns:
            choice(int): current computer hand
        """
        self.choice = randint(1, 3)
        return self.choice

    def get_score(self):
        """This is the getter for computer's current score"""
        return self.score

    def update_score(self, value):
        """Setter to update the computer's score"""
        self.score = value
