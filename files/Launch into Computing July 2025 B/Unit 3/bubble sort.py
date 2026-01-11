# Make a sort list

list_x  = [4, 7, 2, 8, 6, 3, 9, 5, 1, 0, 12, 14, 11, 10]
print("before sorting:", list_x)

# several loops through the list
for pass_num in range(len(list_x)):
     # compare every set of items pairs
     for idx in range(len(list_x) - 1):
          # if the number from the left is bigger, swap the numbers
          if list_x[idx] > list_x[idx + 1]:
             temp = list_x[idx]
             list_x[idx] = list_x[idx + 1]
             list_x[idx + 1] = temp
     print("After pass", pass_num + 1, ":", list_x)

print("After sorting:", list_x)