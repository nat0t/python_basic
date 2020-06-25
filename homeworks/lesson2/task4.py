string = input('Enter few words with spaces: ')
words = string.split()
for word in enumerate(words, 1):
    print(f'{word[0]:<6}{word[1][:10]:<11}') if len(word[1]) > 10 \
        else print(f'{word[0]:<6}{word[1]:<11}')