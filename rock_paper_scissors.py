import random
import sys

print("Enter r(rock),p(paper),s(scissors) or q(quit).")

wins = 0
losses = 0
draws = 0

def cmove():
	cm = random.randint(1,3)
	
	if cm == 1:
		cm = 'r'
	elif cm == 2:
		cm = 'p'
	elif cm == 3:
		cm = 's'	
	return cm

while True:
	print(f"{wins} wins, {losses} losses, {draws} draws.")

	um = input()

	if um == 'q':
		sys.exit()
		p = 'y'
	elif um == 'r':
		p = 'y'
	elif um == 'p':
		p = 'y'
	elif um == 's':
		p = 'y'
	else:
		print("Please enter r(rock),p(paper),s(scissors) or q(quit).")
		p = 'n'
	cm = cmove()


	if um == cm:
		r = 'Its a draw.'
	elif um == 'r' and cm == 's':
		r = 'You won.'
	elif um == 'r' and cm == 'p':
		r = 'You lost.'
	elif um == 'p' and cm == 'r':
		r = 'You won.'
	elif um == 'p' and cm == 's':
		r = 'You lost.'
	elif um == 's' and cm == 'p':
		r = 'You won.'
	elif um == 's' and cm == 'r':
		r = 'You lost.'

	if p != 'n':
		if r == 'Its a draw.':
			print(r)
			draws += 1
		elif r == 'You won.':
			print(r)
			wins += 1
		elif r == 'You lost.':
			print(r)
			losses += 1