class Passport:
    def __init__(self, name, surname, birth_date, sex, date_issue, date_expiration):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.sex = sex
        self.date_issue = date_issue
        self.date_expiration = date_expiration
    
    def show_info(self):
        print(f"Passport info: {self.name} {self.surname} - {self.birth_date}")

    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_birth_date(self):
        return self.birth_date
    def set_date_issue(self, value):
        self.date_issue = value
    def set_date_expiration(self, value):
        self.date_expiration = value
    def __str__(self)-> str:
        return f"Passport({self.name}, {self.surname}, {self.birth_date}, {self.sex}, {self.date_issue}, {self.date_expiration})"
    

class ForeignPassport(Passport):
    def __init__(self, name, surname, birth_date, sex, date_issue, date_expiration, visas, passport_number):
        self.visas = visas
        self.passport_number = passport_number
        super().__init__(name, surname, birth_date, sex, date_issue, date_expiration)

    def show_info(self):
        print(f"Passport info: {self.name} {self.surname} - {self.passport_number}")
        if type(self.visas) == list:
            print(f"Number of visas: {len(self.visas)}")
            for visa in self.visas:
                print(visa)
        elif type(self.visas) == str:
            print(f"Visa: {self.visas}")

    def get_passport_number(self):
        return self.passport_number
    def get_vivas(self):
        return self.visas
    def set_vivas(self, value):
        self.visas = value

    def add_visa(self, visa):
        if type(self.visas) == list:
            if visa not in self.visas:
                self.visas.append(visa)
                print(f"Visa {visa} added")
        elif type(self.visas) == str:
            self.visas = [self.visas, visa]
            print(f"Visa {visa} added")
        elif self.visas == None:
            self.visas = [visa]
            print("Visa added")

    def delete_visa(self, visa):
        if type(self.visas) == list:
            if visa in self.visas:
                self.visas.remove(visa)
                print(f"Visa {visa} removed")
        elif type(self.visas) == str:
            self.visas = None
            print("Visas removed")
        elif self.visas == None:
            print("No visas")

    def __str__(self)->str:
        return f"ForeignPassport({self.name}, {self.surname}, {self.birth_date}, {self.sex}, {self.date_issue}, {self.date_expiration}, {self.visas}, {self.passport_number})"

for_passport=ForeignPassport("Mary","Maksi","29.09.2000","F","24.10.2018","24.11.2028",["USA"], "12345678")
for_passport.show_info()
for_passport.add_visa("Ukraine")

class Number_count:
    number = 0

    @staticmethod
    def show_info():
        print(f"Number of counts temperature: {Number_count.number}")

    @staticmethod
    def converting_to_fahrenheit(temperature):
        Number_count.number += 1
        return temperature * 1.8 + 32
    
    @staticmethod
    def converting_to_celsius(temperature):
        Number_count.number += 1
        return (temperature - 32) / 1.8
    
Number_count.show_info()
temperature=Number_count.converting_to_fahrenheit(1)
print(temperature)
temperature=Number_count.converting_to_celsius(100)
print(temperature)
Number_count.show_info()