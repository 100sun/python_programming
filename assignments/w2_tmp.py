# textbook given program fragment
start1 = ["fee", "fie", "foe"]
rhymes = [
     (" flop", "get a mop"),
     (" fope", "turn the rope"),
     (" fa", "get your ma"),
     (" fudge", "call the judge"),
     (" fat", "pet the cat"),
     (" fog", "walk the dog"),
     (" fun", "say we're done"),
     ]
start2 = "Someone better"

# print above compound objects
capStart1 = "! ". join(word.capitalize() for word in start1) # For the first line: Print each string in start1, capitalized and followed by an exclamation point and a space.
for first, second in rhymes:
     print( f"{ capStart1} {first.capitalize()}!") # Print first, also capitalized and followed by an exclamation point.
     print( f"{ start2} {second}.") # For the second line: Print start2 and a space. Print second and a period.
