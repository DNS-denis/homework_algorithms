# Сложность O(n*log(n))

def numberOfMatches(n):
        matches = 0
        while n > 1:
            if n % 2 != 0:            # если число нечётное, то к матчам прибаляем кол-во команд делённное на 2 и округлённое
                matches += int(n/2)   
                n = int(n/2) + 1      # команд становится вдвое меньше + 1
            else:
                matches += int(n/2)
                n = int(n/2)
        return matches

print(numberOfMatches(14))