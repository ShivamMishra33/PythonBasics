import random

print('H A N G M A N')
user_status = input('Type "play" to play the game, "exit" to quit:')
while user_status == 'play':
    com_choice = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
    hidden_word = list('-' * len(com_choice))
    count = 0
    guessed_letter_list = []
    while count < 8:
        print()
        print(''.join(hidden_word))
        guessed_letter = input('Input a letter: ')
        if len(guessed_letter) != 1:
            print('You should input a single letter')
        elif not guessed_letter.islower():
            print('It is not an ASCII lowercase letter')
        elif guessed_letter in hidden_word or guessed_letter in guessed_letter_list:
            print('You already typed this letter')
        elif guessed_letter in com_choice:
            for i in range(len(com_choice)):
                if com_choice[i] == guessed_letter:
                    hidden_word[i] = guessed_letter
            if com_choice == hidden_word:
                print(f'You guessed the word!{"".join(hidden_word)}')
                print('You survived!')
                break
        else:
            guessed_letter_list.append(guessed_letter)
            print('No such letter in the word')
            count += 1

    if count == 8 and hidden_word != com_choice:
        print('You are hanged!')
    user_status = input('Type "play" to play the game, "exit" to quit:')
    if user_status == 'exit':
        break
