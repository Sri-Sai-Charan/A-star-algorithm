#usr/bin/python3

import numpy as np
import cv2 as cv

def half_planes(my_map,point1,point2,obstacle_color,upper):
    m = (point2[0]-point1[0])/(point2[1]-point1[1]+(1e-6))
    temp=np.zeros_like(my_map)
    for y  in range(my_map.shape[1]):
        c = point1[0] - m*point1[1]
        for x in range(my_map.shape[0]):
            if upper :
                if (y <= ((m*x)+c)):
                    temp[x,y]= obstacle_color
            else:
                if (y >= ((m*x)+c)):
                    temp[x,y]= obstacle_color
    return temp

class action():
    def __init__(self):
        self.action_sets= [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,1),(1,-1),(-1,-1)]
        self.cost = [1,1,1,1,1.4,1.4,1.4,1.4]

def map_thetas(i):
    pass

def PopulateMap(my_map,obstacle_color,tolerance=0,scale=2):

    #Circle
    circle_map = np.zeros_like(my_map)
    # for i in range(24 - tolerance, 104 + tolerance):
    #     for j in range(254 - tolerance, 344 + tolerance):
    #         if (i - 64) **2 + (j - 299)**2 <= (40+tolerance)**2:
    #             circle_map[i,j] = obstacle_color
    for i in range(my_map.shape[0]):
        for j in range(my_map.shape[1]):
            if ((i - (64*scale)) **2 + (j - (299*scale))**2)<= ((40+tolerance)**2)*scale:
                circle_map[i,j] = obstacle_color

    #Hexagon
    hexagon_map = np.zeros_like(my_map)    
      
    hexagon_pts= np.array([[164 - tolerance*1.2 ,170 + tolerance], 
                            [199,190+tolerance*1.6],    
                            [234 +tolerance,170+tolerance], 
                            [234 +tolerance,130 -tolerance], 
                            [199,110 - tolerance*1.2], 
                            [164 - tolerance,130 - tolerance]],np.int32)      

    hexagon_pts= hexagon_pts*scale     
    # print(hexagon_pts)
    side1=half_planes(hexagon_map,hexagon_pts[0],hexagon_pts[1],obstacle_color,False)
    side2=half_planes(hexagon_map,hexagon_pts[1],hexagon_pts[2],obstacle_color,True)
    side2 = cv.bitwise_and(side2,side1)
    side3=half_planes(hexagon_map,hexagon_pts[2],hexagon_pts[3],obstacle_color,True)
    side4=half_planes(hexagon_map,hexagon_pts[3],hexagon_pts[4],obstacle_color,True)
    side5=half_planes(hexagon_map,hexagon_pts[4],hexagon_pts[5],obstacle_color,False)
    side5=cv.bitwise_and(side5,side4)
    side6=half_planes(hexagon_map,hexagon_pts[5],hexagon_pts[0],obstacle_color,False)
    side6 = cv.bitwise_and(side3,side6)
    my_map = cv.bitwise_and(side2,side5)
    hexagon_map = cv.bitwise_and(my_map,side6)

    #Other Obstace
    other_obstacle_map = np.zeros_like(my_map)  
    other_obstacle= np.array([[34 - (tolerance*2.5) ,64 - tolerance*0.6  ], 
                                [104 + tolerance*2,149 + (tolerance*4)], 
                                [89 + tolerance,69 + tolerance ], 
                                [114 + (tolerance*3),39 - (tolerance*(2))]],np.int32)

    other_obstacle = other_obstacle*scale

    side1=half_planes(other_obstacle_map,other_obstacle[0],other_obstacle[1],obstacle_color,False)
    side2=half_planes(other_obstacle_map,other_obstacle[1],other_obstacle[3],obstacle_color,True)
    side3=half_planes(other_obstacle_map,other_obstacle[3],other_obstacle[0],obstacle_color,False)
    side2 = cv.bitwise_and(side1,side2)
    side3 = cv.bitwise_and(side3,side2)
    mask1 = half_planes(other_obstacle_map,other_obstacle[1],other_obstacle[2],obstacle_color,True)
    mask2 = half_planes(other_obstacle_map,other_obstacle[2],other_obstacle[3],obstacle_color,True)
    mask3 = half_planes(other_obstacle_map,other_obstacle[3],other_obstacle[1],obstacle_color,False)
    mask1 = cv.bitwise_or(mask2,mask1)
    mask3 = cv.bitwise_or(mask3,mask1)
    other_obstacle_map=cv.bitwise_and(mask3,side3)
    my_map = cv.bitwise_or(other_obstacle_map,hexagon_map)
    my_map = cv.bitwise_or(my_map,circle_map)

    #Border
    my_map[0:tolerance*scale,:]= [128,128,128]
    my_map[:,my_map.shape[1] - (tolerance*scale) :my_map.shape[1]]=[128,128,128]
    my_map[my_map.shape[0]-(tolerance*scale):my_map.shape[0],:]=[128,128,128]
    my_map[:,0:tolerance*scale] = [128,128,128]

    return my_map.copy()

