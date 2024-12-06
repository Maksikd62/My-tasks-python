#tasks about sets
# citiesMain1={"Rivne", "Krakiv", "Kyiv", "Lviv", "Poltava", "New York", "Los Angeles", "Mykolaiv", "Donetsk", "Odessa"}

# citiesMain2={"Rome", "London", "Paris", "Berlin", "Rivne", "Krakiv", "Kyiv", "Lviv"}

# print(f"Intersection: {citiesMain1.intersection(citiesMain2)}")
# print(f"Difference_1: {citiesMain1.difference(citiesMain2)}")
# print(f"Difference_2: {citiesMain2.difference(citiesMain1)}")
# print(f"Symetric Difference: {citiesMain1.symmetric_difference(citiesMain2)}")

#tasks about generators

#exercise1
print("Exercise 1")
def oddNumbers(numOfStart, numOfEnd):
    for num in range(numOfStart, numOfEnd+1):
        if num%2!=0:
            yield num

start=0
end=0
while start>=end:
    start=int(input("Enter start of range: "))
    end=int(input("Enter end of range: "))
    if start>end:
        print("Start of range more than end. Try again")
    elif start==end:
        print("Start is equal to end. Try again")
        
for num in oddNumbers(start, end):
    print(num)

print("--------------------")
print("Exercise 2")

#exercise2
def otherNumbers(numbers, numOfStart, numOfEnd):
    for num in numbers:
        if num<numOfStart or num>numOfEnd:
            yield num

start=0
end=0
while start>=end:
    start=int(input("Enter start of range: "))
    end=int(input("Enter end of range: "))
    if start>end:
        print("Start of range more than end. Try again")
    elif start==end:
        print("Start is equal to end. Try again")

numbers={2, 3, 8, 19, 24, 55, 78, 123}
for num in otherNumbers(numbers, start, end):
    print(num)



