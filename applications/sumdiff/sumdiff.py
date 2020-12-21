"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
sum_map = {}
diff_map = {}
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


for i in q:
    for j in q:
        fi = f(i)
        fj = f(j)
        if (j, i) not in sum_map:
            sum_map[(i, j)] = ((fi + fj, fi, fj))
        diff_map[(i, j)] = ((fi - fj, fi, fj))

for d in diff_map.items():
    for s in sum_map.items():
        if s[1][0] == d[1][0]:
            ((s1, s2), (st, s1v, s2v)) = s
            ((d1, d2), (dt, d1v, d2v)) = d
            print(
                f"f({s1}) + f({s2}) = f({d1}) - f({d2})  {s1v} + {s2v} = {d1v} - {d2v}")
            if s1 != s2:
                print(
                    f"f({s2}) + f({s1}) = f({d1}) - f({d2})  {s2v} + {s1v} = {d1v} - {d2v}")
