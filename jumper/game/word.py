

import random
from game.words_list import word_list


class Word:
    """The random secret word. 
    
    The responsibility of the SecretWord is to get a random secret word, and keep track of the letters guessed correctly and the letters guessed incorrectly. 
    
    Attributes:
        word_normal (str): The word (randomly generated from a separate .py file list)
        word (str): Uppercase word_normal
        hidden_word (str): word replaced with "_"
        hidden_word_as_list (list): hiden word turned into a list
        missed_letters (list): list of the users missed letter guesses
        word_updated (str): hidden word updated with letters guessed correctly
        guessed (bool): booleon to show if the users letter guess was in the word or not
        you_won (bool): boolean to show if user won game by guess all letters in the hidden word
        first_guess (bool): boolean to turn off the intro message after it is displayed once. 

    """

    def __init__(self):
        """Constructs a new SecretWord

        Args:
            secret_word (str): The secret word (randomly generated from a text file.)
        """
       
        self._word_normal = random.choice(word_list)
        self._word = self._word_normal.upper()

        self._hidden_word = ("_") * len(self._word)
        self._hidden_word_as_list = list(self._hidden_word)
    
        self._missed_letters = []
        self._word_updated = "_"

        self._guessed = False
        self._you_won = False
        self._first_guess = False

    def get_first_guess(self):
        """Returns first guess boolean
        """     
        return self._first_guess
        
    def get_hidden_word(self): # Method for testing if hidden word is working correctly. Coder can print to screen to 
        """Returns hidden word as list 
        """
        return self._hidden_word_as_list

    def get_word(self): # Method to get the word. (NOT HIDDEN)
        """Returns the chosen random word. (NOT HIDDEN)
        """
        return self._word

    def get_guessed_bool(self): # Method to check if the last guess was in the word of not. True/False.
        """Returns the boolean that shown if the users guessed letter was in the word.  
        """
        return self._guessed

    def get_won_bool(self): # Method to check if the hidden word has been completly guessed. True/False.
        """ Returns the boolean that tells if user won the game or not.
        """
        return self._you_won

    def get_missed_letters(self): # Method to get missed letter list
        """Returns the missed guess letters
        """
        return self._missed_letters

    def update_hidden_word(self, guess): # Method for updating the hidden word with a user guess
        """ Updates the hidden word with correct letter guesses. Turns of the intro message by turning the first guess booleon to False.
        Updates guessed boolean to True if guess letter is in the word, to False if it is not. 
        Updates missed letters list if guess in not in the hidden word.
        If hidden word is completly guessed turns you_won booleon to True

        Args:
        
        """

        self._first_guess = True # boolean to turn off first message

        letter_locations = [i for i, letter in enumerate(self._word) if letter == guess]
        for index in letter_locations:
            self._hidden_word_as_list[index] = guess  
            self._hidden_word_as_list = self._hidden_word_as_list         
            self._word_updated = ' '.join(self._hidden_word_as_list)

        letter_locations = [i for i, letter in enumerate(self._word) if letter == "_"]
        for index in letter_locations:
            self._hidden_word_as_list[index] = guess  
            self._hidden_word_as_list = self._hidden_word_as_list         
            self._word_updated = ' '.join(self._hidden_word_as_list)


        if guess in self._word: # Check if user guess is in the word
            self._guessed = True  

        if guess not in self._word: 
            self._guessed = False
            self._missed_letters.append(guess) # Update missed letters list with user guess

        if "_" not in self._word_updated: # Test to see if word is completly guessed
            self._you_won = True # Turn winning booleon to True
                   
        return self._word_updated

           


