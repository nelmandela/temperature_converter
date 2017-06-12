def is_prime(n):
    if n == 2:
        return 2
    for number in range(2,n+1):
        if n%number==0:
            return False
        else:
            return n
