s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cdde', 'opq']
min_length = len(min(s_list, key=len))
shortest_strings = [s for s in s_list if len(s) == min_length]
shortest_strings.sort(key=len)
print("The shortest strings:",end="")
print(" ".join(map(str,shortest_strings)))
