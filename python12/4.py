tuples = ((), (1,), [], 'abc', (),(), (1,), ('a',), ('a', 'b'), ((),), '')
filtered_tuples = [item for item in tuples if isinstance(item, (tuple, str, list)) and item]
print("Filtered elements:", filtered_tuples)