import time
# countries={"USA":"Washington", "Ukraine":"Kyiv", "Poland":"Warsaw"}
# def add(country, capital):
#     countries[country]=capital
#     print("Ok"+ " " + country+ "-" + capital)
# def remove(country):
#     if country in countries:
#         del countries[country]
#         print("Ok")
#     else:
#         print("Not found")

# def search(country):
#     if country in countries:
#         print(f"Country: {country} - Capital city: {countries[country]}")
#     else:
#         print("Not found")

# def change(country, newCapital):
#     if country in countries:
#         countries[country]=newCapital
#         print("Ok")
#     else:
#         print("Not found")

# a=True
# while a:
#     print("1-add\n2-remove\n3-search\n4-change\n5-print all\n0-exit")
#     num=int(input("Enter num of information: "))
#     if num==1:
#         newCountry=input("Enter new country: ")
#         newCapital=input("Enter new capital city: ")
#         add(newCountry, newCapital)
#     elif num==2:
#         countryForRemove=input("Enter name of country: ")
#         remove(countryForRemove)
#     elif num==3:
#         countryForSearch=input("Enter name of country: ")
#         search(countryForSearch)
#     elif num==4:
#         countryForChange=input("Enter name of country: ")
#         newCapital=input("Enter new capital city: ")
#         change(countryForChange, newCapital)
#     elif num==5:
#         print(countries)
#     elif num==0:
#         a=False
#     else:
#         print("Error")

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