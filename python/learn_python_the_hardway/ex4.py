cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driver = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
avg_pass = passengers / cars_driven

print ("There are ",cars, "cars available.")
print("There are only" , drivers, "drivers available.")
print("There will be",cars_not_driver,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",avg_pass,"in each car.")