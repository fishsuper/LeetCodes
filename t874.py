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

