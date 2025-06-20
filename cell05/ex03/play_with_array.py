arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)

transformed = {x + 2 for x in arr if x + 2 > 9}
print(transformed)