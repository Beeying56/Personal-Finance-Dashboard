import json
from pathlib import Path

class TaxPlanning:
    def __init__(self, salary):
        self.salary = salary
        self.year_income = salary * 12
        self.name = "Tax Planning"

    @staticmethod
    def cal_tax(year_income):
        if year_income <= 150000:
            return 0
        brackets = [
            (150000, 300000, 0.05),
            (300000, 500000, 0.10),
            (500000, 750000, 0.15),
            (750000, 1000000, 0.20),
            (1000000, 2000000, 0.25),
            (2000000, 5000000, 0.30),
            (5000000, float('inf'), 0.35)
        ]
        
        total_tax = 0
        for lower, upper, rate in brackets:
            if year_income > lower:
                taxable_in_bracket = min(year_income, upper) - lower
                total_tax += taxable_in_bracket * rate
            else:
                break
        return total_tax
        
    def cal_deduction(self):
        BASE_DIR = Path(__file__).resolve().parent
        json_file = BASE_DIR / "tax_data.json"
        try:
            with open(json_file) as file:
                data = json.load(file)
        except FileNotFoundError:
            # Provide default fallback dictionary instead of crashing
            data = {
                "personal": 60000, "spouse": 0, "firstchild": 0, "secondchild": 0,
                "father": 0, "mother": 0, "spousefather": 0, "spousemother": 0,
                "disableperson": 0, "pregnancy": 0, "insurance": 0, "healthinsurance": 0,
                "parentinsurance": 0, "spouseinsurance": 0, "pvd": 0, "ssf": 0,
                "rmf": 0, "pensioninsurance": 0, "socialinsurance": 0,
                "mortgageinterest": 0, "donation": 0
            }
            
        deduction = 0
        if data["personal"] != 60000:
            data["personal"] = 60000
        deduction += data["personal"]
        
        if data["spouse"] != 60000 and data["spouse"] != 0:
            data["spouse"] = 60000
        deduction += data["spouse"]

        if data["firstchild"] != 30000 and data["firstchild"] != 0:
            data["firstchild"] = 30000
        deduction += data["firstchild"]
        
        if data["secondchild"] != 60000 and data["secondchild"] != 0:
            data["secondchild"] = 60000
        deduction += data["secondchild"]
        
        if data["father"] != 30000 and data["father"] != 0:
            data["father"] = 30000
        deduction += data["father"]
            
        if data["mother"] != 30000 and data["mother"] != 0:
            data["mother"] = 30000
        deduction += data["mother"]
            
        if data["spousefather"] != 30000 and data["spousefather"] != 0:
            data["spousefather"] = 30000
        deduction += data["spousefather"]
            
        if data["spousemother"] != 30000 and data["spousemother"] != 0:
            data["spousemother"] = 30000
        deduction += data["spousemother"]
            
        deduction += data["disableperson"]
        
        if data["pregnancy"] != 60000 and data["pregnancy"] != 0:
            data["pregnancy"] = 60000
        deduction += data["pregnancy"]
        
        if data["insurance"] > 100000 and data["insurance"] != 0:
            data["insurance"] = 100000
        deduction += data["insurance"]

        if data["healthinsurance"] > 25000 and data["healthinsurance"] != 0:
            data["healthinsurance"] = 25000
        deduction += data["healthinsurance"]
        
        if data["parentinsurance"] > 15000 and data["parentinsurance"] != 0:
            data["parentinsurance"] = 15000
        deduction += data["parentinsurance"]
        
        if data["spouseinsurance"] > 10000 and data["spouseinsurance"] != 0:
            data["spouseinsurance"] = 10000
        deduction += data["spouseinsurance"]
        
        upperbound = 500000
        if self.year_income * 0.15 < 500000:
            upperbound = self.year_income * 0.15
        if data["pvd"] > upperbound and data["pvd"] != 0:
            data["pvd"] = upperbound
        deduction += data["pvd"]
        
        upperbound = 200000
        if self.year_income * 0.3 < 200000:
            upperbound = self.year_income * 0.3
        if data["ssf"] > upperbound and data["ssf"] != 0:
            data["ssf"] = upperbound
        deduction += data["ssf"]
        
        upperbound = 500000
        if self.year_income * 0.3 < 500000:
            upperbound = self.year_income * 0.3
        if data["rmf"] > upperbound and data["rmf"] != 0:
            data["rmf"] = upperbound
        deduction += data["rmf"]
        
        upperbound = 200000
        if self.year_income * 0.15 < 500000:
            upperbound = self.year_income * 0.15
        if data["pensioninsurance"] > upperbound and data["pensioninsurance"] != 0:
            data["pensioninsurance"] = upperbound
        deduction += data["pensioninsurance"]
        
        if data["socialinsurance"] > 9000 and data["socialinsurance"] != 0:
            data["socialinsurance"] = 9000
        deduction += data["socialinsurance"]
        
        if data["mortgageinterest"] > 100000 and data["mortgageinterest"] != 0:
            data["mortgageinterest"] = 100000
        deduction += data["mortgageinterest"]
        
        income = self.year_income - deduction
        upperbound = income * 0.1
        if data["donation"] > upperbound and data["donation"] != 0:
            data["donation"] = upperbound
        deduction += data["donation"] * 2
        
        income = self.year_income - deduction
        self.deduction = deduction
        
        return self.cal_tax(income)
    
    def simulation(self, verbose=False):
        tax_pay = self.cal_deduction()
        net_income = max(0, self.year_income - self.deduction)
        
        if verbose:
            print(f"Your income in this year is {self.salary * 12:,.2f}")
            print(f"Your total deduction cost in this year is {self.deduction:,.2f}")
            print(f"The amount of tax you must pay in this year is {tax_pay:,.2f} baht.")
            print(f"*"*100)
            print(f"\n")
            
        return {
            "name": self.name,
            "annual_income": self.year_income,
            "total_deduction": self.deduction,
            "net_taxable_income": net_income,
            "tax_payable": tax_pay
        }
    
    
if __name__ == '__main__':
    salary = 78000
    year_income = salary * 12
    tax_person1 = TaxPlanning(salary)
    print(year_income)
    
    print(tax_person1.cal_tax(year_income))
    print(tax_person1.cal_deduction())
    
    tax_person2 = TaxPlanning(salary=50000)
    print(tax_person2.year_income)
    print(tax_person2.cal_tax(tax_person2.year_income))
    print(tax_person2.cal_deduction())