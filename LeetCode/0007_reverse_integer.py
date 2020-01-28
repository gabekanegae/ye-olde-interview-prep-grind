def reverse1(x):
    if x < 0:
        r = int(str(x)[1:][::-1]) * -1
    else: 
        r = int(str(x)[::-1])

    if -2**31 <= r <= 2**31-1:
        return r
    return 0

def reverse2(x):
    neg = (x < 0)
    x = abs(x)

    r = 0
    while x > 0:
        r = r*10 + x%10 # Push
        x //= 10 # Pop

    return -r if neg else r

print(reverse1(120))
print(reverse1(1203))
print(reverse1(-1203))
print(reverse2(120))
print(reverse2(1203))
print(reverse2(-1203))