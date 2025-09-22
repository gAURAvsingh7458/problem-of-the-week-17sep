# Question 1: Given a list with duplicate elements, write a program to remove duplicates and print the unique elements in the same order.

input_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = []
seen = set()

for item in input_list:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)

print(unique_list)
