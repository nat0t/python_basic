'''Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
def int_func(word: str) -> str:
    """
    Function takes a string of lowercase letters and returns this string with uppercase
    first letter.
    :param text:
    :return:
    """
    return word.title() if word.islower() and word.isalpha() else \
        print('Not all symbols are letters and lowercase.')

def phrase_func(sentence: str) -> str:
    """
    Function takes a few words of lowercase letters and returns this words with uppercase
    first letters.
    :param sentence:
    :return:
    """
    words = sentence.split()
    sentence = []
    for word in words:
        sentence.append(int_func(word))
    try:
        sentence = ' '.join(sentence)
    except TypeError:
        print('Not all symbols are letters and lowercase.')
        return
    return sentence

if __name__ == '__main__':
    print(int_func(input('Enter a word of lowercase letters: ')))
    print(phrase_func(input('Enter a sentence of lowercase letters: ')))