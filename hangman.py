from getpass import getpass

class Game:
    def __init__(self):
        self.lives = 8
        self.letters_left = "abcdefghijklmnopqrstuvwxyz"

    def generate_word(self):
        self.target_word = getpass("Player 1: Please enter a word: ")
        self.current_word = "_" * len(self.target_word)

    def check_word(self, letter):
        if len(letter) != 1:
            print("Please enter a single letter.")
            return
        elif letter not in self.letters_left:
            print("You already guessed this letter. Please guess a different letter")
            return
        else:
            self.letters_left = self.letters_left.replace(letter, "")

        if letter in self.target_word:
            print("You guessed correctly! Letter {} is in the word.".format(letter))
            indices = [pos for pos, char in enumerate(self.target_word) if char == letter]
            for i in indices:
                self.current_word = self.current_word[:i] + letter + self.current_word[i+1:]
            print("Letters left: {}".format(self.letters_left))
            print(self.current_word)
        else:
            print("Letter {} is not in the word.".format(letter))
            print("Letters left: {}".format(self.letters_left))
            print(self.current_word)
            self.lives -= 1
            if self.lives == 0:
                print("You lost! The word was {}.".format(self.target_word))
            else:
                print("You have {} lives left.".format(self.lives))

    def check_win(self):
        if self.current_word == self.target_word:
            print("You won! The word was {}.".format(self.target_word))
            return True
        else:
            return False
def main():
    game = Game()
    game.generate_word()
    print("Game is initialized. You have 8 lives. There are {} letters in the word.".format(len(game.target_word)))
    print(game.current_word)
    while game.lives > 0:
        if game.check_win():
            break
        letter = input("\nPlayer 2: Please enter a letter: ")
        game.check_word(letter)

main()

