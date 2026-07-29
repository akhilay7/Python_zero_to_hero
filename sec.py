def sectorarea():
    pi = new_func()
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    sur_area = (pi*radius**2) * (angle/360)
    print("Sector Area: ", sur_area)

def new_func():
    pi=22/7
    return pi

sectorarea()