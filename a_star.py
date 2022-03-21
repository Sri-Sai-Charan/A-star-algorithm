#usr/bin/python3

import numpy as np
import cv2 as cv

from utils import *


class _CONST():
    ##############################
    # USER INPUTS
    ##############################
    x_s = 10
    y_s = 10
    theta_s = 30
    clearance = 5
    robot_radius = 5
    x_g = 20
    y_g = 20
    theta_g = 30
    step_size = 10
    scale = 2
    ##############################
    # END OF USER INPUTS
    ##############################
    def __setattr__(self, *_):
        pass

class _GLOBAL():
    parent_map = np.zeros((250*_CONST.scale,400*_CONST.scale,2),dtype='uint16')
    cost_to_come_map = np.ones((int(250*_CONST.scale),int(400*_CONST.scale)),dtype=float)*1000
    visited_map = np.zeros((int(250*_CONST.scale),int(400*_CONST.scale),12),dtype='uint16')
    my_map = np.zeros((np.int(250*_CONST.scale),np.int(400*_CONST.scale),3),dtype='uint8')
    open_nodes = []
    
def set_obstacle_space():
    obstacle_color = [255,255,255]
    tolerance_map = PopulateMap(_GLOBAL.my_map,obstacle_color,5,2)
    obstacle_map = PopulateMap(_GLOBAL.my_map,obstacle_color,0,2)
    _GLOBAL.my_map = cv.addWeighted(tolerance_map, 0.5, obstacle_map, 1, 0)

def check_validity_position(node):
    if not (node.x > 249 | node.y > 399) :
        if(int(_GLOBAL.my_map[node.x,node.y,1])>127):
            return False
        else:
            return True
    else:
        return False



class nodes():
    def __init__(self,x_pos,y_pos,theta):
        self.x = x_pos
        self.y = y_pos
        self.cost_to_come = np.inf
        self.parent = [0,0]
        self.cost_to_goal = self.calculate_cost_to_goal(x_pos,y_pos)
        self.theta = theta
        self.total_cost = self.calculate_totalcost()

    def calculate_totalcost(self):
        if not (self.cost_to_come == np.inf ):
            self.total_cost = self.cost_to_come + self.cost_to_goal
            return self.total_cost
        else:
            return np.inf

    def calculate_cost_to_goal(self,x_current,y_current):

        self.cost_to_goal = np.sqrt(((_CONST.x_g- x_current)**2)+((_CONST.y_g - y_current)**2))
        return self.cost_to_goal

def calculate_cost_to_come(node):

    pass
class robot():
    def __init__(self,x_pos,y_pos,theta):
        self.x = x_pos
        self.y = convert_to_cv(y_pos)
        self.theta = theta

def check_future_state(current,my_map,my_lists,path_map):
    actions = action()
    
    for ite in range(8):
        move = [0,0]
        move[0] = current.position[0] + actions.action_sets[ite][0]
        move[1] = current.position[1] + actions.action_sets[ite][1]
        cost = 0
        cost = current.cost + actions.cost[ite]
        
        if (int(my_map[move[0],move[1],1])<127):
            
            future = nodes([0,0])
            # future.position = 
            future.cost = cost
            future.parent = current.position
            if not _GLOBAL.visited_map[future.x,future.y,ite]==1:
                my_lists.OpenNodes.append(future)
                path_map[future.position[0],future.position[1]]=[0,255,0]                

    my_lists.OpenNodes.pop(0) 
    my_lists.OpenNodes = sorted(my_lists.OpenNodes,key=lambda x: x.total_cost , reverse=False)

def set_goal(goal):
    for i in range(goal.x - 3*_CONST.step_size , goal.x + 3*_CONST.step_size ):
        for j in range(goal.y - 3*_CONST.step_size , goal.y + 3*_CONST.step_size ):
            if ((i - goal.x) **2 + (j - goal.y)**2)<= ((1.5*_CONST.step_size)**2):
                _GLOBAL.visited_map[i,j] = 2
    

def a_star(start_node,goal_node):
    current_node = start_node
    set_goal(goal_node)
    print(_GLOBAL.visited_map)
    while True:
        check_future_state(current_node)
        current_node = _GLOBAL.open_nodes[0]        
        if _GLOBAL.visited_map[current_node.x , current_node.y] == 2:
            break
            


def main():

    set_obstacle_space()
    start_node = nodes(_CONST.x_s,_CONST.y_s,_CONST.theta_s)
    goal_node = nodes(_CONST.x_g,_CONST.y_g,_CONST.theta_g)
    if check_validity_position(start_node):
        if check_validity_position(goal_node):
            a_star(start_node,goal_node)

        else:
            print("Incorrect Nodes")
    else:
        print("Incorrect Nodes")

if __name__ == '__main__':
    main()
    # test()