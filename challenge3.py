def can_ride_rollercoaster(rider_height: float):
    if rider_height > float(120):
        return True
    else:
        return False
print(can_ride_rollercoaster(rider_height= 120))
