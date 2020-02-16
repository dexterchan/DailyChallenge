
#Given a list of building in the form of (left, right, height), return what the skyline should look like.
# The skyline should be in the form of a list of (x-axis, height),
# where x-axis is the next point where there is a change in height starting from 0,
# and height is the new height starting from the x-axis.

#Here's some starter code:
#Analysis
#Prepare a long array as foundation, for building.... say 100, f=[0]*100
#read input (x,y,h)
#construct building and find boundary (s,e) = (100,0) <-init
#s = min(s,x-1)
#e = max(e,y)
# for i in range(x-1,y):
#   f[i] = f[i]+h
# IN the end, scan the "city" from s to e
# lvl = 0
# res = []
# for i in range(s,e):
#   if lvl != h[i]:
#       lvl = j[i]
#       res.append((i+1,lvl))

DIM = 1000

def generate_skyline(buildings):
    # Fill this in.
    f = [0] * DIM
    s,e = (DIM, 0)
    for (x, y ,h) in buildings:
        s = min(s,x-1)
        e = max(e, y+1)
        for i in range(x-1, y):
            f[i] = max(h, f[i])
    lvl = 0
    res = []
    for i in range(s, e):
        if lvl != f[i]:
            lvl = f[i]
            res.append((i+1, lvl))
    return res

if __name__ == "__main__":
    #            2 2 2
    #            2 2 2
    #        1 1 2 2 2 1 1
    #        1 1 2 2 2 1 1
    #        1 1 2 2 2 1 1
    # pos: 1 2 3 4 5 6 7 8 9
    print (generate_skyline([(2, 8, 3), (4, 6, 5)]))
    # [(2, 3), (4, 5), (7, 3), (9, 0)]