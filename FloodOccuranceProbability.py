#Calculator for Flood Event Occurrence for Various Periods
#return_period: 10, 50, 100, 500
return_period = 500
#building life: 30, 60, 90
building_life = 70
POA = 1-(1-(1/return_period))**building_life
percentage = "{:.0%}".format(POA)
print("Probability of occurance during your building life", percentage)