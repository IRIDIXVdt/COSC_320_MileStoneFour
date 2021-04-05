import random
import math
class Graph:
    def __init__(self,rangeX,rangeY,qty):
        self.rangeX = rangeX
        self.rangeY = rangeY
        self.qty = qty
    
    def randomVertex(self,rangeX,rangeY,qty):
        openfile = open('file.txt','w')
        for x in random.sample(range(self.rangeX*self.rangeY),self.qty):
            openfile.write(str('{},{}'.format(*divmod(x,self.rangeX)))+ '\n')
        openfile.close()
        cell_array = [[]]
        with open('file.txt','r') as file:
            line_array = file.read().splitlines()
            cell_array = [line.split(',') for line in line_array]
            
        cell_array2 = [list(map (int,i)) for i in cell_array]
        return cell_array2

    