def recursive_search(numbers, target, index=0):
    
   
    if index >= len(numbers):
        return -1
    
   
    if numbers[index] == target:
        return index
    
    return recursive_search(numbers, target, index + 1)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the number to search for: "))

index = recursive_search(numbers, target)

if index != -1:
    print(f"Number {target} found at index {index}.")
else:
    print(f"Number {target} not found in the list.")
