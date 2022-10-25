# #1
# def numberOfSteps (num):
#         step = 0
#         while num > 0:
#             if num % 2 == 0:
#                 num /= 2 
#             else:
#                 num -= 1 
#             step += 1
#         return step
    
# print(numberOfSteps(30))


# #2
# def numberOfMatches(n):
#         matches = 0
#         while n > 1:
#             if n % 2 != 0:
#                 matches += int(n/2) 
#                 n = int(n/2) + 1
#             else:
#                 matches += int(n/2)
#                 n = int(n/2)
#         return matches

# print(numberOfMatches(14))


#3
def numJewelsInStones(jewels: str, stones: str):
    jewels_in_stones = 0
    for element in stones:
        if element in jewels:
            jewels_in_stones += 1
    return jewels_in_stones

print(numJewelsInStones("aA", "aAAbbbb"))