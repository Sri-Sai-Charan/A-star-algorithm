#usr/bin/python3

import numpy as np
import cv2 as cv

class hash_maps():
    def __init__(self):
        visited_map = np.zeros((250,400,12),dtype='uint16')
        cost_to_come_map = np.ones((250,400),dtype=float)*1000
        cost_to_go_map = np.ones((250,400),dtype=float)*1000

class action():
    def __init__(self):
        self.action_sets= [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,1),(1,-1),(-1,-1)]
        self.cost = [1,1,1,1,1.4,1.4,1.4,1.4]

class nodes():
    def __init__(self,x_pos,y_pos,theta):
        self.x = x_pos
        self.y = y_pos
        self.cost_to_come = np.inf
        self.parent = [0,0]
        self.cost_to_go = np.inf
        self.theta = theta

class robot():
    def __init__(self,x_pos,y_pos,theta):
        self.x = x_pos
        self.y = y_pos
        self.theta = theta

def calculate_cost_to_goal(node,goal):
    x_current = node.x
    y_current = node.y
    x_goal = goal.x
    y_goal = goal.y
    cost_to_goal = np.sqrt(((x_goal - x_current)**2)+((y_goal - y_current)**2))
    print(cost_to_goal)

def a_start(start_node,goal_node):
    
    pass

def main():
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

    ##############################
    # END OF USER INPUTS
    ##############################
    # a_star()
    start_node = nodes(x_s,y_s,theta_s)
    goal_node = nodes(x_g,y_g,theta_g)
    a_start(start_node,goal_node)

    pass
if __name__ == '__main__':
    main()