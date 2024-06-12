def binary_search(element, some_list):
    # 여기에 코드를 작성하세요
    start = 0
    final = len(some_list) - 1
    
    while start <= final:
        middle = (start + final) // 2
        if some_list[middle] == element:
            return middle
        else:
            if element < some_list[middle]:
                final = middle - 1 
            elif element > some_list[middle]:
                start = middle + 1
    return None
                

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))