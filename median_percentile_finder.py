#Write a function called percentile_50 that takes a list of arbitrary numbers
#The function will return a dictionary
#where the keys are strings that describe a the upper and lower 50th percentile (the median) as a range (see below)
#And the values are lists containing numbers from the input list that fall within the lower(inclusive) or upper(exclusive) percentile described by the key


def percentile_50(some_lst):
    d = {'<=0.50': [], '>=0.50': []}
    below_median = []
    above_median = []
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
    d['<=0.50'] += below_median
    d['>=0.50'] += above_median
    return d


lst = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
print(percentile_50(lst))

