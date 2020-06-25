text = None
while text != '':
    text = input('Enter a line of text (empty line for stop):\n')
    with open('text.txt', 'a') as file:
        file.write(text + '\n')