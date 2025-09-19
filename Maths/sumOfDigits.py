def sumOfDigits(n):
    add = 0
    while n > 0:
        add += n % 10
        n //= 10
    return add
