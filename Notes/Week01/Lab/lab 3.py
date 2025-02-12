import math

ice_cream = int(input("What is the number of ice cream scopes do you want?"))
ice_cream_radius = int(input("What is the radius of each ice cream scope?"))
cone_radius = int(input("What is the radius of the cone?"))
cone_height = int(input("What is the height of the cone?"))

ice_cream_volume = (float(((4/3) * 3.1416) * (ice_cream_radius ** 3))) * ice_cream
cone_volume = float(3.1416 * (cone_radius ** 2) * cone_height/3)

total_volume = ice_cream_volume + cone_volume

print("The total volume of your", ice_cream, "ice cream scopes is", total_volume, "cubic feet." )



