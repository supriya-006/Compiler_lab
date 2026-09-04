g = {"E": ["T+F", "F"], "T": ["i"], "F": ["i"]}
follow = {"E": {"$"}, "T": set(), "F": set()}

for a in g:
    for p in g[a]:
        for i in range(len(p) - 1):
            if p[i] in g and p[i+1] not in g:
                follow[p[i]].add(p[i+1])

for x in follow:
    print("FOLLOW(" + x + ") =", follow[x])

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 7")    