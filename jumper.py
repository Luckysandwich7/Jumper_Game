
import random


class Director:
    """
    This is the class header
    """
    #holds all the defs and directs the game
    def __init__(self):
        
        return
    def start_game(self):
        blanks = WordBlanks()
        generator = UnknownWordGenerator()
        stick_figure = Parachute()
        while stick_figure.parachute_life() == True and blanks.checker() == False:
            blanks.print_blanks()
            stick_figure.print_parachute()
            if blanks.guess_letter(generator.get_unknown_word()) == False:
                stick_figure.cut_chute()
        blanks.print_blanks()
        stick_figure.print_parachute()


class WordBlanks:
    """
    This class displays the word blanks and calls for the random 5 letter word
    """

    def __init__(self):
        self.blankString = list("_ _ _ _ _")
    #def for a guess, take input from Director.
    def guess_letter(self, unknown_word):
        guess = input("Guess a letter (a/z): ")
        if guess in unknown_word:
            index = 0
            for letter in unknown_word:
                if letter == guess:
                    self.blankString [index *2] = guess
                index += 1
            return True
        return False

    def checker(self):
        if "_" in self.blankString:
            return False
        else:
            return True
""
test
""

    def print_blanks(self):
        print("".join(self.blankString))
        print("")
    #returns inputs

class Parachute:
    """
    This class displays the parachute and controls the life points the parachute has.
    """

    def __init__(self):
        self.parachute = [' ___', '/   \\', ' ———', '\\    /', ' \\  / ', '  0', '/ | \\', ' / \\', " ", "^^^^^^^^^^^^^"]

    def cut_chute(self):
        self.parachute.pop(0)
        if self.parachute_life() == False:
            self.parachute[0] = '  X'
    
    def print_parachute(self):
        for line in self.parachute:
            print(line)

    def parachute_life(self):
        if len(self.parachute) > 5:
            return True
        else:
            return False

class UnknownWordGenerator:
    """
    This class pulls a random word from the word bank and returns it for use throughout the code
    """
    def __init__(self):
        bank = ['areas', 'pizza', 'trees']
        self.unknown_word = bank[random.randint(0, 2)]
    def get_unknown_word(self):
        return self.unknown_word


def main():
    game = Director()
    game.start_game()

if __name__ == "__main__":
    main()
        

    

#Class needs atributes(variables) and methods (functions)
