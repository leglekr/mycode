#!usr/bin/env python3

#initalize an integer variable, months_per_year
months = 12

#initialize another integer variable, days_per_year
days_per_year = 365

#compute the average days per month
avg_num_days = days_per_year / months

#compute the average days per month
avg_num_days2 = days_per_year // months


# Print out information about the days in a year, months in a year
print("There are 365 days in a year .. except for leap-years.")
print("There are 12 months in a year")

#Print an empy line
print()

#Print the average number of days, per month
print("The average number of days in a given month is: ",avg_num_days)

print(round(avg_num_days))

#Print the average number of days, per month
print("The average number of days in a given month is: ",avg_num_days2)


# This is another way to print an empty line
print("\n")
