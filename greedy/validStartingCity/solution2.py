# Time: O(N), Space: O(1)
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    numberOfCities = len(distances)
    milesRemaining = 0
    indexOfStartingCity = 0
    milesRemainingAtStartingCity = 0

    for idx in range(1, numberOfCities):
        distanceFromPreviousCity = distances[idx - 1]
        fuelFromAvailable = fuel[idx - 1]
        milesRemaining += fuelFromAvailable * mpg - distanceFromPreviousCity
        if milesRemainingAtStartingCity > milesRemaining:
            milesRemainingAtStartingCity = milesRemaining
            indexOfStartingCity = idx

    return indexOfStartingCity
