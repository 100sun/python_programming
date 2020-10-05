eng = input("Type a english statement: ")
words = eng.split()
words_dict = {}
for word in words:
     words_dict[word] = len(word)
print(words_dict)
