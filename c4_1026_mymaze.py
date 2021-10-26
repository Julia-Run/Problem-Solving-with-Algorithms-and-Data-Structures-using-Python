from turtle import *

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


# 假设or判断语句中有x个并列条件，只要第一个条件满足，就会直接进入下一步。
# 先沿着第一支一直往下算，算不通就返回上一级的第二支。。。上一级全部不通就返回上上一级的第二支。。。如此循环，确定第一个条件是T or F


class Maze(object):
    def __init__(self, filename):
        # 把txt文件转换成list。确认S的初始位置
        rowsInMaze = 0
        colsInMaze = 0
        self.mazelist = []  # 初始空list
        file = open(filename, 'r')
        for line in file:
            rowlist = []
            col = 0
            for ch in line[:-1]:
                rowlist.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1  # 第5列(4)才开始出现符号（逗号也被加入了）

            rowsInMaze += 1  # (symbols start from 0)
            self.mazelist.append(rowlist)
            colsInMaze = len(rowlist)  # 总共的列数
        # print(self.startRow, self.startCol)
        self.rowsInMaze = rowsInMaze
        self.colsInMaze = colsInMaze
        self.xTranslate = -colsInMaze / 2  # 左上角的x值
        self.yTranslate = rowsInMaze / 2  # 左上角的y值
        self.t = Turtle(shape='turtle')
        # setup(width=600, height=600)
        # 左下角x左下角有，右上角下，右上角y
        setworldcoordinates(-(colsInMaze - 1) / 2 - 1, -(rowsInMaze - 1) / 2 - 1,
                            (colsInMaze - 1) / 2 + 1, (rowsInMaze - 1) / 2 + 1)

    def drawmaze(self):
        #  画障碍墙
        self.t.speed(1000)
        for y in range(self.rowsInMaze):  # 行/纵坐标
            for x in range(self.colsInMaze):  # 列/横坐标
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawbox(x + self.xTranslate, -y + self.yTranslate, 'tan')  # 坐标变换
        self.t.color('black', 'yellow')  # ？

    def drawbox(self, x, y, color):
        # 画方框，在画障碍中被调用
        tracer(0)
        self.t.up()
        self.t.goto(x - .5, y - .5)  # 左下角
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveturtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(self.xTranslate + x, self.yTranslate - y))
        self.t.goto(self.xTranslate + x, self.yTranslate - y)

    def dropbread(self, color):
        self.t.dot(15, color)  # 绘制直径为size的圆点，size默认为max（pensize+4，2*pensize），可指定为大于等于1的int

    def updatePosition(self, row, col, val=None):
        if val:
            # 设定当前位置的状态是什么
            self.mazelist[row][col] = val
        self.moveturtle(col, row)  # to （x，y）

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'black'
        elif val == TRIED:
            color = 'gray'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        # 依据不同状态画上颜色
        if color:
            self.dropbread(color)

    def __getitem__(self, idx):
        return self.mazelist[idx]

    def isExit(self, row, col):
        return row == 0 or col == 0 or row == self.rowsInMaze - 1 or col == self.colsInMaze


def searchmaze(maze, start_row, start_col):
    maze.updatePosition(start_row, start_col)
    if maze[start_row][start_col] == OBSTACLE:
        return False
    if maze[start_row][start_col] == TRIED or maze[start_row][start_col] == DEAD_END:
        return False
    if maze.isExit(start_row, start_col):
        maze.updatePosition(start_row, start_col, PART_OF_PATH)
        return True
    maze.updatePosition(start_row, start_col, TRIED)

    found = searchmaze(maze, start_row, start_col - 1) or searchmaze(maze, start_row, start_col + 1) or \
            searchmaze(maze, start_row - 1, start_col) or searchmaze(maze, start_row + 1, start_col)
    if found:
        maze.updatePosition(start_row, start_col, PART_OF_PATH)
    else:
        maze.updatePosition(start_row, start_col, DEAD_END)
    return found


myMaze = Maze('maze1.txt')
myMaze.drawmaze()
print(myMaze.startRow, myMaze.startCol)
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)

searchmaze(myMaze, myMaze.startRow, myMaze.startCol)
win = myMaze.t.getscreen()
win.exitonclick()
