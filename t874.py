# 机器人类

import numpy as np
class Robots:
    direction = 'Y+'
    coordinate = [0,0]

    def __init__(self):
        self.pointer = 0
        self.max_distance = 0
        print('我是一个机器人，初始坐标是：', self.coordinate)

    def move(self, commands: list[int], obstacles: list[list[int]]):
        if [0,0] in obstacles:
            return 0
        else:
            direction_set = ['Y+','X+','Y-','X-']
            for item in commands:
                # 机器人的方向
                if item==-1:
                    if self.direction=='X-':
                        self.pointer = 0
                        self.direction = direction_set[self.pointer]
                    else:
                        self.pointer += 1
                        self.direction = direction_set[self.pointer]
                elif item==-2:
                    if self.direction=='Y+':
                        self.pointer = 3
                        self.direction = direction_set[self.pointer]
                    else:
                        self.pointer -= 1
                        self.direction = direction_set[self.pointer]
                # 机器人移动指令
                else:
                    if self.direction=='Y+':
                        temp = []
                        for obs in obstacles:  #先找出相关的障碍物，存入temp列表
                            if obs[0]!=self.coordinate[0]:
                                continue
                            elif obs[1]>self.coordinate[1]:
                                temp.append(obs[1]-self.coordinate[1]-1)
                        if temp!=[] and min(temp)<item:
                            self.coordinate[1] += min(temp)
                        else:
                            self.coordinate[1] += item

                    elif self.direction=='Y-':
                        temp = []
                        for obs in obstacles:
                            if obs[0]!=self.coordinate[0]:
                                continue
                            elif obs[1]<self.coordinate[1]:
                                temp.append(-obs[1]+self.coordinate[1]-1)
                        if temp!=[] and min(temp)<item:
                            self.coordinate[1] -= min(temp)
                        else:
                            self.coordinate[1] -= item

                    elif self.direction=='X+':
                        temp = []
                        for obs in obstacles:
                            if obs[1]!=self.coordinate[1]:
                                continue
                            elif obs[0]>self.coordinate[0]:
                                temp.append(obs[0]-self.coordinate[0]-1)
                        if temp!=[] and min(temp)<item:
                            self.coordinate[0] += min(temp)
                        else:
                            self.coordinate[0] += item

                    else:
                        temp = []
                        for obs in obstacles:
                            if obs[1]!=self.coordinate[1]:
                                continue
                            elif obs[0]<self.coordinate[0]:
                                temp.append(-obs[0]+self.coordinate[0]-1)
                        if temp!=[] and min(temp)<item:
                            self.coordinate[0] -= min(temp)
                        else:
                            self.coordinate[0] -= item

                self.max_distance = max(self.max_distance, self.coordinate[0]**2+self.coordinate[1]**2)
            return self.max_distance


commands = [-2,-1,8,9,6]
obstacles = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]
robot1 = Robots()

print(robot1.move(commands, obstacles))

print(robot1.direction)
print(robot1.coordinate)

'''
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = 'Y+'
        coordinate = [0,0]
        direction_set = ['Y+','X+','Y-','X-']
        pointer = 0
        max_distance = 0
        for item in commands:
            if item==-1:
                if direction=='X-':
                    pointer = 0
                    direction = direction_set[pointer]
                else:
                    pointer += 1
                    direction = direction_set[pointer]
            elif item==-2:
                if direction=='Y+':
                    pointer = 3
                    direction = direction_set[pointer]
                else:
                    pointer -= 1
                    direction = direction_set[pointer]
            else:
                if direction=='Y+':
                    temp = []
                    for obs in obstacles:
                        if obs[0]!=coordinate[0]:
                            continue
                        elif obs[1]>coordinate[1]:
                            temp.append(obs[1]-coordinate[1]-1)
                    if temp!=[] and min(temp)<item:
                        coordinate[1] += min(temp)
                    else:
                        coordinate[1] += item

                elif direction=='Y-':
                    temp = []
                    for obs in obstacles:
                        if obs[0]!=coordinate[0]:
                            continue
                        elif obs[1]<coordinate[1]:
                            temp.append(-obs[1]+coordinate[1]-1)
                    if temp!=[] and min(temp)<item:
                        coordinate[1] -= min(temp)
                    else:
                        coordinate[1] -= item

                elif direction=='X+':
                    temp = []
                    for obs in obstacles:
                        if obs[1]!=coordinate[1]:
                            continue
                        elif obs[0]>coordinate[0]:
                            temp.append(obs[0]-coordinate[0]-1)
                    if temp!=[] and min(temp)<item:
                        coordinate[0] += min(temp)
                    else:
                        coordinate[0] += item

                else:
                    temp = []
                    for obs in obstacles:
                        if obs[1]!=coordinate[1]:
                            continue
                        elif obs[0]<coordinate[0]:
                            temp.append(-obs[0]+coordinate[0]-1)
                    if temp!=[] and min(temp)<item:
                        coordinate[0] -= min(temp)
                    else:
                        coordinate[0] -= item

            max_distance = max(max_distance, coordinate[0]**2+coordinate[1]**2)
        return max_distance
'''

### 网友解答
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 北、东、南、西 （用字典类型，合适！）
        x, y = 0, 0  # 机器人的当前位置
        direction_index = 0  # 当前朝向的索引
        max_distance = 0  # 最大欧式距离的平方
        obstacle_set = set(map(tuple, obstacles))  # 将障碍物列表转换为集合，以便快速查找 (因为集合可以删掉重复元素?)

        for cmd in commands:
            if cmd == -2:  # 向左转 90 度
                direction_index = (direction_index - 1) % 4  # （避免判断，比较巧妙！）
            elif cmd == -1:  # 向右转 90 度
                direction_index = (direction_index + 1) % 4
            else:  # 向前移动 cmd 个单位
                for _ in range(cmd):
                    next_x, next_y = x + directions[direction_index][0], \
                    y + directions[direction_index][1]
                    if (next_x, next_y) in obstacle_set:  # 遇到障碍物，停止移动  （一小步小步走，同时判断障碍物）
                        break                             # （后面赋值更新操作也无需执行，不更新位置，不计算距离平方）
                    x, y = next_x, next_y  # 更新机器人的位置
                    max_distance = max(max_distance, x**2 + y**2)  # 更新最大欧式距离的平方

        return max_distance

### 官方解答
    
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        px, py, d = 0, 0, 1
        mp = set([tuple(i) for i in obstacles])   # 哈希表存储每一个障碍物放置点
        res = 0
        for c in commands:
            if c < 0:
                d += 1 if c == -1 else -1
                d %= 4
            else:
                for i in range(c):
                    if tuple([px + dirs[d][0], py + dirs[d][1]]) in mp:
                        break
                    px, py = px + dirs[d][0], py + dirs[d][1]
                    res = max(res, px * px + py * py)
        return res
