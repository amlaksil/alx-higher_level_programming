#!/usr/bin/python3
def weight_average(my_list=[]):
    n = len(my_list)
    if n == 0:
        return 0
    sum_t = 0
    den = 0
    for i in range(n):
        sum_t += my_list[i][0] * my_list[i][1]
        den += my_list[i][1]
    return (sum_t / den)
