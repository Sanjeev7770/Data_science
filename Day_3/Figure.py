import math

def volume_cylinder(radius,height_cylinder):
    return math.pi*radius**2*height_cylinder

def volume_cone(radius,height_cone):
    return (math.pi*radius**2*height_cone)/3

radius=float(input('enter the radius'))
height_cylinder=float(input('enter the height of cylinder'))
height_cone=float(input('enter the height of cone'))


volumeofcylinder=volume_cylinder(radius,height_cylinder)
volumeofcone=volume_cone(radius,height_cone)
totalvolume=volumeofcylinder+volumeofcone

print(f'the total volume of cylinder and cone are{totalvolume}')






