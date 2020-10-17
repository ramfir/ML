a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 9, 0, 10}
intersection = 0
union = 0
for i in a:
    if i in b:
        intersection += 1
union = len(a) + len(b) - intersection
print(intersection/union)

