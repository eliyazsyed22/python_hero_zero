import random
import hangman_art
import hangman_words


choosen_word = random.choice(hangman_words.word_list)
print(choosen_word)

lives = 6


display = []
word_len = len(choosen_word)
for _ in range(word_len):
    display += '_'

print(display)


end_of_game = False
while not end_of_game:
    guess = input("please guess a letter \n ").lower()
    for position in range(word_len):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you Loose")
    if "_" not in display:
        end_of_game = True
        print("you Win")

    print(hangman_art.stages[lives])