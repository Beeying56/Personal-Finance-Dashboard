from .investment import Investment
from .liquidity import Liquidity
from .retire import Retirement
from .tax import TaxPlanning

class Profile:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    
    def get_finance_info(self, salary, fix_expense, vary_expense, debt_pay):
        self.salary = salary
        self.fix_expense = fix_expense
        self.vary_expense = vary_expense
        self.debt_pay = debt_pay
        
        
    def get_retire_goal(self, retire_age, life_age, monthly_cost):
        self.retire_age = retire_age
        self.life_age = life_age
        self.monthly_cost = monthly_cost
        
        
    def get_invest_plan(self, plan=None):
        low_port = [0.5, 0.3, 0.15, 0.05]
        medium_port = [0.3, 0.35, 0.25, 0.1]
        high_port = [0.2, 0.2, 0.35, 0.25]
        
        if plan == None:
            if self.age < 30:
                self.invest_plan = high_port
            elif 30 < self.age < 40:
                self.invest_plan = medium_port
            elif 40 < self.age < 50:
                self.invest_plan = low_port
            else:
                self.invest_plan = [1, 0, 0, 0]
        else:
            self.invest_plan = plan
                
                
    def create_plan(self):
        self.tax = TaxPlanning(self.salary)
        annual_tax = self.tax.cal_deduction()
        
        self.liquidity = Liquidity(
            self.salary, annual_tax, self.fix_expense, 
            self.vary_expense, self.debt_pay
        )
        self.retire = Retirement(
            self.age, self.retire_age, self.life_age, self.monthly_cost
        )
        self.invest = Investment(
            self.liquidity.saving, self.invest_plan, 
            self.retire_age - self.age, self.retire.cal_fund()
        )
        
        self.plans = [self.tax, self.liquidity, self.retire, self.invest]
    
    def get_result(self):
        return {
            "profile": {
                "name": self.name,
                "surname": self.surname,
                "full_name": f"{self.name} {self.surname}",
                "age": self.age
            },
            "results": {
                plan.name: plan.simulation() for plan in self.plans
            }
        }
    
    @staticmethod
    def neon_banner(text):
        # ANSI Codes: 92 is Green, 95 is Magenta, 1 is Bold
        G = "\033[92m" 
        M = "\033[95m"
        B = "\033[1m"
        R = "\033[0m"
        
        line = "★" + "—" * (len(text) + 2) + "★"
        print(f"{M}{line}{R}")
        print(f"{M}│ {G}{B}{text.upper()} {M}│{R}")
        print(f"{M}{line}{R}")

        
    def get_report(self):
        name = self.name + ' ' + self.surname + ' age ' + str(self.age)
        self.neon_banner(name)
        
        for plan in self.plans:
            length = len(plan.name) + 4
            print(f"┌{'─' * length}┐")
            print(f"│  {plan.name.upper()}  │")
            print(f"└{'─' * length}┘")
            plan.simulation(verbose=True)
    
    