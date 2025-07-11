def factorial(num, result=1): 
    if num == 0: 
        return result 
    else: 
        return factorial(num - 1, result * num)
    