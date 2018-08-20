import pypot.dynamixel
import math
import time

ports = pypot.dynamixel.get_available_ports()

def pos(x,y):
    d = math.hypot(x, y)
    theta = math.degrees(math.atan2(y, x))
    alpha = math.acos(d/30)
    alpha = math.degrees(alpha)
    beta = math.acos(1 - ((d**2) / 450))
    beta = math.degrees(beta)
    return (alpha+theta) - 90, beta-180

def move(Dxl, x, y):
    ids = [1, 2]
    angs = pos(x, y)
    moves = {}
    j = 0
    for i in ids:
        moves[i] = angs[j]
        j += 1
    Dxl.set_moving_speed({1:1000, 2:1000})
    Dxl.set_goal_position(moves)
    print moves

dxl = pypot.dynamixel.DxlIO(ports[0])
# dxl.set_moving_speed({1:50, 2:50})
print(dxl.scan(range(5)))
dxl.set_goal_position({1:0,2:0})

# move(dxl, x-r, y)
# time.sleep(1)
# move(dxl, x, y+r)`
# time.sleep(1)
# move(dxl, x+r, y)
# time.sleep(1)
# move(dxl, x, y-r)
# time.sleep(1)
# move(dxl, x-r, y)
# while (i < x):
    # j = y + math.sqrt(r**2 - ((x-i)**2))
    # move(dxl, i, j)
    # time.sleep(0.2)
    # i += 0.01
# i = x
# while(i < x+r):
    # j = y + math.sqrt(r**2 - ((x-i)**2))`
    # move(dxl, i, j)
    # time.sleep(0.2)
    # i += 0.01

# i = x+r
# while(i > x):
    # j = y - math.sqrt(r**2 - ((x-i)**2))
    # move(dxl, i, j)
    # time.sleep(0.2)
    # i -= 0.01

# i = x
# while(i > x-r):
    # j = y - math.sqrt(r**2 - ((x-i)**2))
    # move(dxl, i, j)
    # time.sleep(0.2)
    # i -= 0.01
x = {}
y = {}
for i in range(4):
    x[i] = input()
    y[i] = input()

i  = x[0]
while(i < x[1]):
    move(dxl, i, y[0])
    time.sleep(0.2)
    i += 0.01
j = y[1]
while(j > y[2]):
    move(dxl, x[1], j)
    time.sleep(0.2)
    j -= 0.01
i = x[2]
while(i > x[3]):
    move(dxl, i, y[2])
    time.sleep(0.2)
    i -= 0.01
j = y[3]
while(j < y[0]):
    move(dxl, x[3], j)
    time.sleep(0.2)
    j += 0.01
