def gcd(a: int, b: int) -> int:
    # write code here
    while True:
        remainder = b % a
        if remainder:
            b = a
            a = remainder
        else:
            return a


print(gcd(5, 7))
print(gcd(4, 6))
print(gcd(8, 12))
