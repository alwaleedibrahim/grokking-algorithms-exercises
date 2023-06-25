# fab series using a loop
def loop_fab(size): 
    fab_series = []
    for i in range(2):
        if (i==size):
            break
        fab_series.append(i)
    for i in range(2, size):
        fab_series.append(fab_series[i-1] + fab_series[i-2])
    return fab_series


# fab series using recursion
fab_series = []
def recursive_fab(size): 
    if size <= 2:
        base_series = []
        for i in range(size):
            base_series.append(i)
        return base_series
    else:
        smaller_fab = recursive_fab(size-1)
        smaller_fab.append(smaller_fab[-1] + smaller_fab[-2])
        return smaller_fab
series_size = int(input("Enter the size of fab series: "))
print(recursive_fab(series_size))
print(loop_fab(series_size))



