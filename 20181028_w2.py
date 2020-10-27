# Q1.
n = int(input("num of classes? "))
s_id = int(input("your student id? "))
print(f"your class is...{s_id%100%n+1}")
# Q6
sentence = input("Type any sentence: ")
sentence = sentence.lower()
word_dict = {}
letter_dict = {}
for word in sentence.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
print(f'Occurrence of each word: {word_dict}')
print(f'Occurrence of each letter: {letter_dict}')
