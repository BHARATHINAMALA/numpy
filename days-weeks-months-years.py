age=int(input("enter your current age"))
years=int(input("for how many years you want to calculate balance 'days','weeks','months','years'"))
years_left=years-age
days_left=years_left*365
weeks_left=years_left*52
months_left=years_left*12
print(f"you have {days_left} days,{weeks_left} weeks,and {months_left} months left ")