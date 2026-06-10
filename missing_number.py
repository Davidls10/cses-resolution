n = int(input())
numbers_array = []
boolean_array = []
 
numbers_array = input().split()
 
for i in range(n):
    boolean_array.append(0)
for i in numbers_array:
    boolean_array[int(i) - 1] = 1
    
for i in range(1, n+1):
    if boolean_array[i-1] == 0:
        print(i)
        break