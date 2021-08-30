import pyperclip
text = pyperclip.paste()

for i in range(len(text)):
	text[i] += '+'
	
pyperclip.copy(text)
input('Press enter to exit')