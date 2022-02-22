import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _blanks: dashed line for the blank word.
        generator: random selector of a word from the given list.
        stick_figure: draws the parachute
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._blanks = WordBlanks()
        self._generator = UnknownWordGenerator()
        self._stick_figure = Parachute()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._stick_figure.parachute_life() == True and self._blanks.checker() == False:
            self._blanks.print_blanks()
            self._stick_figure.print_parachute()
            if self._blanks.guess_letter(self._generator.get_unknown_word()) == False:
                self._stick_figure.cut_chute()
        self._blanks.print_blanks()
        self._stick_figure.print_parachute()

class WordBlanks:
    """A dashed line drawing of the word to guess.

    The responsibility of WordBlanks is to keep track of the correct letters when guessing the word.
   
    Attributes:
        blankString (string): The dashes of letters on the word.
    """

    def __init__(self):
        """Constructs a new instance of WordBlanks.

        Args:
            self (blankString): An instance of WordBlanks.
        """
        self._blankString = list("_ _ _ _ _")

    def guess_letter(self, unknown_word):
        """Requires input from jumper to guess letter of the random word.

        Args:
            self (WordBlanks): An instance of WordBlanks.
        """
        guess = input("Guess a letter (a/z): ")
        if guess in unknown_word:
            index = 0
            for letter in unknown_word:
                if letter == guess:
                    self._blankString [index *2] = guess
                index += 1
            return True
        return False

    def checker(self):
        """Check input from jumper against the random word.

        Args:
            self (WordBlanks): An instance of WordBlanks.
        """
        if "_" in self._blankString:
            return False
        else:
            return True

    def print_blanks(self):
        """Prints the letter from jumper if correct, otherwise prints none.

        Args:
            self (WordBlanks): An instance of WordBlanks.
        """
        print("".join(self._blankString))
        print("")
    
class Parachute:
    """A sketch drawing of the parachute and the jumper.

    The responsibility of Parachute is to keep track of the number of lines the jumper has left when guessing the word.
   
    Attributes:
        parachute (string): The number of lines on the parachute
    """

    def __init__(self):
        """Constructs a new instance of Parachute.

        Args:
            self (parachute): An instance of Parachute.
        """
        self._parachute = [' ___', '/   \\', ' ———', '\\   /', ' \\ / ', '  0', '/ | \\', ' / \\', " ", "^^^^^^^^^^^^^"]

    def cut_chute(self):
        """Cuts a line on the parachute if the guess is not correct, kills the jumper if no parachute is left

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._parachute.pop(0)
        if self.parachute_life() == False:
            self._parachute[0] = '  X'
    
    def print_parachute(self):
        """Displays the number of lines left on the parachute

        Args:
            self (Parachute): An instance of Parachute.
        """
        for line in self._parachute:
            print(line)

    def parachute_life(self):
        """Life of the parachute for words, in this case, five letters in length. If more than five guesses are made, there will be no more life.

        Args:
            self (Parachute): An instance of Parachute.
        """
        if len(self._parachute) > 5:
            return True
        else:
            return False

class UnknownWordGenerator:
    """A generator to randomly select a word from the a list.

    The responsibility of UnknownWordGenerator is to generate a random word for the jumper ot guess.
   
    Attributes:
        unknown_word (string): A randomly selected word.
    """
    def __init__(self):
        """Constructs a new instance of UnknownWordGenerator.

        Args:
            self (unknown_word): An instance of UnknownWordGenerator.
        """
        bank = ['areas', 'pizza', 'trees','jazzy','adore']
        self._unknown_word = bank[random.randint(0, 4)]

    def get_unknown_word(self):
        """Generates random word.

        Args:
            self (UnknownWordGenerator): An instance of UnknownWordGenerator.
        """
        return self._unknown_word

def main():
    """This is the game entry point.
    An instance of the Director class is created and assigned to a variable called game. 
    The next line of code invokes the start game method. 
    """
    game = Director()
    game.start_game()

if __name__ == "__main__":
    main() 
