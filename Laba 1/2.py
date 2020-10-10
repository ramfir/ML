a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 9, 0, 10}
peresechenie = 0
obedenenie = 0
for i in a:
    if i in b:
        peresechenie += 1
obedenenie = len(a) + len(b) - peresechenie
print(peresechenie/obedenenie)

