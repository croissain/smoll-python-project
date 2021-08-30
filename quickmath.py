import random, time

def add_subtract():
    i = random.randint(1, 999)
    j = random.randint(1, 999)
    syms = ['+', '-']
    c = random.choice(syms)
    if(i<j and c =='-'):
        # đổi chỗ i và j
    	temp = i
    	i = j
    	j = temp
    	print(str(i) + ' ' + c + ' ' + str(j) + ' = ')
        while(int(ans) != i - j):
            print("Sai rùi\n")
            ans = input()
    elif (i > j and c == '-'):
        print(str(i) + ' ' + c + ' ' + str(j) + ' = ')
        ans = input()
        while(int(ans) != i - j):
            print("Sai rùi\n")
            ans = input()

    else:
    	print(str(i) + ' ' + c + ' ' + str(j) + ' = ')
        ans = input()
        while(int(ans) != i - j):
            print("Sai rùi\n")
            ans = input()

for time in range (1, 10):
	add_subtract()
	print('\n')