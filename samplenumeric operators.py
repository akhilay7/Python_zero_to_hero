"""a= input( 'enter a number  : ')
b= int(a)**2 + 5.8 /3
print(b)"""

"""cost_per_hour = 0.51

days = int(input("Enter the number of days in the month: "))

cost_per_day = cost_per_hour * 24
cost_per_month = cost_per_day * days


print(f"Cost per day: ${cost_per_day:.2f}")
print(f"Cost for the month: ${cost_per_month:.2f}")"""

cost_per_hour = 0.51
servers = 20 
savings =918

cost_per_day = cost_per_hour * 24
cost_per_month = cost_per_day * 30
cost_per_month_20 = cost_per_day * 30* 20
cost_per_day_20 = cost_per_hour * 24 * 20
cost_per_918 = 918 / (0.51 * 24)

print("Cost to operate one server per day: $", cost_per_day)
print("Cost to operate one server per month: $", cost_per_month)
print ( cost_per_month_20)
print(cost_per_day_20 )
print(cost_per_918)