# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, right, down, left

    def cleanRoom(self, robot):
        visited = set()
        self.dfs(0, 0, 0, visited, robot)

    def dfs(self, x, y, theta, visited, robot):
        """
        Since we don't know the real coordinates, this x, y have an offset to the real coordinates.
        But it does not affect the final result.
        """
        robot.clean()
        visited.add((x, y))

        for i in range(4):
            new_theta = theta + i
            new_x = x + self.directions[new_theta % 4][0]
            new_y = y + self.directions[new_theta % 4][1]

            if (new_x, new_y) not in visited and robot.move():
                self.dfs(new_x, new_y, new_theta, visited, robot)
                # go back to previous cell and maintain the same orientation
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            robot.turnRight()

