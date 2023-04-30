# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:02:28 2023

@author: 86319
"""

import random
import matplotlib.pyplot as plt

# 掷骰子
def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100>roll>50:
        return True

# 简单的赌徒
def simple_bettor(funds,initial_wager,wager_count):
    value = funds           # 资金
    wager = initial_wager   # 赌注
    wX = []                 # wager X
    vY = []                 # value Y
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)
        currentWager += 1
    plt.plot(wX,vY)         # 画图
    # 分类
    if value<=0:
        return "破产"
    elif value<funds:
        return "输"
    elif value>funds:
        return "赢"
    elif value==funds:
        return "平局"

x = 0
# 赌博人数
people = 100
# funds 赌金
funds = 10000
# 赌注
initial_wager = 100
# 模拟赌博次数
count = 100000

num_win = 0
num_lose = 0
num_broke = 0
num_equal = 0

while x < people:
    result = simple_bettor(funds,initial_wager,count)
    x += 1
    if result == '赢':
        num_win += 1
    elif result == '输':
        num_lose += 1
    elif result == '破产':
        num_broke += 1
    elif result == '平局':
        num_equal += 1

print("%d 人正在赌博"%people)
print("每个人赌博 %d 次"%count)
print("赢的人数:",num_win)
print("输的人数:",num_lose)
print("破产的人数:",num_broke)
print("平局的人数:",num_equal)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.ylabel("剩余的钱数")
plt.xlabel("投注次数")
plt.show()