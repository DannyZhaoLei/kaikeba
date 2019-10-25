# 1. Determine whether it is a leap year
# year = int(input('Please enter a year:'))
# if (year % 4 == 0 and year % 100 != 0) | (year % 400 == 0):
#     print('The year %s is a leap year.' % year)
# else:
#     print('The year %s is not a leap year.' % year)

# 2. 首先记录输入的7天的收入，然后记录输入的7天的支出。
# 然后打印出以下内容：
# 7天的收入(list)
# 7天的支出(list)
# 每天的结余(dict)
# 最终的结余
# week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# week_income = []
# week_spend = []
# day_balance = {}
# for i in week:
#     temp_income = int(input('Please enter your ' + i + ' income: '))
#     temp_spend = int(input('Please enter your ' + i + ' spend: '))
#     week_income.append(temp_income)
#     week_spend.append(temp_spend)
#
# for i in range(7):
#     print('Your %s income is %d $' % (week[i], week_income[i]))
#
# for i in range(7):
#     print('Your %s spend is %d $' % (week[i], week_spend[i]))
#
# for i in range(7):
#     day_balance[week[i]] = week_income[i] - week_spend[i]
#
# for day, balance in day_balance.items():
#     print('{0} balance is {1} $'.format(day, balance))
#
# print('The end balance is %d $' % (sum(week_income) - sum(week_spend)))

# 3. 实现ATM机器
# - 查询余额
# - 存款
# - 取款
# - 退出
# info = '''
# ======= Please select a function=======
# 1.Query balance
# 2.Save money
# 3.Withdraw money
# 4.Quit
# ========================
# Enter>>>
# '''
# balance = 100
# action = 0
#
# while action != 4:
#     action = int(input(info))
#     if action == 1:
#         print('The balance is : %d ' % balance)
#     elif action == 2:
#         income = int(input('Please enter the amount of deposit: '))
#         balance += income
#     elif action == 3:
#         spend = int(input('Please enter the amount withdrawn:'))
#         if spend > balance:
#             print('Lack of balance.')
#         else:
#             balance -= spend
#             print('%d has been withdrawn' % spend)
#     elif action == 4:
#         print('Quit')
#         break
#     else:
#         print('Please enter the correct option.')
#         continue
# 4.词汇表生成及统计
# text = '2019 年 十月 一日 上午 ， 庆祝 中华人民共和国 成立 70 周年 阅兵式 在 首都北京 盛大举行 ， 59 个 阅兵 方阵 ， 580 台受 ' \
#        '阅 装备 ， 1.5 万人 的 参阅 队伍 接受 了 全国 人民 的 检阅 。 阅兵 装备 方队 展示 的 武器装备 皆 为 国产 现役 主战 装备' \
#        ' ， 40% 为 首次 展示 。 其中 近些年来 广受 全球 关注 的 东风 41 洲际 弹道导弹 ， 巨浪 二潜射 弹道导弹 ， 东风 17 高超音' \
#        '速 武器 系统 终于 揭幕 亮剑 ， 以 " 不怒 自威 " 的 形象 向 世界 展示 中国 捍卫 和平 的 意志 与 力量 。 相较 于 其他 首度' \
#        ' 公开 亮相 的 武器装备 ， 这 三款 武器 多年 来 传闻 不断 ， 备受 关注 ， 并 因 其 " 大国 基石 " 的 地位 而 被 公众 赋予' \
#        ' 特殊 的 期待 ， 这 三款 武器装备 实力 究竟 如何 ， 又 各自 承担 着 怎样 的 历史 " 使命 " 呢 ？ 本报 特约 相关 领域 ' \
#        '军事 专家 ， 为 大家 详细 解读 这 三款 彰显 国威 ， 震撼 世界 的 国 之 重器 。'
# word = text.split(' ')
# vocab = list(set(word))
# word2id = {}
# id2word = {}
# temp = 0
# for i in vocab:
#     word2id[i] = temp
#     temp += 1
# print(word2id)
#
# for word, number in word2id.items():
#     id2word[number] = word
# print(id2word)
