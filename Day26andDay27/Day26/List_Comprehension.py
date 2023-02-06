# List Comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Manas"
new_list = [letter for letter in name]
print(new_list)

doubles = [n * 2 for n in range(1, 5)]
print(doubles)

#   Conditional list Comprehension
new_list = [item for item in range(10) if item % 2 != 0]
print(new_list)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

list1 = [1, 2, 4, 7, 22, 34, 65, 98]
list2 = [2, 4, 65, 3, 22, 11, 34, 7]
common_list = [int(num) for num in list1 if num in list2]
print(common_list)