"""
The idea is to simply find the city that we enter with the   least
amount of gas overall. There is guaranteed to be such a city,
and it is guaranteed that the gas amount will be minimal.
This will be the case if we travel there from ANY city and means we can't
reach this city if we start from other cities, therefore it must be the city
we have to start at because if we start there, we can get back there and if we get back there,
we were able to reach ALL of the other cities.

Imagine you have a set of cities that are laid out in a circle, connected by a
  circular road that runs clockwise. Each city has a gas station that provides
  gallons of fuel, and each city is some distance away from the next city.
  You have a car that can drive some number of miles per gallon of fuel, and
  your goal is to pick a starting city such that you can fill up your car with
  that city's fuel, drive to the next city, refill up your car with that city's
  fuel, drive to the next city, and so on and so forth until you return back to
  the starting city with 0 or more gallons of fuel left.
  This city is called a valid starting city, and it's guaranteed that there will
  always be exactly one valid starting city.
  For the actual problem, you'll be given an array of distances such that city
  i is distances[i] away from city i + 1.
  Since the cities are connected via a circular road, the last city is connected
  to the first city. In other words, the last distance in the
  distances array is equal to the distance from the last city to
  the first city. You'll also be given an array of fuel available at each city,
  where fuel[i] is equal to the fuel available at city
  i. The total amount of fuel available (from all cities combined)
  is exactly enough to travel to all cities. Your fuel tank always starts out
  empty, and you're given a positive integer value for the number of miles that
  your car can travel per gallon of fuel (miles per gallon, or MPG). You can
  assume that you will always be given at least two cities.

Write a function that returns the index of the valid starting city.
Sample Input
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
Sample Output:
    4
"""


# Time: O(M), Space: O(1)
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    milesLeft = 0
    minGaz = 0
    minCity = 0
    for city in range(len(distances)):
        milesLeft = (milesLeft + (mpg * fuel[city])) - distances[city]
        if milesLeft < minGaz:
            minGaz = milesLeft
            minCity = (city + 1 % len(distances))
    return minCity


def test1():
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    assert validStartingCity(distances, fuel, mpg) == 4


if __name__ == "__main__":
    test1()
