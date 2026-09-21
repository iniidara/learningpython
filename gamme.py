import random 
toss = random.randint(0, 1) # 0 is tails, 1 is heads 
for attempt in range(2):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().strip().lower()
    if guess == 'heads':
        guess = 1
    elif guess == 'tails':
        guess = 0
    if toss == guess: 
        print('You got it!')
        break
    elif attempt == 0:
        print('Try again!')
    else:
        print('Sorry, you are out of attempts!')