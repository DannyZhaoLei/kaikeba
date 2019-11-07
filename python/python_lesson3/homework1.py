# 1. 实现print函数
# 定义一个函数`print_string`，返回一个字符串。
# `print_string`函数支持输入多个参数，每个参数间使用参数`sep`(默认一个空格)的字符进行连接，
# 并且最后还要添加一个`end`(默认一个换行)参数的字符。
# 比如
# - `print_string('This is a test')` 返回`a\n`
# - `print_string('This', 'is', 'a', 'test')` 返回`This is a test\n`
# - `print_string('This', 'is', 'a', 'test', sep = '-')` 返回`This-is-a-test\n`
# - `print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')` 返回`This_is_a_test_,_Yes.`


def print_string(*strings, sep=' ', end='\n'):
    string = ''
    for i in strings:
        string += str(i)
        string += sep
    string = string[:-1] + end
    return string


print(print_string('This is a test'))
print(print_string('This', 'is', 'a', 'test'))
print(print_string('This', 'is', 'a', 'test', sep='-'))
print(print_string('This', 'is', 'a', 'test', ',', 'Yes', sep='_', end='.'))