def convert_to_cv(y,y_max):
    y = abs((y-y_max))
    return y






class Matrix: 

  def __init__(self, dims, fill):    
     self.rows = dims[0]  
     self.cols = dims[1]   
     self.A = [[fill] * self.cols for i in range(self.rows)]

# class action():
#     def __init__(self):
#         self.action_sets= [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,1),(1,-1),(-1,-1)]
#         self.cost = [1,1,1,1,1.4,1.4,1.4,1.4]





# class hash_maps():
#     def __init__(self):
        # self.visited_map = np.zeros((int(250*_CONST.scale),int(400*_CONST.scale),12),dtype='uint16')
        # self.cost_to_come_map = np.ones((int(250*_CONST.scale),int(400*_CONST.scale)),dtype=float)*1000
        # self.cost_to_go_map = np.ones((int(250*_CONST.scale),int(400*_CONST.scale)),dtype=float)*1000
        # self.my_map = np.zeros((np.int(250*_CONST.scale),np.int(400*_CONST.scale),3),dtype='uint8')







# from a_star import *
# import random



# def testing_random_cases():
#     global visited_map 
#     global cost_map 
#     global parent_map 
#     for ite in range(100):
#         start_x = random.randint(1,249)
#         start_y = random.randint(1,399)
#         goal_x =  random.randint(1,249)
#         goal_y = random.randint(1,399)

#         visited_map = np.zeros((250,400),dtype='uint16')
#         cost_map = np.ones((250,400),dtype=float)*1000
#         parent_map = np.zeros((250,400,2),dtype='uint16')
#         my_map = np.zeros((250,400,3),dtype='uint8')
#         my_map = np.zeros((250,400,3),dtype='uint8')
#         obstacle_color = [255,255,255]
#         tolerance_map = PopulateMap(my_map,obstacle_color,5)
#         obstacle_map = PopulateMap(my_map,obstacle_color)
#         my_map = cv.addWeighted(tolerance_map, 0.5, obstacle_map, 1, 0)
#         start_node = nodes([start_x,start_y])
#         start_node.cost = 0
#         start_node.parent = [None,None]
#         goal_node = nodes([goal_x,goal_y])
#         cost_map[start_x,start_y] = 0.0
#         visited_map[start_x,start_y] = 1
#         parent_map[start_x,start_y] = [start_x,start_y]
#         print("Start Node :",start_x,start_y, "Goal Node :",goal_x,goal_y)
#         if check_validity_position(start_node,my_map):
#             if check_validity_position(goal_node,my_map):
#                 DijkstraAlogrithm(start_node,goal_node,my_map)
#             else:
#                 print("Invalid Goal Position")                
#         else:
#             print("Invalid Start Position")
