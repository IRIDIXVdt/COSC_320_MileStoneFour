import random
#map size(x*y)
rangeX = 10 
rangeY = 10
qty = 5  # or however many points you want
#random vertex
openfile = open('file.txt','w')
for x in random.sample(range(rangeX*rangeY),qty):
    openfile.write(str('{},{}'.format(*divmod(x,rangeX)))+ '\n')
    #print('{},{}'.format(*divmod(x,rangeX)))

openfile.close()
cell_array = [[]]
with open('file.txt','r') as file:
    line_array = file.read().splitlines()
    cell_array = [line.split(',') for line in line_array]

    #print (cell_array)
cell_array2 = [list(map (int,i)) for i in cell_array]
print (cell_array2)
