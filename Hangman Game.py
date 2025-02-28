import random
import stages

word_list = ["apple" , "cherry" ]
chosen_word = random.choice(word_list)
print(chosen_word)

hint = []
for i in chosen_word:
    hint +="_"
print(hint)

lives = 6
game_over = False
while not game_over:
    Guess =input("Enter a letter : ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==Guess:
            hint[position]=Guess
    print(hint)

    if Guess not in chosen_word :
        lives-=1   
        if lives ==0:
            print("You Lose!!")
            game_over=True

    if "_" not in hint:
        print("Congragulations , You Won !!")
        print(stages.HANGMAN_PICS[lives])      
        game_over=True 