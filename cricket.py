import random

class player:
	first_batting_total_runs = 0
	run_list = [0,1,2,3,4,5,6]
	out = False

	def batting(self,opponent,first_batting_total_runs,user_name,opponent_name,batting_order):
		self.name = user_name
		opponent.name = opponent_name
		self.total_runs = 0
		batsman_run = 0
		win = False 
		if batting_order == 2:
			print("{} needs to defend {} runs to win".format(opponent.name,first_batting_total_runs))
			print("{} needs to take {} runs to win".format(self.name,first_batting_total_runs+1))
		while self.out == False:
			try:
				print("Enter run")
				batsman_run = int(input())
			except ValueError:
				print("Enter a number")
				continue
			if batsman_run < 0 or batsman_run > 6:
				print("Invalid input\nEnter runs between 0 and 6")
				continue
			bowler_bowl = random.choice(self.run_list)
			print("opponent puts ", bowler_bowl)
			if batsman_run == bowler_bowl:
				print("{} and {} put same number".format(self.name,opponent.name))
				print("You are out")
				print("Your total runs is {}".format(self.total_runs))
				if batting_order == 2:
					if self.total_runs < first_batting_total_runs:
						print("{} wins".format(opponent.name))
					elif self.total_runs == first_batting_total_runs:
						print("Match tied")
					else:
						print("{} wins".format(self.name))
				break
			elif batsman_run == 0:
				self.total_runs = self.total_runs + bowler_bowl
				print("total runs of {} is {}".format(self.name,self.total_runs))
			else:
				self.total_runs = self.total_runs + batsman_run
				print("total runs of {} is {}".format(self.name,self.total_runs))
				if batting_order == 2:
					if self.total_runs > first_batting_total_runs:
						print("{} wins".format(self.name))
						win = True
			if win == True:
				break
		if batting_order == 1:
			first_batting_total_runs = self.total_runs
			user_name = self.name
			opponent_name = opponent.name
			user.bowling(comp,first_batting_total_runs,user_name,opponent_name,2)


	def bowling(self,opponent,first_batting_total_runs,user_name,opponent_name,batting_order):
		self.name = user_name
		opponent.name = opponent_name
		opponent.batting_order = batting_order
		opponent.total_runs = 0
		win = False
		if opponent.batting_order == 2:
			print("{} needs to defend {} runs to win".format(self.name,first_batting_total_runs))
			print("{} needs to take {} runs to win".format(opponent.name,first_batting_total_runs+1))
		while self.out == False:
			try:
				print("Enter run")
				bowler_bowl = int(input())
			except ValueError:
				print("Enter a number")
				continue
			if bowler_bowl < 0 or bowler_bowl > 6:
				print("Invalid input\nEnter runs between 0 and 6")
				continue
			batsman_run = random.choice(opponent.run_list)
			print("{} score {}".format(opponent.name,batsman_run))
			if bowler_bowl == batsman_run:
				print("{} and {} put same number".format(opponent.name,self.name))
				print("{} is out".format(opponent.name))
				print("total runs of {} is {}".format(opponent.name,opponent.total_runs))
				if batting_order == 2:
					if opponent.total_runs < first_batting_total_runs:
						print("{} wins".format(self.name))
					elif opponent.total_runs == first_batting_total_runs:
						print("Match tied")
					else:
						print("{} wins".format(opponent.name))
				break
			elif batsman_run == 0:
				opponent.total_runs = opponent.total_runs + bowler_bowl
				print("opponents total runs is {}".format(opponent.total_runs))
			else:
				opponent.total_runs = opponent.total_runs + batsman_run
				print("opponents total runs is {}".format(opponent.total_runs))
				if batting_order == 2:
					if opponent.total_runs > first_batting_total_runs:
						print("{} wins".format(opponent.name))
						win = True
			if win == True:
				break

		if batting_order == 1:
			first_batting_total_runs = opponent.total_runs
			user_name = self.name
			opponent_name = opponent.name
			user.batting(comp,first_batting_total_runs,user_name,opponent_name,2)

		

user = player()
comp = player()
toss_list = ['heads','tails']
choice_list = ['batting','bowling']
user_toss_check = False
user_choice_check = False
print("###########****WELCOME TO CRICKET****###########")
print("*****GENERAL RULE*****")
print("Use lower case letter for input")
print("Do you want to read rules. YES or NO")
read_rules = input()
if read_rules == 'yes':
	print("Rules are not added yet")
print("Time for toss")
while user_toss_check == False:
	print("heads or tails")
	toss = random.choice(toss_list)
	user_toss = input()
	if user_toss == 'heads' or user_toss == 'tails':
		user_toss_check = True
		if user_toss == toss:
			print("you won the toss")
			while user_choice_check == False:
				print("batting or bowling")
				user_choice = input()
				if user_choice == 'batting' or user_choice == 'bowling':
					user_choice_check = True
					if user_choice == 'batting':
						print("You choose to bat")
						user.batting(comp,0,'user','computer',1)
					else:
						print("You choose to bowl")
						user.bowling(comp,0,'user','computer',1)
				else:
					print("Invalid input\nPlease check if the input is in lower case or not,If not please change to lower case")
		else:
			print("You lost the toss")
			comp_choice = random.choice(choice_list)
			if comp_choice == 'batting':
				print("Computer chooses batting\nYou need to bowl first")
				user.bowling(comp,0,'user','computer',1)
			else:
				print("Computer chooses bowling\nYou need to bat first")
				user.batting(comp,0,'user','computer',1)
	else:
		print("Invalid input\nPlease check if the input is in lower case or not,If not please change to lower case")
