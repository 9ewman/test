N = 1000000


def dec_to_bin(number):
    s = ''
    while number > 0:
        s += str(number % 2)
        number = number // 2
    return s


def is_palindrome_bin(s):
    return s[::-1] == s


def is_palindrome_dec(number):
    s_n = str(number)
    return s_n[::-1] == s_n


palindrome_sum = 0
for n in range(1, N+1, 2):
    if (is_palindrome_dec(n) and is_palindrome_bin(dec_to_bin(n))):
        palindrome_sum += n

print(palindrome_sum)
