# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:23:29 2023

@author: 86319
"""

import random
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
# 赌博人数
sampleSize = 100
# 赌资
startingFunds = 1000000000
# 每次赌金
wagerSize = 100
# 赌博次数
wagerCount = 3000

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100>roll>=50:
        return True

def double_bettor(funds,initial_wager,wager_count):
    global double_busts
    global double_lose
    global double_profits
    value = funds           # 资金
    wager = initial_wager   # 赌注
    wX = []                 # wager X
    vY = []                 # value Y
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'lose'
                previousWagerAmount = wager     # 前一次赌注
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    double_busts += 1
                    break
        elif previousWager == 'lose':
            if rollDice():
                wager = previousWagerAmount * 2
                if(value - wager) < 0:          # 钱不够时
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                if(value - wager) < 0:
                    wager = value
                value -= wager
                previousWager = 'lose'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    double_busts += 1
                    break
        currentWager += 1
    plt.plot(wX,vY)         # 画图
    # 分类
    if value>funds:
        double_profits += 1
    elif value<funds:
        double_lose += 1

def Print_result():
    print("总赌金:",startingFunds)
    print("开始每次赌金:",wagerSize)
    print("赌博次数:",wagerCount)
    print("赌钱人数:",sampleSize)
    print("破产几率:",(double_busts/sampleSize)*100.00)
    print("赢钱几率:",(double_profits/sampleSize)*100.00)
    print("输钱几率:",(double_lose/sampleSize)*100.00)


x = 0
double_busts = 0.0
double_profits = 0.0
double_lose = 0.0

while x < sampleSize:
    double_bettor(startingFunds,wagerSize,wagerCount)
    x += 1

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.axhline(0,color='r')
plt.ylabel("资金值")
plt.xlabel("下注次数")
Print_result()
plt.show()
