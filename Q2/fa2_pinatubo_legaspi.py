class Patient:
    __name: str
    __bill_amount: float
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return f"Patient name: {self.__name} \nOriginal Bill: {self.__bill_amount} \nFinal Bill: {self.__bill_amount}"

class Senior_Patient(Patient):
    def calculate_bill(self):
        amount = self.get_bill_amount()*0.80
        return f"Patient name: {self.get_name()} \nOriginal Bill: {self.get_bill_amount()} \nFinal Bill: {amount}"

class PhilHealth_Patient(Patient):
    def calculate_bill(self):
        amount = self.get_bill_amount()*0.85
        return f"Patient name: {self.get_name()} \nOriginal Bill: {self.get_bill_amount()} \nFinal Bill: {amount}"

pat1 = Patient("Juan Dela Cruz", 15000)
senpat1 = Senior_Patient("Maria Santos", 15000)
philpat1 = PhilHealth_Patient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("--------------------------------")
print(pat1.calculate_bill())
print("")
print(senpat1.calculate_bill())
print("")
print(philpat1.calculate_bill())
