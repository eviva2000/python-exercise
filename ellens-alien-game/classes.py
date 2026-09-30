"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """
    
    total_aliens_created = 0

    def __init__(self, location):
        self.x_coordinate = location[0]
        self.y_coordinate = location[1]
        self.health = 3
        Alien.total_aliens_created += 1


def new_aliens_collection(coordinates):
    return [Alien(location) for location in coordinates]

    
