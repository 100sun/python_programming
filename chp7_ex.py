#7.1
years_list=[i+1999 for i in range(6)]
print(years_list)
#7.2
print(years_list[3])
#7.3
print(years_list[len(years_list)-1])
print(years_list[-1])
#7.4
things=["mozzarella", "cinderella", "salmonella"]
print(things)
#7.5
print(things[1].capitalize())
print(things)
things[1]=things[1].capitalize()
print(things)
#7.6
things[2]=things[2].upper()
print(things)
#7.7
del things[-1]
print(things)
#7.8
surprise=["Groucho", "Chico", "Harpo"]
print(surprise)
#7.9
surprise[-1]=surprise[-1].lower()
surprise[-1]=surprise[-1][::-1]
surprise[-1]=surprise[-1].capitalize()
print(surprise)
#7.10
even=[i for i in range(10) if i%2==0]
print(even)
#7.11
start1 = ["fee", "fie", "foe"]
rhymes = [ ("flop", "get a mop"), ("fope", "turn the rope"), ("fa", "get your ma"), ("fudge", "call the judge"), ("fat", "pet the cat"), ("fog", "walk the dog"), ("fun", "say we're done"), ]
start2 = "Someone better"
cap_start1 = '! '.join(word.capitalize() for word in start1)
for first, second in rhymes:
     print(f'{cap_start1}! {first.capitalize()}!')
     print(f'{start2} {second}.')
