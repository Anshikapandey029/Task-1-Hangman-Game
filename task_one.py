import random

word_list = ["apple", "beautiful", "potato"]
chosen_word = random.choice(word_list)

lives = 6
display = []

for i in range(len(chosen_word)):
    display += "_"

game_over = False

while not game_over:
    print("\n" + " ".join(display))
    print("Lives left:", lives)

    guessed_letter = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):                             
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in chosen_word:
        lives -= 1
        print("Wrong guess!")

        if lives == 0:
            game_over = True
            print("You Lose!")
            print("The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print(" ".join(display))
        print("🎉 You Win!")