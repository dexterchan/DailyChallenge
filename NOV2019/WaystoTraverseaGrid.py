
#You 2 integers n and m representing an n by m grid,
#determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

#Example:
#n = 2, m = 2

#This should return 2, since the only possible routes are:
#Right, down
#Down, right.


class Route:
    def __init__(self, x, y, lastdirection):
        self.coor = (x, y)
        self.trydown = False
        self.tryright = False
        self.lastdrct = lastdirection
        self.prev = None

    def move_right(self, boundary):
        self.tryright = True
        newX = self.coor[0] + 1
        if newX >= boundary[0]:
            return None
        else:
            newRoute = Route(newX, self.coor[1], "right")
            newRoute.prev = self
            return  newRoute

    def move_down (self, boundary):
        self.trydown = True
        newY = self.coor[1] + 1
        if newY >= boundary[1]:
            return None
        else:
            newRoute = Route (self.coor[0], newY, "down")
            newRoute.prev = self
            return newRoute
    def exhaustAllDirection(self):
        return self.trydown and self.tryright

    def printTrace (self):
        r = self
        while r is not None:
            print("x:%d y:%d, direction:%s"%(r.coor[0],r.coor[1],r.lastdrct))
            r = r.prev





class Solution:

    def calculate_num_ways_from_Topleft_to_Bottomright(self, n, m):
        routestack = []
        successRoutes = []
        boundary = (n, m)
        #Start
        start = Route(0,0, None)
        dest = (n-1, m-1)
        routestack.append(start)

        while len(routestack) != 0:
            r = routestack[-1]
            if r.coor == dest:
                successRoutes.append(r)
                routestack.pop()
                continue
            elif r.exhaustAllDirection():
                routestack.pop()
                continue

            if not r.trydown:
                newRoute = r.move_down(boundary)
                if newRoute is not None:
                    routestack.append(newRoute)
            elif not r.tryright:
                newRoute = r.move_right(boundary)
                if newRoute is not None:
                    routestack.append(newRoute)

        return successRoutes


def num_ways(n, m):
    # Fill this in.
    solu = Solution()
    successRoutes = solu.calculate_num_ways_from_Topleft_to_Bottomright(n, m)

    for r in successRoutes:
        r.printTrace()
        print("---")
    return len(successRoutes)

if __name__ == "__main__":
    print (num_ways(2, 2))
    # 2

    print (num_ways(9, 8))
