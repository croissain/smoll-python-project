import pyperclip
text = pyperclip.paste()
words = text.split()
for i in range(len(words)):
	words[i] = '-' + words[i]

	
text = ''.join(words)
pyperclip.copy(text)
input('Press enter to exit')


# le nguyen nhat tho
# -le-nguyen-nhat-tho