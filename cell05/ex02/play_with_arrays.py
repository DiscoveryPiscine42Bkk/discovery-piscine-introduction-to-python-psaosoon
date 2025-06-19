original_array = [2, 8, 9, 48, 8, 22, -12, 2]
#filter values greater than 5
filtered = [num for num in original_array if num > 5]
#Remove duplicates using a set while preserving order
unique_filtered = []
seen = set()
for num in filtered:
    if num not in seen:
        unique_filtered.append(num)
        seen.add(num)
print(unique_filtered)