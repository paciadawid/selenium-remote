destination_city = "Chartum"

destinations = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Chartum": "not exists"
}

distance = destinations[destination_city]

if type(distance) != int:
    raise Exception

cost = 2 * distance
if distance < 2000:
    cost += 100

print(f"Total cost is {cost}")