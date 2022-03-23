import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ["Test1", "Test2", "Test3"]

print(grades)


eva = grades["Eva"]

sam = grades.Sam

# using loc and iloc method

test2 = grades.loc["Test2"]

test1 = grades.iloc[0]


# consectutive rows
test1_thru_test3 = grades.loc["Test1":"Test3"]

# non-consecutive rows
test1_and_test3 = grades.loc[["Test1", "Test3"]]

test1_and_test2 = grades.iloc[0:2]


# only eva and katie grades for test 1 and test 2
katie_eva = grades.loc["Test1":"Test2", ["Eva", "Katie"]]


sam_through_bob = grades.loc[["Test1", "Test3"], "Sam":"Bob"]


# Boolean Indexing

# everyone with an A grade
grades_a = grades[grades >= 90]

# dataframe with b grades
grades_b = grades[(grades >= 80) & (grades < 90)]

# dataframe for a & b
grades_a_or_b = grades[(grades >= 90) | (grades >= 80)]

pd.set_option("precision", 2)

# by student
print(grades.describe())

# by test
print(grades.T.describe())

# average of all students grades on each test
print(grades.T.mean())

# sort rows bt thier indicies (test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

# sort columns by their coloumn names (student)

c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)


print()
