def first_fit(items, bin_capacity):
    bins = []
    for item in items:
        if len(bins) == 0:
            bin = []
            bins.append(bin)

        placed = False
        for bin in bins:
            empty_space = bin_capacity - sum(bin)
            if item <= empty_space:
                bin.append(item)
                placed = True
                break
        if placed is False:
            new_bin = [item]
            bins.append(new_bin)

    return bins


items = [2, 4, 1, 6, 4, 7, 3]
bins = first_fit(items, 10)
print(bins)
