def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print ('Correct answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry worng answer. Try again. ')
            attempt  = attempt + 1


        if attempt  == 3:
         print(' The correct answer is ' + answer)


score = 0
print('Guess the Animal')
guess1 = input('Whitch animal lives at the north pole?')
check_guess(guess1, 'polar bear')
guess2 = input('Whitch is the fastest land animal?')
check_guess(guess2, 'cheetah')
guess3 = input('Whitch is the largest animal on earth')
check_guess(guess3, 'blue whale')

print('Your score is ' + str(score))
