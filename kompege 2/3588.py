print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = not(y <= w) or (x == z) or x
                if F == 0:
                    print(w, x, y, z)
#zywx
