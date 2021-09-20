import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')

logging.info('Start of program')
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# the original code stored numbers in the toss variable but asked user to enter a string, heads or tails,
# and therefore it was not possible to get a match
random_number = random.randint(0, 1)  # 0 is tails, 1 is heads
if random_number == 0:
    toss = "tails"
else:
    toss = "heads"

logging.debug('Toss is %s', toss)
logging.debug('Guess is %s', guess)

if toss == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    logging.debug('Toss is %s', toss)
    logging.debug('Guess is %s', guess)
    guess = input()
    # the input here wass loaded into a new variable "guesss" which remained unused,
    # leaving the program to work with the original input in "guess"

    if toss == guess:
        print('You got it!')
        logging.debug('Toss is %s', toss)
        logging.debug('Guess is %s', guess)

    else:
        print('Nope. You are really bad at this game.')
        logging.debug('Toss is %s', toss)
        logging.debug('Guess is %s', guess)

logging.debug('End of program')
