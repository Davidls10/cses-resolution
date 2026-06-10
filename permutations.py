n = int(input())
numbers_array = []
current_number = 0

if n == 1:
    print(n)

elif n < 4:
    print("NO SOLUTION")

else:
    for i in range(0, n):
        numbers_array.append(0)
        
    current_number = 2
    for i in range(1, int(n/2) + 1):
        numbers_array[i - 1] = current_number
        current_number += 2
    current_number = 1
    for i in range(int(n/2) + 1, n+1):
        numbers_array[i - 1] = current_number
        current_number += 2

    for i in range(0, n):
        print(numbers_array[i], end=' ')