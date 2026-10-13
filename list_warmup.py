# 1. Create a list called fruits containing four fruits of your choice.
fruits = ["apple", "banana", "orange", "grape"]

# 2. Print the first and last item using indexes.
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. append() a fifth fruit, then print the whole list.
fruits.append("kiwi")
print("After append:", fruits)

# 4. remove() one fruit, then print the list again.
fruits.remove("banana")
print("After remove:", fruits)

# 5. Print how many fruits remain using len().
print("Number of fruits remaining:", len(fruits))