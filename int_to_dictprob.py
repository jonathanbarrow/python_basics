import random

def breakout_1(num):
    #take in an integer and will roll a 6-sided dice randomly for that number of times
    # will update the proportions of each number occurring and update the counts also
    # One dictionary will update the count of number of times 1 was rolled, the other dictionary will update the proportions of all numbers.

    accum = []
    d = {'num_of_count1': 0, 'pro_of_roll1': 0, 'num_of_count2': 0, 'pro_of_roll2': 0, 'num_of_count3': 0,
         'pro_of_roll3': 0, 'num_of_count4': 0, 'pro_of_roll4': 0, 'num_of_count5': 0, 'pro_of_roll5': 0,
         'num_of_count6': 0, 'pro_of_roll6': 0}
    num1 = num
    while num1 == num:
        if len(accum) == num - 1:
            num += 1
        accum += str(random.randint(1, 6))

    accum1 = []
    for item in accum:
        accum1.append(int(item))
    for item in accum1:
        if item == 1:
            d['num_of_count1'] += 1
            d['pro_of_roll1'] += 1/len(accum1)
        if item == 2:
            d['num_of_count2'] += 1
            d['pro_of_roll2'] += 1 / len(accum1)
        if item == 3:
            d['num_of_count3'] += 1
            d['pro_of_roll3'] += 1 / len(accum1)
        if item == 4:
            d['num_of_count4'] += 1
            d['pro_of_roll4'] += 1 / len(accum1)
        if item == 5:
            d['num_of_count5'] += 1
            d['pro_of_roll5'] += 1 / len(accum1)
        if item == 6:
            d['num_of_count6'] += 1
            d['pro_of_roll6'] += 1 / len(accum1)



    return d, accum1



    

print(breakout_1(100))

