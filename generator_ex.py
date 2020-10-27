def func_get_odds():
     for num in range(1,10,2):
          return num
n = func_get_odds()
print(n)

def gen_get_odds():
     for num in range(1,10,2):
          yield num
n = gen_get_odds()
print(list(n))

genobj = (pair for pair in zip(['a','b'], ['1', '2']))
print(list(genobj))
print(list(genobj))
