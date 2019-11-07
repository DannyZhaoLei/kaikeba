# 2. 首先记录输入的7天的收入，然后记录输入的7天的支出。
# 然后打印出以下内容：
# 7天的收入(list)
# 7天的支出(list)
# 每天的结余(dict)
# 最终的结余
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_income = []
week_spend = []
day_balance = {}
for i in week:
    temp_income = int(input('Please enter your ' + i + ' income: '))
    temp_spend = int(input('Please enter your ' + i + ' spend: '))
    week_income.append(temp_income)
    week_spend.append(temp_spend)

for i in range(7):
    print('Your %s income is %d $' % (week[i], week_income[i]))

for i in range(7):
    print('Your %s spend is %d $' % (week[i], week_spend[i]))

for i in range(7):
    day_balance[week[i]] = week_income[i] - week_spend[i]

for day, balance in day_balance.items():
    print('{0} balance is {1} $'.format(day, balance))

print('The end balance is %d $' % (sum(week_income) - sum(week_spend)))
