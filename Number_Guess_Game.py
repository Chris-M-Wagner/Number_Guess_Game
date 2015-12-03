"""
Creator: Chris Wagner
Created Date: 12/03/2015
Last Updated: 12/03/2015

Summary: 
    Number_Guess_Game generates a random integer and asks the user to guess it. 
"""
import random

def Number_Guess_Game():

	LL = 1 #Lower limit
	UL = 10 #Upper limit
	guessUL = 3 #Guess upper limit
	guess = 0
	tries = 0

	ans = random.randrange(LL,UL+1) #This will be the mystery number

	print "\n\n\nWelcome to the Guessing Game! I will think of a mystery number between %s and %s, and you will have %s guesses to find the number!" %(LL, UL, guessUL)

	while tries<guessUL and guess!=ans:
		guessguesses = "guesses"
		if (guessUL - tries) == 1:
			guessguesses = "guess"
		print "\nYou have %s %s left" %((guessUL - tries), guessguesses)

		try:
			guess = int(raw_input("Enter a number: "))
			print ""
		except ValueError:
			print "You have entered an incorrect value. Please input a positive integer."

		if guess>UL or guess<LL:
			print "The mystery number is between %s and %s, try guessing between those numbers!" %(LL, UL)

		if guess!=ans and guess<=UL and guess>=LL:
			tries+=1

			if (guessUL-tries)>0:
				hilow = ""

				if guess > ans:
					hilow = "lower"
				elif guess < ans:
					hilow = "higher"

				print "The mystery number is %s than %s" %(hilow, guess)

	if guess==ans:
		print "You win! The mystery number is %s" %(ans)
	elif guess!=ans and tries==guessUL:
		print "Sorry, the mystery number was %s" %(ans)

	replay = raw_input("Play again? \n(Y/N): ")
	if replay == "Y":
		Number_Guess_Game()
	else:
		print "Exiting Game."
		return None

Number_Guess_Game()

'''
Testing Methodology:
- Guess a string
- Guess an integer outside of the LL/UL range 
- Guess number that is false to review guess iteration
- Guess the mystery number, make sure that the win message comes up
- Test the replay Y/N
'''