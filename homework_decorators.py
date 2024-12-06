import time
#decorators (homework1)
def allTime(func):
    def difference():
        startTime=time.time()
        result=func()
        endTime=time.time()
        differenceTime=endTime-startTime
        return differenceTime, result
    return difference

@allTime
def numbers():
    evenNumbers=[]
    for num in range(1, 100000):
        if num%2==0:
            evenNumbers.append(num)
    return evenNumbers

timeForFunc, evenNumbers = numbers()
print(evenNumbers)
print("Time for function: "+ str(timeForFunc))