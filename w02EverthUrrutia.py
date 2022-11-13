import random


class Card():

    def __init__(self):

        self.suit = ''

    def get_face_value(self):
        return (random.randint(1, 13))


class Player():

    def __init__(self):

        self.score = 300

    def winner(self):

        self.score += 100

    def loser(self):

        self.score -= 75
        if self.score < 0:
            self.score = 0

    def score(self):

        return (self.score)


class Manager:

    def __init__(self, player):
        self.card = Card()
        self.card1_value = 0
        self.card2_value = 0
        self.hilo_choice = ""
        self.player = player

    def choose_hi_low(self):

        self.hilo_choice = input("Higher or Lower? [h/l] ")
        return (self.hilo_choice)

    def settle_score(self):

        if (self.card1_value < self.card2_value and self.hilo_choice == "h"):
            self.player.winner()
        elif (self.card1_value > self.card2_value and self.hilo_choice == "l"):
            self.player.winner()
        else:
            self.player.loser()

    def start_game(self):

        print("The game start, you have 300 points.")
        play_again = "y"
        while (play_again == "y"):

            self.card1_value = self.card.get_face_value()
            print(f"The card is {self.card1_value}")

            self.hilo_choice = self.choose_hi_low()

            self.card2_value = self.card.get_face_value()
            print(f"The next card was {self.card2_value}")

            self.hilo_choice = self.settle_score()
            print("Your score is: ", self.player.score())

            if (self.player.score() > 0):
                play_again = input("Play again? [y/n] ")
                print()
            else:
                play_again = "n"
                print()

        if (self.player.score() > 0):
            print("your score is {}".format(
                self.player.score()))
        else:
            print("Game Over")


def main():
    player = Player()
    dealer = Manager(player)
    dealer.start_game()


if __name__ == "__main__":
    main()
