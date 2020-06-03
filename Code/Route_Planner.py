route = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


count = 0

for i in range (0, len(route)-1):
    if route[i] < route[i+1] and route[i] < max(route):
        count += 1
print(count)