from plan import FinancialProfile


profile1 = FinancialProfile("Jon", "Snow", 30)
profile1.get_finance_info(salary=50000, fix_expense=15000, vary_expense=14900, debt_pay=10000)
profile1.get_retire_goal(retire_age=60, life_age=85, monthly_cost=10000)
profile1.get_invest_plan()
profile1.create_plan()
profile1.get_report()


# profile2 = FinancialProfile("Arya", "Stark", 23)
# profile2.get_finance_info(salary=35000, fix_expense=10000, vary_expense=5000, debt_pay=5000)
# profile2.get_retire_goal(retire_age=40, life_age=85, monthly_cost=10000)
# profile2.get_invest_plan()
# profile2.create_plan()
# profile2.get_report()


# profile3 = FinancialProfile("Cersei", "Lannister", 45)
# profile3.get_finance_info(salary=65000, fix_expense=35000, vary_expense=20000, debt_pay=20000)
# profile3.get_retire_goal(retire_age=60, life_age=85, monthly_cost=10000)
# profile3.get_invest_plan()
# profile3.create_plan()
# profile3.get_report()
