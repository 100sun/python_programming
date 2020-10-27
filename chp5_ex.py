# 5.1 Capitalize the word starting with m:
song = """ When an eel grabs your arm, ... And it causes great harm, ... That's - a moray!"""
song = song.replace('m',' M')
print(song)
#5.2 Print each list question with its correctly matching answer in the form: Q: question A: answer > > >
questions = [
     "We don't serve strings around here. Are you a string?",
     "What is said on Father's Day in the forest?",
     "What makes the sound 'Sis! Boom! Bah!'?"
     ]
answers = [
     "An exploding sheep.",
     "No, I'm a frayed knot.",
     "' Pop!' goes the weasel."
     ]
for i in range(0,3):
     print(f'Q: {questions[i]}\nA: {answers[i]}')
#5.3 Write the following poem by using old-style formatting. Substitute the strings 'roast beef', 'ham', 'head', and 'clam' into this string:
poem = '''My kitty cat likes %s,  My kitty cat likes %s,  My kitty cat fell on his %s  And now thinks he's a %s'''
args = ('roast beef','ham','head','claim')
print(poem % args) # ∵ must be immutable values.. -> set
#5.6 old style
names = ['duck', 'gourd', 'spitz']
for name in names:
     print("%sy Mc%sface" % (name.capitalize(), name.capitalize()))
#5.7 new style
for name in names:
     print("{}y Mc{}face".format(name.capitalize(), name.capitalize()))
#5.8 newest tysle
for name in names:
     print(f"{name.capitalize()}y Mc{name.capitalize()}face")
