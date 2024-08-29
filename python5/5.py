s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cdde', 'opq']
shortest_string = s_list[0]
for string in s_list[1:]:
    if len(string) > len(shortest_string):
        shortest_string = string
print(f"The shortest string: {shortest_string}")
