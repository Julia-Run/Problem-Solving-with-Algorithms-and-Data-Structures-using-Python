# 队列first in first out
# a=Queue() /a.enqueue(item)  / a.dequeue()  / a.size()  / a.isEmpty

from pythonds.basic import Queue
import random


# # 人围坐一圈。以queue表示，第一个进入的人（认为拿着土豆），提出并排队到尾端，此时认为土豆在顶端的人手中，一次传递完成
# # num次传递结束后，土豆在谁手里，踢出谁，即提出顶端的人。一轮结束
# # 循环，直到只剩下最后一人，游戏结束。
# def potato(names, num):
#     circle = Queue()
#     for i in names:
#         circle.enqueue(i)
#
#     while circle.size() > 1:
#         for j in range(num):
#             circle.enqueue(circle.dequeue())
#         circle.dequeue()
#
#     res = circle.dequeue()
#     print(res)
#     return res
#
#
# potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)


# # 打印机实验模拟 (简单看一次后自己写的)
# # 打印机printer：1.速度（5 or 10 / min） 2.取得一个task所需要的总时间 in s  3.busy or not  4.tick. 一秒一次
# # 一个task：1.random获得页数  2.计算总共所需耗时  3.取得耗时
# # 每秒钟是否有需要打印的任务
# # 需要一个task的队列，通过队列和进出时间可计算每个任务的等待时间。
# class Printer(object):
#     def __init__(self, ppm):
#         self.speed = ppm / 60  # in s
#         self.duration = None
#         self.current_time = None
#
#     def duration(self, atask):
#         self.duration = atask.get_duration()
#         self.current_time = self.duration
#
#     def tick(self):
#         if self.current_time > 0:
#             self.current_time = self.current_time - 1
#         else:
#             self.current_time = None
#
#     def busy(self):
#         if self.current_time is not None:
#             return True
#         else:
#             return False
#
#
# class Task(object):
#     def __init__(self):
#         self.pages = random.randrange(1, 21)
#         self.time = None
#
#     def need_time(self, rate):
#         self.time = self.pages / rate.speed  # get speed from printer
#
#     def get_duration(self):
#         return self.time
#
#
# def simulation():

# 打印机实验模拟 (第一版更新，注意：pass to next one)
# 打印机printer：1.参数：速度（5 or 10 / min）   3.busy or not  4.tick. 一秒一次
#               5. pass to next task, 取得一个task所需要的总时间 in s
# 一个task：1.random获得页数    3.取得耗时
#           4. 计算等待时间  5.获得开始时间
# 每秒钟是否有需要打印的任务

class Printer(object):
    def __init__(self, ppm):
        self.speed = ppm / 60  # in s
        self.ongoing = None  # 注意这个变量！！！
        self.time_left = 0

    def start_new(self, atask):
        self.ongoing = atask
        self.time_left = atask.get_pages() / self.speed  # newtask开始

    def tick(self):
        if self.ongoing:
            self.time_left = self.time_left - 1
            if self.time_left <= 0:
                self.ongoing = None

    def busy(self):
        if self.ongoing:
            return True
        else:
            return False


class Task(object):
    def __init__(self, begin):
        self.begin = begin
        self.pages = random.randrange(1, 21)
        self.currentT = None

    def get_pages(self):
        return self.pages

    def get_begin(self):
        return self.begin

    def wait_time(self, current):
        return current - self.begin


def have_task():
    k = random.randrange(1, 181)
    if k == 180:
        return True
    else:
        return False


# 需要一个task的队列，1. 通过队列进出时间可计算每个任务的等待时间。2.计算平均等待时间
# details：任意秒要做的事： 1.是否有要打印的任务：有，放入对列 2. 打印机是否繁忙：繁忙：tick。不繁忙且队列非空：取得顶端task的等待时间并放入list
#           dequeue, printer开始新任务，tick. 3. 计算平均等待时间
def simulation(seconds, speed_ppm):
    wait_queue = Queue()
    waitT = []
    p = Printer(speed_ppm)
    for i in range(seconds):
        if have_task():
            wait_queue.enqueue(Task(i))
        if (not p.busy()) and (not wait_queue.isEmpty()):
            new = wait_queue.dequeue()
            waitT.append(new.wait_time(i))
            p.start_new(new)
        p.tick()
    # print(waitT)
    averageWait = sum(waitT) / len(waitT)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, wait_queue.size()))


for i in range(10):
    simulation(3600, 10)
