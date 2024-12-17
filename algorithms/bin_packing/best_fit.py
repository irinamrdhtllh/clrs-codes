def best_fit(items, bin_capacity):
    bins = []
    for item in items:
        if len(bins) == 0:
            bin = []
            bins.append(bin)

        max_load = 0
        bin_id = None

        for i, bin in enumerate(bins):
            load = item + sum(bin)
            if load > max_load and load <= bin_capacity:
                bin_id = i
                max_load = load

        if bin_id is not None:
            bins[bin_id].append(item)
        else:
            new_bin = [item]
            bins.append(new_bin)

    return bins


items = [2, 4, 1, 6, 4, 7, 3]
bins = best_fit(items, 10)
print(bins)
