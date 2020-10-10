chars = ['a','b','c','d','e','a','a','b','c']
result = {}
for i in range(len(chars)):
    result[chars[i]] = result.get(chars[i], []) + [i]
print(result)


