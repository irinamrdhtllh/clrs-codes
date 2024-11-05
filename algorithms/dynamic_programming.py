def memoized_cut_rod(p, n):
    r = (n + 1) * [float("-inf")]
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = float("-inf")
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = (n + 1) * [float("-inf")]
    r[0] = 0
    for j in range(1, n + 1):
        q = float("-inf")
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
r = memoized_cut_rod(p, 4)
print(r)
