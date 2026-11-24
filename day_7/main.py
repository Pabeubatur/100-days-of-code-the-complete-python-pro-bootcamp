import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

word_list = hangman_words.word_list

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

chosen_word = random.choice(word_list)

# we need to word printed in order to debug. But It should be commented in Deployment
# print(chosen_word)

# Print the placeholder to give a hint about the word length
placeholder = ""
word_length = len(chosen_word)
# if I only input the final value to range, It starts at 0 by default
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False

# I need this variable out of the loop in order to not get it overwritten
correct_letters = []

# To enter a while loop, we usually use a boolean variable that starts and true and should be shifted to False to exit the loop
# Controlling the loop with the checks is a Good Practice. We should avoid using continue / exit, as the uses of this are very specific
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    # I need to put this sign here before the loop starts, otherwise if the guess is correct, It would print the sign
    # although is the first time we put the letter
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        # if the letter is in the correct_letters and not in the actual guess, it should be printed to display
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    # both statements are independent. If I guessed the whole word, then the first check would be false and the second, true. If I didn't guessed, the first check will be true and the second check will be false
    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"IT WAS \"{chosen_word}\"!")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
