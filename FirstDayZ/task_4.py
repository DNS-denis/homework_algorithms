# сложность O(n*log(n))
# Код ищет минимальную абсолютную разность.
def minimumAbsDifference(arr: list[int]):
    arr.sort()
    min_num = 10**6
    for i in range(1, len(arr)): # Задается цикл, проверяющий с помощью условий каждое значение списка
        pAbs = abs(arr[i] - arr[i-1])
        if pAbs < min_num:
            min_num = pAbs
            spsk = []
        if pAbs == min_num:
            spsk.append([arr[i-1], arr[i]])
        return spsk # И возвращает 2 минимальную абсолютную разность
print(minimumAbsDifference([1, 2, 3, 4, 5]))
