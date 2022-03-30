import random
random.seed(1)

class Wordle():
    def __init__(self, attempt_allowed=5,wins=0,losses=0,total_games=0):
        self.attempt_allowed = attempt_allowed
        self.wins = wins
        self.losses = losses
        self.total_games = total_games
        
            
    def get_word(self):
        """Asks the user for a guess and then, checks if it meets the requirements. Then returns the guess."""
        word = str(input("Type in a 5 letter word: ")).lower()
        if self.check_input(word) == False:
            return self.get_word()
        else:
            return word


    def win_check(self,guess_word,correct_word):
        if guess_word == correct_word:
            print("Winner winner chicken dinner! You guessed the word!\n")
            self.wins += 1
            return True
        else:
            return False
            

    def get_random_word(self):
        """Picks a random word from the random_words.txt file"""
        with open("random_words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            return random.choice(words)
    
    def check_input(self,guess_word):
        """Takes in the input from the user and then checks if it meets the requirements for a guess"""
        if len(guess_word) != 5:
            print('Word is not 5 letters! Try again.',end='\n\n')
            return False

        allowed_letters = "abcdefghijklmnopqrstuvwxyz"
        for a in guess_word:
            if a not in allowed_letters:
                print("Word contains illegal letters! Try again.",end='\n\n')
                return False
        return True
    
    def change_guesses(self):
        """Changes the number of tries available to the user, checks if the user input is a integer and that it is not zero"""
        try:
            self.attempt_allowed = int(input('Select new number of guesses: '))
        except ValueError:
            print('Invalid input, try again.\n')
            self.change_guesses()
        if self.attempt_allowed == 0:
            print('Having 0 guesses is obviously not allowed. Try again\n')
            self.change_guesses()
        print()

    def game_print(self,guesses,guess_letter_check):
        """print function, takes in the user guesses and the hints and then prints them out in one line."""
        current = 5
        for word in guesses:
            print('\n'+word,end=' | ')
            for letter in guess_letter_check[current-5:current]:
                print(letter,end=' ')
            current += 5
        print('\n')

    
    def word_in_database(self,newword):
        """Takes in a word, checks if it is in the random_words.txt"""
        with open("random_words.txt","r") as file:
            if(newword in file. read()):
                return True
            else:
                return False
    
    def add_word_to_database(self):
        """Adds a word to the existing word libary, checks if the word meets the word req."""
        newword = self.get_word()
        in_db = self.word_in_database(newword)
        if in_db == False:
            with open("random_words.txt","a") as file:
                file.write(f"\n{newword}")
                print(f"{newword} added to Word Libary\n")
        else:
            print (f"{newword} already exist, no duplicates allowed!\n")

    def view_score(self):
        print(f'\nTotal games: {self.total_games}\nTotal wins: {self.wins}\nTotal losses: {self.losses}\n')
            

    def play_game(self):
        correct_word = self.get_random_word()
        print(correct_word)
        guess_letter_check = [] #stores the hint code.
        attempt = 0
        guesses = [] # stores the guesses made by the user.
        game_won_check = False

        while attempt < self.attempt_allowed and game_won_check == False:
            
            guess_word = self.get_word() #gets a guess from the user.

            guesses.append(guess_word) #adds the guess to a list.
             
            count = 0
            for i in guess_word: #Generates the hint
                if i == correct_word[count]: 
                    guess_letter_check.append("C") # if character in the word and at the right place.
                elif i in correct_word: 
                    guess_letter_check.append("c") #else if character anywhere in word.
                else:
                    guess_letter_check.append("-") # if letter not in word. 
                count+=1 
            self.game_print(guesses,guess_letter_check)
            game_won_check = self.win_check(guess_word,correct_word)
            attempt += 1
        if game_won_check == False:
            self.losses += 1
            print('You lost :( Correct word was...',correct_word)
        self.total_games += 1
    
    # def __str__(self,guesses,guess_letter_check):

    #     return f"{guesses} : {guess_letter_check}"


def menu():
    play = Wordle()
    selection = True
    print('Welcome to \nWORDLE\n')

    while selection != False:
        print('Select one of the following:\n1:Play game\n2:Select number of guesses\n3:View Score\n4:Add a new word\nq:Quit\n')
        selection = input('Select option: ')
        if selection == '1':
            play.play_game()
        elif selection == '2':
            play.change_guesses()
        elif selection == '3':
            play.view_score()
        elif selection == "4":
            play.add_word_to_database()
        elif selection == 'q' or 'Q':
            selection = False
        else:
            print('Wrong option, try again.')

menu()


