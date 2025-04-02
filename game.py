import random 

print('Welcome to the Word Guessing Game!')
print('You have 10 attempts to guess the word.')
print('The word is a domestic animal that can be inside of the house like "Dog" & "Cat".')
print('Good luck!')
word_bank = ['dog', 'cat', 'bird', 'fish', 'hamster', 'rabbit', 'turtle', 'ferret', 'lizard']
word = random.choice(word_bank)
guessword = ["_"] * len(word)
attempts = 10

while attempts > 0:
    print("\nCurrent Word: " + " " .join(guessword))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessword[i] = guess
        print('Great guess!')
    else:   
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    
    if '_' not in guessword:
        print('\nCongratulations!! You guessed the word: ' + word)
        break

else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)