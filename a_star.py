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

class hash_maps():
    def __init__(self):
        self.visited_map = np.zeros((int(250*_CONST.scale),int(400*_CONST.scale),12),dtype='uint16')
        self.cost_to_come_map = np.ones((int(250*_CONST.scale),int(400*_CONST.scale)),dtype=float)*1000
        self.cost_to_go_map = np.ones((int(250*_CONST.scale),int(400*_CONST.scale)),dtype=float)*1000
        self.my_map = np.zeros((np.int(250*_CONST.scale),np.int(400*_CONST.scale),3),dtype='uint8')



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

        cost_to_goal = np.sqrt(((_CONST.x_g- x_current)**2)+((_CONST.y_g - y_current)**2))
        print(cost_to_goal)
        return cost_to_goal

def calculate_cost_to_come(node):

    pass
class robot():
    def __init__(self,x_pos,y_pos,theta):
        self.x = x_pos
        self.y = convert_to_cv(y_pos)
        self.theta = theta



def a_star(start_node,goal_node,my_map):
    
    pass

# class user_inputs():
#     def __init__(self,x_s,y_s,theta_s,x_g,y_g,theta_g,step_size,clearance,robot_radius):
#         self.start_node = nodes(x_s,y_s,theta_s)
#         self.goal_node = nodes(x_g,y_g,theta_g)
#         self.clearance = clearance
#         self.step_size = step_size
#         self.robot_radius = robot_radius
        

def main():

    my_hasmaps = hash_maps()
    my_map = my_hasmaps.my_map
    obstacle_color = [255,255,255]
    tolerance_map = PopulateMap(my_map,obstacle_color,5,2)
    obstacle_map = PopulateMap(my_map,obstacle_color,0,2)
    my_map = cv.addWeighted(tolerance_map, 0.5, obstacle_map, 1, 0)


    start_node = nodes(_CONST.x_s,_CONST.y_s,_CONST.theta_s)
    goal_node = nodes(_CONST.x_g,_CONST.y_g,_CONST.theta_g)
    if check_validity_position(start_node,my_map):
        if check_validity_position(goal_node,my_map):
            a_star(start_node,goal_node,my_map)
            # print("corrent nodes")
        else:
            print("Incorrect Nodes")
    else:
        print("Incorrect Nodes")

if __name__ == '__main__':
    main()
    # test()