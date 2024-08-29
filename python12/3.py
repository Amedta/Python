mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]
a, b = map(int, input("Enter two integers: ").split())
found_ab = False
found_ba = False
index_ab = -1
index_ba = -1
for i in range(len(mylist)):
    m, n = mylist[i]
    if (m, n) == (a, b):
        found_ab = True
        index_ab = i + 1  
    elif (m, n) == (b, a):
        found_ba = True
        index_ba = i + 1
if found_ab:
    print("There is (" + str(a) + ", " + str(b) + ") at the " + str(index_ab) + "th.")
elif found_ba:
    print("There is no (" + str(a) + ", " + str(b) + ") but there is (" + str(b) + ", " + str(a) + ") at the " + str(index_ba) + "th.")
else:
    print("There is no (" + str(a) + ", " + str(b) + ") nor (" + str(b) + ", " + str(a) + ").")