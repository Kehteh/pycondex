def red_light_camera(light_colour: str, car_detected: bool):
    if light_colour == "Red" and car_detected == True:
        return True
    else:
        return False
print(red_light_camera("Green", False))
    
