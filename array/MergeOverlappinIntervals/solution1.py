
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    mergedInterverals = []
    currentIntervals = sortedIntervals[0]
    mergedInterverals.append(currentIntervals)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentIntervals
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentIntervals[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentIntervals = nextInterval
            mergedInterverals.append(currentIntervals)
    
    return mergedInterverals