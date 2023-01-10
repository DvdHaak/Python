def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  if city == "Tampa":
    return 220
  if city == "Pittsburgh": 
    return 222
  if city == "Los Angeles": 
    return 475

def rental_car_cost(days):
  day_price = 40
  total_price = days * day_price
  if days >= 3:
    total_price -= 20
    return total_price

  elif days >= 7:
    total_price -= 50
    return total_price


def trip_cost(city, days):
    sum(rental_car_cost(days), hotel_cost(days - 1), plane_ride_cost(city))
input()