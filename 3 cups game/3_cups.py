from random import shuffle

#Function to shuffle the list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#Takes user input as guess
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2")

    return int(guess)

#Checks if the user's guess is correct (matches the position of O)
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print("Wrong guess!")
        print(mylist)

#INITIAL LIST
mylist = [' ','O',' ']

#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)

