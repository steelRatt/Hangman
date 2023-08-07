import random
import hangman_art
import hangman_words

#Main variables
chosen_word = hangman_words.word_list[random.randint(0, len(hangman_words.word_list))-1]
final_word = []
lives = 0

#Function to check if the guessed letter is one of the letters in the chosen word
def guessCheck(guess, chosen_word):
    for i in chosen_word:
        if i == guess:
            return True
    return False

#Function to check if all letters have been guessed, if so, you win!
def isOver(final_word):
    if "_" not in final_word:
        return True
    else:
        return False

#Make each letter of the word in the list hidden for the start of the game
for i in chosen_word:
    final_word.append("_")

print(f"{hangman_art.logo}\n\nThe word has been chosen!\n")

#While loop that keeps the game going until you run out of lives
while lives != 6 and not isOver(final_word):
    print(f"{final_word}\n")
    guess = input("Enter your guess: ").lower()

    #If guess is correct, unhide the correctly guessed letters
    if guessCheck(guess, chosen_word):
        print(f"Correct!\n{hangman_art.stages[lives]}\n")

        for j in range(0, len(chosen_word)):
            if chosen_word[j] == guess:
                final_word[j] = guess.upper()
    else:
        lives += 1
        print(f"Wrong!\n{hangman_art.stages[lives]}\n")

#If at this line, the while loop must be broken. Check if the game is won or lost and act accordingly
if isOver(final_word):
    print(f"{final_word}\n\nYou win! You correctly guessed the word!\n")
else:
    #Once the user has ran out of lives, game over!
    print(f"Game over! The word was: {chosen_word.upper()}. Try again next time.")