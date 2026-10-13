# 1. Start with this list in your code:
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Loop through the list and print each item numbered: 1. bread, 2. avocado, ...
print("Numbered list:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# 2. Count how many item names have more than 4 letters (a loop + an if).
long_name_count = 0
for item in items:
    if len(item) > 4:
        long_name_count += 1
print(f"\nItems with more than 4 letters: {long_name_count}")

# 3. Find and print the longest item name using a loop comparison —
# no shortcuts, build the pattern yourself.
longest_item = ""
for item in items:
    if len(item) > len(longest_item):
        longest_item = item
print(f"Longest item name: {longest_item}")