n = int(input())
 
numbers_array = input().split()
moves = 0
 
for i in range(1, n):
    if int(numbers_array[i]) < int(numbers_array[i-1]):
        diff = int(numbers_array[i-1]) - int(numbers_array[i])
        numbers_array[i] = int(numbers_array[i]) + diff
        moves += diff
        
print(moves)