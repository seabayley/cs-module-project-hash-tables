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
        if (j, i) not in sum_map:
            sum_map[(i, j)] = f(i) + f(j)
        diff_map[(i, j)] = f(i) - f(j)

for d in diff_map.items():
    for s in sum_map.items():
        if d[1] == s[1]:
            s1 = s[0][0]
            s2 = s[0][1]
            d1 = d[0][0]
            d2 = d[0][1]
            print(
                f"f({s1}) + f({s2}) = f({d1}) - f({d2})  {f(s1)} + {f(s2)} = {f(d1)} - {f(d2)}")
            if s1 != s2:
                print(
                    f"f({s2}) + f({s1}) = f({d1}) - f({d2})  {f(s2)} + {f(s1)} = {f(d1)} - {f(d2)}")
