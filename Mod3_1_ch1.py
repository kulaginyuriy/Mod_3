l = [1, 4, 1, 6, "hello","a" 5, "hello" ]
print("Повторяющиеся элементы: ")
for i in range(0, len(l)): 
    for j in range(i+1, len(l)): 
    if (arr[i] == arr[j]): 
        print(arr[j])
