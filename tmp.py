eng = input("Type any senetence in english : ")
words = eng.split()
wordCnt = dict()
letterCnt = dict()

for word in words:
     word_lower = word.lower()
     if word_lower in wordCnt:
          wordCnt[word_lower] += 1
     else:
          wordCnt[word_lower] = 1
     for letter in word_lower:
          if letter in letterCnt:
               letterCnt[letter] += 1
          else:
               letterCnt[letter] = 1

print("Occurences of each word you typed: ", wordCnt);
print("Occurences of each letter you typed: ", letterCnt);
