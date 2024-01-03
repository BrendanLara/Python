# Final Exam Problem

# Implement a class named Sprite with the following properties and behaviors. A Sprite object (similar to what you experienced
# in Scratch) has an x-coordinate and a y-coordinate that indicates its current location in a two-dimensional grid.
# The sprite's initial x and y coordinates are specified in the constructor,  along with its initial direction.
# The only allowable values for direction are 0, 90, 180 and 270. These represent the angles in 360-degree circle (like a compass),
# with 0 degrees being north, 90 being east, 180 being south, 270 being west.  The constructor should verify that the direction supplied
# by the user is one of the four valid choices; if it is not, an error message should be output, and the initial direction should be set
# to zero.
# The three instance variables should be named in such a way that they are "private" to the class.
#
# Write an instance method named move(n) that simulates the sprite moving n pixels in whatever direction it is facing.
#
# Write an additional instance method turn_right() that causes the sprite to turn 90 degrees to the right.
#
# Finally, define the method __str__so that information about a sprite can printed.


class Sprite:
    def __init__(self, x, y, d):
        self.x_coordinate = x
        self.y_coordinate = y
        self.direction = d

        if self.direction != 0 and self.direction != 90 and self.direction != 180 and self.direction != 270:
            print('error: direction must be 0, 90, 180, or 270. Setting direction to 0')
            self.direction = 0

        def move(self, n):
            if self.direction == 0:
                self.y_coordinate += n
            if self.direction == 90:
                self.x_coordinate += n
            if self.direction == 180:
                self.y_coordinate -= n
            if self.direction == 270:
                self.x_coordinate -= n

        def turn_right(self):
            if self.direction == 270:
                self.direction = 0
            else:
                self.direction += 90

        def __str__(self):
            if self.direction == 0:
                heading = 'north'
            if self.direction == 90:
                heading = 'east'
            if self.direction == 180:
                heading = 'south'
            if self.direction == 270:
                heading = 'west'

            return 'Sprite is at location (' + str(self.x_coordinate) + ',' + str(
                self.y_coordinate) + 'and is facing' + heading