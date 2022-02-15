my_list = [5, 65, 26, 8, 485, 65, 564, 45, 44, 96, 2, 23, 56,]
total = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(total)