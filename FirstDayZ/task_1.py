# Сложность O(n)
# функция делит на два если число чётное и отнимает 1 если нечётное
def numberOfSteps (num):
        step = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2 
            else:
                num -= 1 
            step += 1
        return step
    
print(numberOfSteps(30))