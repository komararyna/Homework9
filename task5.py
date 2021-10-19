import string
def word_count(text):
    for item in string.punctuation:
        if item in string.punctuation:
            text = text.replace(item, ' ')
    count = 0
    for item in text.split():
        count += 1
    return count
print(word_count('aryna,, komarevych ::::sergeevna aryna aryna aryna'))
