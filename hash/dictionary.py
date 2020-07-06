from collections import Counter, defaultdict, OrderedDict


dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
del dictionary['d']
print(type(dictionary), dictionary)
print("Frequency of 'a': %s \nFrequency of 'd': %s\n " % (dictionary['a'], dictionary.get('d')))


counter = Counter("abbcccd")
print(type(counter), counter)


default = defaultdict(int)
for i in "abbcccd":
    default[i] += 1
print(type(default), default)


cache = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 1})
cache.popitem(last=False)
cache['a'] = 3
print(type(cache), cache)
