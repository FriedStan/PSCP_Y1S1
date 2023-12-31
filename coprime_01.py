"""CoPrimeV1"""


def find_gcd(num_1, num_2):
    """Find the GCD of 2 numbers"""
    maxine = 0
    for num in range(1, min(num_1, num_2) + 1):
        if num_1 % num == num_2 % num == 0:
            maxine = num
    if 0 in (num_1, num_2):
        maxine = max(num_1, num_2)
    return maxine


def coprimer(num_1, num_2):
    """do something"""
    gcd = find_gcd(num_1, num_2)
    if gcd == 1:
        print("YES")
    else:
        print("NO")
    print(gcd)


coprimer(int(input()), int(input()))
