import random
 
shiki = [("$1", 300),('$1.5', 300), ('$2', 50), ('$10', 5), ('$100', 1)]
prize_list = [prize for prize, weight in shiki for i in range(weight)]
 
for i in range (0, 9):
	print(random.choice(prize_list))
# returns '$1'