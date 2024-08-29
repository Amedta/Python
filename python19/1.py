n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
filtered_list = filter(lambda x: x % 2 == 0, n_list)
for item in filtered_list:
    even_list.append(item)
print(even_list)