import datetime

class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    def __init__(self, distance):
        """Initializes the Distance object with distance and timestamp."""
        self.distance = float(distance)
        self.time = datetime.datetime.now().time().strftime('%H:%M:%S')   # Stores HH:MM:SS format

    def __str__(self):
        """Returns a formatted string representation of the Distance object."""
        return f'Distance from wall: {self.distance:.3f} cm | Time: {self.time}'
