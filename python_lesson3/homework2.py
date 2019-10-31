# 2. 打印斐波那契数列
def fib_1(n):
    a, b = 0, 1
    for x in range(n):
        print('第{0}个数为:{1}'.format(x + 1, b))
        a, b = b, a + b


def fib_2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_2(n - 1) + fib_2(n - 2)


if __name__ == '__main__':
    for i in range(1, 21):
        print('第{0}个数为:{1}'.format(i, fib_2(i)))
