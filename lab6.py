g = {"E": ["aT", "b"], "T": ["c", "d"]}
first = {}

for nt in g:
    first[nt] = set()
    for p in g[nt]:
        x = p[0]
        if x not in g:
            first[nt].add(x)
        else:
            first[nt] |= first[x]

for nt in first:
    print("FIRST(" + nt + ") =", first[nt])
print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 6")    