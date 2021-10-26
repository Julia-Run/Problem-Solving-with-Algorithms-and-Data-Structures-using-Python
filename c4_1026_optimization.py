# 硬币找零问题
# 在base中，直接找。否则，
# def recMC(coinValueList, change):
#     minCoins = change
#     if change in coinValueList:
#         return 1
#     else:
#         for i in [c for c in coinValueList if c <= change]:  #
#             numCoins = 1 + recMC(coinValueList, change - i)  # 多少个硬币
#             if numCoins < minCoins:
#                 minCoins = numCoins
#     return minCoins
#
#
# print(recMC([1, 5, 10, 25], 63))

# dynamic programming
# 把change前面所有的结果算‘’依次‘’出来。怎么算呢？
# 1. 0-change的的所有结果，注意一定从0开始
# 2. 对于任意一点，初始值为0-change。接着进入循环：
#       j=【零钱列表中的&小于等于该change的值】。对不同的j，可以得到一个coins_j,最小值为对应change的最小值
def dp(coinlist, change, coins, used):
    for j in range(change + 1):  # change范围内所有需要找零的值j,构造列表
        amount = j  # 假设全部找零一块
        newcoin = 1
        for i in [c for c in coinlist if c <= amount]:
            if 1 + coins[j - i] < amount:
                amount = 1 + coins[j - i]  # 更新为更小的值
                newcoin = i
        coins[j] = amount  # 更新为最小的值
        used[j] = newcoin  # 每个change使用的最后一个硬币
    return coins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]  # 53-1-10-21 --》 52（10）， 42（21）， 21（21）
        print(thisCoin)
        coin = coin - thisCoin  # 前面的coin函数在对应位置，只用了一个值（也就是最后一个硬币）


def main():
    amnt = 53
    clist = [1, 5, 10, 21, 25]
    coinCount = [0] * (amnt + 1)
    used = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dp(clist, amnt, coinCount, used), "coins")
    print(used, '/n', len(used))
    printCoins(used, amnt)


main()
