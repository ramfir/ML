chars = ['a','b','c','d','e','a','a','b','c']
print({key: [i for i, j in enumerate(chars) if j == key] for key in chars})
