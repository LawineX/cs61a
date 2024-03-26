def remove_digit(n, num, verison='iter'):
    if verison=='iter':
        ret = 0
        i = 0
        while (n):
            if n % 10 != num:
                ret += (n % 10) * 10 ** i
                i += 1
            n //= 10
        return ret
    if verison=='recu':
        if n<10:
            if n!=num:
                return n
            else:
                return 0
        else:
            if n%10!=num:
                return n%10+10*remove_digit(n//10,num,verison='recu')
            else:
                return remove_digit(n // 10, num, verison='recu')

a=remove_digit(3141592653589793,5,verison='recu')
print(a)