from pythonds.basic import Queue
import random


# # 传土豆
# # 1. 传递n次为一轮，一轮结束后，踢掉拿着土豆的人，直到只剩下一人，游戏结束
# # 队伍顶端的人为拿着土豆的人，人在跑，土豆不跑
# def potato(names, num):
#     circle = Queue()
#     for i in names:
#         circle.enqueue(i)
#     while circle.size() > 1:
#         k = random.randrange(1, num + 1)
#         for i in range(k):
#             circle.enqueue(circle.dequeue())
#         circle.dequeue()
#     res = circle.dequeue()
#     print(res)
#     return res
#
#
# for i in range(1, 11):
#     potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)


# 打印机实验（每一秒发生的事情）
# printer：1. 参数:打印速度，是否工作，剩余多少工作时间  2.方法一：此时不在工作，开始下一个任务。 4.方法二：是否在工作
#           3。方法三：打印机一秒的工作--当前任务工作时长 - 1 s （如果有当前任务）。总时长为0，进入停止工作状态
# task：1. 参数：开始时间,页数 2.方法一: get pages 3.方法二：get waiting time
# func1： 任意秒是否有任务进行
# simulation：1.参数：总仿真时长，打印机速度  2。等待时长list，排队等候queue， 打印机， 是否有new task
#               3.任意秒是否有new task，有则加入queue。 4.打印机是否繁忙，繁忙，tick， 不繁忙且queue非空：开始newtask，newtask恩待时间加入list，tick
class Printer(object):
    def __init__(self, ppm):
        self.speed = ppm / 60  # in s
        self.ongoing = None
        self.timeleft = 0

    def busy(self):
        if self.ongoing:
            return True
        else:
            return False

    def startnew(self, newtask):
        self.ongoing = newtask
        self.timeleft = newtask.pages / self.speed

    def tick(self):
        if self.ongoing:
            self.timeleft = self.timeleft - 1
        if self.timeleft <= 0:
            self.ongoing = None


class Task(object):
    def __init__(self, startT):
        self.start = startT
        self.pages = random.randrange(1, 21)

    def waitT(self, end):
        return end - self.start


def ifnew():
    k = random.randrange(1, 181)
    if k == 180:
        return True
    else:
        return False


def simulation(seconds, ppms):
    waitlist = []
    waitqueue = Queue()
    p = Printer(ppms)
    for i in range(seconds):
        if ifnew():
            waitqueue.enqueue(Task(i))
        if not p.busy() and not waitqueue.isEmpty():
            new = waitqueue.dequeue()
            waitlist.append(new.waitT(i))
            p.startnew(new)
        p.tick()

    aveT = sum(waitlist) / len(waitlist)
    print('average waitting time is %6.2f sec, %3d tasks left' % (aveT, waitqueue.size()))


for i in range(10):
    simulation(3600, 15)
