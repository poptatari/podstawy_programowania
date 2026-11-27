# This program defines a class C that stores a list of 2D 
# point coordinates (x, y) on a plane. Its m(n) method counts 
# how many of those points lie in the first quadrant—where both x 
# and y are greater than zero—and returns True if that count is 
# at least n, or False otherwise.

class C:
    def __init__(self, points):
        self.points = points

    def m(self, n: int) -> bool:
        count = 0
        for point in self.points:
            x = point[0]
            y = point[1]
            if x > 0 and y > 0:
                count += 1
        return count >= n

def main():
    obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
    print(obj.m(2))
    print(obj.m(3))

if __name__ == '__main__':
    main() 