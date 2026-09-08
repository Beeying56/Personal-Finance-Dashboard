class Retirement:
    def __init__(self, age, retire_age, life_age, monthly_cost):
        self.age = age
        self.retire_age = retire_age
        self.life_age = life_age
        self.monthly_cost = monthly_cost
        self.name = "Retire Fund"
        
        
    def cal_fund(self, inflation=0.03):
        retire_duration = self.life_age - self.retire_age
        yearly_cost = self.monthly_cost * 12
        yearly_cost_retire = yearly_cost * ((1 + inflation)**(self.retire_age-self.age))
        retire_fund = yearly_cost_retire * retire_duration
        return retire_fund
        

    def simulation(self, verbose=False):
        retire_fund = self.cal_fund()
        retire_duration = self.life_age - self.retire_age
        if verbose:
            print(f"Your goal is to retire at age {self.retire_age}.")
            print(f"You plan to spend {retire_duration} years in retirement.")
            print(f"To live freely and comfortably in old age, you should have a retirement fund of {retire_fund:,.2f} baht.")
            print(f"*"*100)
            print(f"\n")
        return {
            "name": self.name,
            "retire_age": self.retire_age,
            "retire_duration": retire_duration,
            "monthly_cost": self.monthly_cost,
            "retire_fund": retire_fund
        }

