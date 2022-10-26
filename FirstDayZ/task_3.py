# Сложность O(n)
def numJewelsInStones(jewels: str, stones: str):
    jewels_in_stones = 0           
    for element in stones:
        if element in jewels:      # если элемент есть в камнях и он является драгоценностью, то к драгоценностям +1
            jewels_in_stones += 1  
    return jewels_in_stones

print(numJewelsInStones("aA", "aAAbbbb"))
