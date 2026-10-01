def water(min, max):
    average = (int(min) + int(max))/2
    desire = input("how many gallons: ")
    time_to_fill = desire/average
    print(str(time_to_fill), "minutes")

water(1, 3)