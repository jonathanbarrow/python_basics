#Let’s make a function that takes in a list of random numbers (Could be floats or ints) and returns a dictionary which
# identifies where the numbers appear in terms of quartiles. Assume each quartile mark is includes the lower end of the
# range and goes up to but does not include the upper end of the range.

def percentile_50(some_lst):
    d = {'<Q1': [], '>=Q1 and <0.5': [], '>=0.5 and <Q3': [], '>=Q3': []}
    below_median = []
    above_median = []
    quartile1 = []
    quartile3 = []
    median = []
    some_lst = sorted(some_lst)
    if len(some_lst) % 2 == 0:
        middle_val1 = int(len(some_lst)/2)
        middle_val2 = int(len(some_lst)/2 - 1)
        median = ((some_lst[middle_val1])+(some_lst[middle_val2]))/2
    if len(some_lst) % 2 == 1:
        median = (some_lst[int(len(some_lst)/2 - 0.5)])

    for item in some_lst:
        if item >= median:
            above_median.append(item)
        if item <= median:
            below_median.append(item)
    for item in above_median:
        if len(above_median) % 2 == 0:
            middle_val3 = int(len(above_median) / 2)
            middle_val4 = int(len(above_median) / 2 - 1)
            quartile3 = ((above_median[middle_val3]) + (above_median[middle_val4])) / 2
        if len(above_median) % 2 == 1:
            quartile3 = (above_median[int(len(above_median) / 2 - 0.5)])
    for item in below_median:
        if len(below_median) % 2 == 0:
            middle_val5 = int(len(below_median) / 2)
            middle_val6 = int(len(below_median) / 2 - 1)
            quartile1 = ((below_median[middle_val5]) + (below_median[middle_val6])) / 2
        if len(below_median) % 2 == 1:
            quartile1 = (below_median[int(len(below_median) / 2 - 0.5)])
    for item in some_lst:
        if item < quartile1:
            d['<Q1'].append(item)
        if item >= quartile1 and item < median:
            d['>=Q1 and <0.5'].append(item)
        if item >= median and item < quartile3:
            d['>=0.5 and <Q3'].append(item)
        if item >= quartile3:
            d['>=Q3'].append(item)
    return d


lst = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
print(percentile_50(lst))

