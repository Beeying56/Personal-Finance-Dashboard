# risk_level: Low, Medium, High, Very high
class Investment:
    def __init__(self, invest, plan, year, goal):
        self.invest = invest
        self.plan = plan
        self.year = year
        self.goal = goal
        self.name = "Investment"
    
    @staticmethod
    def cal_fv(t, pmt, r=0.015, n=12):
        total_times = n * t
        numer = ((1+(r/n))**total_times) - 1
        denom = r/n
        fv = pmt * (numer/denom)
        return fv
        

    def simulation(self, verbose=False):
        money1, money2, money3, money4 = (self.invest*self.plan[0], \
                                          self.invest*self.plan[1], \
                                          self.invest*self.plan[2], self.invest*self.plan[3])
        fv_1 = self.cal_fv(self.year, money1)
        fv_2 = self.cal_fv(self.year, money2, r=0.05)
        fv_3 = self.cal_fv(self.year, money3, r=0.10)
        fv_4 = self.cal_fv(self.year, money4, r=0.25)
        total = fv_1 + fv_2 + fv_3 + fv_4
        left_over = total - self.goal
        is_sufficient = left_over >= 0
        
        if not is_sufficient:
            status_message = (
                f"Your investment plan is not sufficient to cover your retirement fund. "
                f"You require an additional {-left_over:,.2f} baht to reach your goal."
            )
        else:
            status_message = (
                f"Your current investment strategy fully supports your retirement goals. "
                f"You have an additional {left_over:,.2f} baht available for your retirement."
            )
        
        if verbose:
            print(f"You invest {self.invest * 12:,.2f} baht annually over a {self.year}-year period.")
            print(f"By the time you retire, you will have {total:,.2f} baht to enjoy the next chapter of your life.")
            print(status_message)
            print(f"*"*100)
            print(f"\n")
        
        return {
            "name": self.name,
            "annual_investment": self.invest * 12,
            "invest_years": self.year,
            "projected_total": total,
            "target_goal": self.goal,
            "surplus_or_deficit": left_over,
            "is_sufficient": is_sufficient,
            "status_message": status_message
        }