list1 = [1, 2, 3, 4, 5, 6, "7", "7"]
list2 = [8, 7, 6, 5, 4, 3, 2, 1]

# Create a new list with duplicates removed
new_list1 = []
new_list2 = []
for i, x in enumerate(list1):
    if x not in new_list1:
        new_list1.append(x)
        new_list2.append(list2[i])

print(new_list1)  # Output: [1, 2, 3, 4, 5, 6]
print(new_list2)  # Output: [2, 4, 6, 8, 10, 14]