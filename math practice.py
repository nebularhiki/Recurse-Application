from collections import Counter

# list of numbers
n_num = [10, 11, 4, 7, 12, 11, 16, 6, 9, 15]
n = len(n_num)
n_num.sort()

# get the mean
get_sum = sum(n_num)
mean = get_sum / n

# get the median
if n % 2 == 0:
    median1 = n_num[n // 2]
    median2 = n_num[n // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = n_num[n // 2]

# get the mode
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "".join(map(str, mode))

# print answer
print(n_num)
print(f"Mean, median, mode is: {mean}, {median}, {get_mode}.")
