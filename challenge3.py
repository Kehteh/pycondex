def can_ride_rollercoaster(rider_height: float):
    """Only people who are over 120cm in height can ride the rollercoaster.
    
    Arguments:
        - rider_height: a float representing the height of the prospective rider in centimetres
        
    Returns: a boolean representing whether or not the prospective rider is allowed on the rollercoaster.
    """
    if rider_height >= float(120):
        return True
    else:
        return False
can_ride_rollercoaster(rider_height= float(150))