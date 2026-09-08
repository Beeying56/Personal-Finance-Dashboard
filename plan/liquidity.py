
class Liquidity:
    socialinsurance = 875
    def __init__(self, salary, tax, fix_expense, vary_expense, debt_pay):
        self.salary = salary
        self.fix_expense = fix_expense
        self.vary_expense = vary_expense
        self.debt_pay = debt_pay
        self.tax_monthly = tax/12
        self.saving = self.salary - self.tax_monthly - self.fix_expense - \
                      self.debt_pay - self.vary_expense - Liquidity.socialinsurance
        self.name = "Liquidity Health"
        self.cal_reserve(reserve_month=6)
        
        
    def check_saving_ratio(self, verbose=False):
        if self.saving <= 0:
            raise ValueError("Negative or zero savings. Please review your income and expenses.")
    
        saving_ratio = (self.saving/self.salary) * 100
        
        if 0 < saving_ratio < 10:
            msg = "In the future, you will live a decent life."
            status = "error"
        elif 10 <= saving_ratio < 20:
            msg = "In the future, you will enjoy a comfortable and fulfilling life."
            status = "warning"
        elif 20 <= saving_ratio < 50:
            msg = "You are on the path to financial success and a life of abundance."
            status = "success"
        else: # ครอบคลุมกรณี >= 50
            msg = "Your early efforts will lead to financial freedom while you are still young."
            status = "info"
        # ต้องมั่นใจว่ามี return อยู่บรรทัดนอกสุดเพื่อส่งค่าออกไปเสมอ

        if verbose:
            print(f"You save {saving_ratio:.2f}% of your income.")
            print(msg)

            
        return {
            "ratio": saving_ratio,
            "message": msg,
            "status": status
        }

    def check_debt_ratio(self, verbose=False):
        
        if self.salary <= 0:
            raise ValueError("Salary must be greater than zero.")
                
        if self.debt_pay >= self.salary:
            raise ValueError("Debt cannot be higher than or equal to salary.")
            
        debt_ratio = (self.debt_pay / self.salary) * 100

        if 0 <= debt_ratio < 10:
            msg = "Your life will feel lighter and less constrained."
            status = "info"
        elif 10 <= debt_ratio < 30:
            msg = "You have a manageable level of burden."
            status = "success"
        elif 30 <= debt_ratio < 50:
            msg = "You're dealing with a heavy load."
            status = "warning"
        else:
            msg = "You will have little freedom due to high debt."
            status = "error"
            
        if verbose:
            print(msg)
            
        return {
                "ratio": debt_ratio,
                "message": msg,
                "status": status
            }
        
            
    def cal_reserve(self, reserve_month=6):
        self.fix_cost_fund = self.fix_expense * reserve_month
        self.reserve_fund = (self.fix_expense * reserve_month) + (self.vary_expense * reserve_month)
        
    def simulation(self, verbose=False):
        self.check_saving_ratio(verbose)
        self.check_debt_ratio(verbose)
        if verbose:
            print(f"\n")
            print("Suggested amount for an emergency fund")
            self.cal_reserve(reserve_month=6)
            print(f"Fixed expense fund for 6 months: {self.fix_cost_fund:,.2f}")
            print(f"Fixed and variable expense fund for 6 months: {self.reserve_fund:,.2f}")
            print(f"*"*100)
            print(f"\n")
            
        return {
            "name": self.name,
            "saving": self.saving,
            "saving_analysis": self.check_saving_ratio(),
            "debt_analysis": self.check_debt_ratio(),
            "fix_cost_fund": self.fix_cost_fund,
            "reserve_fund": self.reserve_fund
        }
            