import math

# Function for Cube
def cube(side):
    surface_area = 6 * side * side
    volume = side ** 3
    return surface_area, volume

# Function for Cylinder
def cylinder(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius * radius * height
    return surface_area, volume

# Function for Cone
def cone(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    surface_area = math.pi * radius * (radius + slant_height)
    volume = (1/3) * math.pi * radius * radius * height
    return surface_area, volume

# Function for Cuboid
def cuboid(length, width, height):
    surface_area = 2 * (length * width + width * height + length * height)
    volume = length * width * height
    return surface_area, volume

# Main Program
print("SURFACE AREA AND VOLUME CALCULATOR")
print("1. Cube")
print("2. Cylinder")
print("3. Cone")
print("4. Cuboid")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side = float(input("Enter side of cube: "))
    sa, vol = cube(side)
    print("Surface Area of Cube =", sa)
    print("Volume of Cube =", vol)

elif choice == 2:
    radius = float(input("Enter radius of cylinder: "))
    height = float(input("Enter height of cylinder: "))
    sa, vol = cylinder(radius, height)
    print("Surface Area of Cylinder =", sa)
    print("Volume of Cylinder =", vol)

elif choice == 3:
    radius = float(input("Enter radius of cone: "))
    height = float(input("Enter height of cone: "))
    sa, vol = cone(radius, height)
    print("Surface Area of Cone =", sa)
    print("Volume of Cone =", vol)

elif choice == 4:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    sa, vol = cuboid(length, width, height)
    print("Surface Area of Cuboid =", sa)
    print("Volume of Cuboid =", vol)

else:
    print("Invalid Choice")