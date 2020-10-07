eng = input("Type any senetence in english : ")
words = eng.split()
wordCnt = dict()
letterCnt = dict()

for word in words:
     if word in wordCnt:
          wordCnt[word] += 1
     else:
          wordCnt[word] = 1
     for letter in word:
          if letter in letterCnt:
               letterCnt[letter] += 1
          else:
               letterCnt[letter] = 1

print("Occurences of each word you typed: ", wordCnt);
print("Occurences of each letter you typed: ", letterCnt);
