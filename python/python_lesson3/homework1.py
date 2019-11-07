# 1. ʵ��print����
# ����һ������`print_string`������һ���ַ�����
# `print_string`����֧��������������ÿ��������ʹ�ò���`sep`(Ĭ��һ���ո�)���ַ��������ӣ�
# �������Ҫ���һ��`end`(Ĭ��һ������)�������ַ���
# ����
# - `print_string('This is a test')` ����`a\n`
# - `print_string('This', 'is', 'a', 'test')` ����`This is a test\n`
# - `print_string('This', 'is', 'a', 'test', sep = '-')` ����`This-is-a-test\n`
# - `print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')` ����`This_is_a_test_,_Yes.`


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