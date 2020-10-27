# 8.1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)
# 8.2
print(e2f.get("walrus"))
print(e2f["walrus"])
# 8.3
f2e = {e: f for f, e in e2f.items()}
print(f2e)
# 8.4
print(f2e["chien"])
# 8.5
print(e2f.keys())
print(set(e2f.keys()))
# 8.6
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
                    'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
print(type(life))
print(type(life["plants"]))
print(type(life["animals"]["octopi"]))
# 8.7
print(life.keys())
# 8.8
print(life["animals"].keys())
# 8.9
print(life["animals"]["cats"])
# 8.10
squares = {keys: keys*keys for keys in range(10)}
print(squares)
# 8.11
odd = {n for n in range(10) if n % 2}
print(odd)
# 8.12
for x in (f'Got {i}' for i in range(10)):
    print(x)
# 8.13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty',
          'How did you get a glass?')
print(dict(zip(keys, values)))
# 8.14
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster',
         'A haunted yarn shop', 'Check your exits']
movies = dict(zip(titles, plots))
print(movies)
