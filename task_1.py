def exercise1():
    fruits = ("banana", "apple", "strawberry", "banana")
    nameOfFruit = input("Name of fruit: ")
    if nameOfFruit in fruits:
        print("yes")
    else:
        print("no")

def exercise2():
    fruits = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
    nameOfFruit = input("Name of fruit: ")
    numOfFruit=0
    for fruit in fruits:
        if nameOfFruit in fruit:
            numOfFruit+=1
    print(f"{nameOfFruit} occurs in list {numOfFruit} times")

cars = ("Mazda", "Audi", "Ford", "Tesla")
def exercise3():
    global cars
    nameOfCar = input("Name of car: ")

    if nameOfCar in cars:
        newName = input("Name of new car instead of previous one: ")
        carsList=list(cars)
        for i in range(len(carsList)):
            if carsList[i]==nameOfCar:
                carsList[i]=newName
            
        cars = tuple(carsList)
        print(f"New cars: {cars}")
    else:
        print(f"{nameOfCar} is not in list of cars")
        print(f"Cars: {cars}")

def exercise4():
    numbers=(324, 123, 76, 98765, 10)
    for i, number in enumerate(numbers):
        count=len(str(number))
        print(f"{i+1} number has {count} chars")


a = True
while a:
    numOfExercise=int(input("Enter number of exercise (0-exit): "))
    if numOfExercise==1:
        exercise1()
    elif numOfExercise==2:
        exercise2()
    elif numOfExercise==3:
        exercise3()
    elif numOfExercise==4:
        exercise4()
    elif numOfExercise==0:
        a=False
    else:
        print("Error")


