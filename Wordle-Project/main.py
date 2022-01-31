import random
from os import system
import time
from collections import defaultdict
#\033[1;33;40m] Yellow colour
#\033[1;32;40m Bright Green colour
#\033[1;31;40m Red Colour
class wordlegame():
    #function acts as the starting point and explains the rules   
    def start(self):
        #print the rules of the game
        print(f"Rules:\n1) You get a maximum of 6 guesses at the word.\n")
        print("2) if the letter is in the word but not in the correct position then it will turn " + "\033[1;33;40m Yellow \033[1;37;40m \n")
        print("3) if the letter is in the word and in the correct position it will turn " + "\033[1;32;40m Bright Green \033[1;37;40m\n")
        print("4) if the letter is not in the word the colour will not change")
        self.game()
        return

    #function sets the user chosen settings
    def settings(self):
        input1_whileloop = True
        setting_repeat_word = False
        while(input1_whileloop == True):
            print(f"Repeat words is currently turned off.\nWould you like repeat words on? type" + "\033[1;32;40m y \033[1;37;40m" + "for yes or" + "\033[1;31;40m n \033[1;37;40m" + "for no")
            input_switch_repeatword = input()
            if (input_switch_repeatword == "y"):
                input1_whileloop = False
                setting_repeat_word = True
                print("\nSettings has been updated")
            elif (input_switch_repeatword == "n"):
                input1_whileloop = False
                setting_repeat_word = False
                print("\nSettings has been updated")
            else:
                print(f"\n\nYour input: '{input_switch_repeatword}' does not = 'y' or 'n'\nPlease try again.")

        return(setting_repeat_word)
    #function returns a random word for the game
    def getword(self, setting_repeat_word):
        #random num gen
        r_num_word_get = random.randrange(0,100)
        #opens words.txt and old_words.txt files
        file_words = open("words.txt")
        word_list = []
        #for loop to append each line in words.txt to the list word_list[]
        for line in file_words:
            word_list.append(line)

        if(setting_repeat_word == False):
            file_old_words = open("old_words.txt", "a+")
            used_words = []
            #for loop to set used_words list as contents of old_words.txt
            #skips the first line of the file as its a header
            lines_old_wordfile = file_old_words.readlines()[1:]
            for line in lines_old_wordfile:
                used_words.append(line)

            #checks if the word has been used before or not
            Check_new_word = True
            while(Check_new_word == True):
                #if word used before repeate loop to get a new word
                if r_num_word_get in used_words:
                    Check_new_word = True
                #else exit loop with the new word
                else:
                    used_words.append(r_num_word_get)
                    string_rnum_wordget = str(r_num_word_get)
                    file_old_words.write("\n" + string_rnum_wordget)
                    Check_new_word = False
            file_old_words.close()
        #sets the word to guess as a random word from word_list[]
        word_toguess = word_list[r_num_word_get]
        file_words.close()
        #returns the variable for the new word to use in the game. 
        return(word_toguess)
    #function colours the letters
    def colour_letters(self, hidden_word, Guessed_word):
        count_1 = 0
        letter_colour_list = [0, 0, 0, 0, 0]
        while (count_1 < 5):
            if Guessed_word[count_1] in hidden_word:
                letter_colour_list[count_1] = "\033[1;33;40m"
            if Guessed_word[count_1] == hidden_word[count_1]:
                letter_colour_list[count_1] = "\033[1;32;40m"
            if Guessed_word[count_1] not in hidden_word:
                letter_colour_list[count_1] = "\033[1;30;40m"
            count_1 = count_1 + 1
        return letter_colour_list

    #simply puts the colour order and the guess into a single string
    def concatinate_colour_Guess(self, colour, guess):
        concatinated_colour_guess = ""
        for i in range(0, 5):
            concatinated_colour_guess = concatinated_colour_guess + colour[i] + guess[i]
        concatinated_colour_guess = concatinated_colour_guess + "\033[1;37;40m"
        return concatinated_colour_guess
    #function contains the game itself       


    def game(self):
        setting_1 = self.settings()
        Hidden_word_whole = self.getword(setting_1)
        Hidden_word_whole = Hidden_word_whole[:-1] #this deletes the \n at the end of the word
        Hidden_word_split = []
        for char in Hidden_word_whole:
            Hidden_word_split.append(char)
        time.sleep(3)
        system('cls')
        print(f"Welcome to the game\n")
        round_counter = 0
        Game_W_L = False
        Finalised_Guess_List = []
        while (round_counter != 6) and (Game_W_L == False):
            system('cls')
            if round_counter != 0:
                print("Game Board:")
                for i in range(0, len(Finalised_Guess_List)):
                    print(f"Guess {i+1}: {Finalised_Guess_List[i]}")
            Guesses_list = []
            input_check = True
            #makes sure user entered a 5 letter word
            while(input_check == True):
                print("What is your guess?: (5 letter word)")
                #print(f"for testing: {Hidden_word_whole}")
                user_guess = input()
                if (len(user_guess)!= 5):
                    print("not 5 letters try again...")
                    time.sleep(3)
                    system('cls')
                else:
                    input_check = False
            #this stuff applys the colouring
            for char in user_guess:
                Guesses_list.append(char)
            colour_order = self.colour_letters(Hidden_word_split, Guesses_list)
            concatinated_colour_guess = self.concatinate_colour_Guess(colour_order, Guesses_list)
            #updates final guess list with coloured word
            Finalised_Guess_List.append(concatinated_colour_guess)

            #win or loss logic stuff 
            if (user_guess == Hidden_word_whole):
                Game_W_L = True #says they won the game
            else:
                round_counter = round_counter + 1
        if(Game_W_L == True):#if the user won
            system('cls')
            print("Game Board:")
            for i in range(0, len(Finalised_Guess_List)):
                print(f"Guess {i+1}: {Finalised_Guess_List[i]}")
            print(f"\nCongrats you won, the answer was: {Hidden_word_whole}, well done! :)")
        else:#if user lost
            system('cls')
            print("Game Board:")
            for i in range(0, len(Finalised_Guess_List)):
                print(f"Guess {i+1}: {Finalised_Guess_List[i]}")
            print(f"\nSorry you have lost the game :(\nThe answer was: {Hidden_word_whole}")
        return

#instance of Class wordlegame
object = wordlegame()
#calls main function
object.start()
print ("\nend of game")