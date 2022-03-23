import pandas as pd


grades = pd.Series([87, 100, 94])

print(grades)

a = pd.Series(98.6, range(3))
print()


b = grades[0]


c = grades.count()

d = grades.mean()

print(grades.describe())

grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])

grades_dict = {"Wally": 87, "Eva": 100, "Sam": 94}

grads_ds = pd.Series(grades_dict)


e = grades.values


hardware = pd.Series(["Hammer", "Saw", "Wrench"])

f = hardware.str.contains("a")

g = hardware.str.upper()


# convert a series object ot python list
hardware_list = hardware.to_list()


ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

h = ds1 == ds2

i = ds1 < ds2

j = ds1 > ds2


# series of one list to one seris
list_of_series = pd.Series([["Red", "Green", "White"], ["Red", "Black"], ["Yellow"]])


list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)

# sort seirs
s = pd.Series(["100", "200", "python", "300.12", "400"])


s = pd.Series(["100", 200, "python", 300.12, "400"])

sotred_series = s.sort_values


# adding to a series
s = s.append(pd.Series(["500", "php"])).reset_index(drop=True)

# calculate the frequency count of each unique value of a given stat

import random

list1 = [random.randrange(1, 10) for i in range(0, 100)]
s = pd.Series(list1)
result = s.value_counts()

#
print()
