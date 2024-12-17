def next_fit(items, bin_capacity):
    bins = []
    for item in items:
        if len(bins) == 0:
            bin = []
            bins.append(bin)

        bin = bins[-1]
        empty_space = bin_capacity - sum(bin)

        if item <= empty_space:
            bin.append(item)
        else:
            bin = [item]
            bins.append(bin)

    return bins


items = [2, 4, 1, 6, 4, 7, 3]
bins = next_fit(items, 10)
print(bins)
