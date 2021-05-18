# exercise 01
class bus:
    def __init__(self, number_of_seats, color, driver):
        self.number_of_seats = number_of_seats
        self.color = color
        self.driver = driver

bus = bus(20, "yellow", "Grant")

print(bus.number_of_seats)
print(bus.color)
print(bus.driver)

# exercise 02

class buses:
    buses_count = 0
    def __init__(self, bus_number):
        self.bus_number = bus_number
        buses.buses_count += 1
bus1 = buses("bus1")
bus2 = buses("bus2")
bus3 = buses("bus3")

print (buses.buses_count)
