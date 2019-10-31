# 3. 实现ATM机器
# - 查询余额
# - 存款
# - 取款
# - 退出
info = '''
======= Please select a function=======
1.Query balance
2.Save money
3.Withdraw money
4.Quit
========================
Enter>>>
'''
balance = 100
action = 0

while action != 4:
    action = int(input(info))
    if action == 1:
        print('The balance is : %d ' % balance)
    elif action == 2:
        income = int(input('Please enter the amount of deposit: '))
        balance += income
    elif action == 3:
        spend = int(input('Please enter the amount withdrawn:'))
        if spend > balance:
            print('Lack of balance.')
        else:
            balance -= spend
            print('%d has been withdrawn' % spend)
    elif action == 4:
        print('Quit')
        break
    else:
        print('Please enter the correct option.')
        continue