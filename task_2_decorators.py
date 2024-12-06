import time
def allTime(func):
    def difference():
        startTime=time.time()
        func()
        endTime=time.time()
        differenceTime=endTime-startTime
        return differenceTime
    return difference

@allTime
def numbers():
    evenNumbers=[]
    for num in range(1, 101):
        if num%2==0:
            evenNumbers.append(num)
    print(evenNumbers)

timeForFunc=numbers()
print("Time for function: "+ str(timeForFunc))