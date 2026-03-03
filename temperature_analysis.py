Name: Harini N
Assignment:Python Loops & automation - Subjective Question


Task 1 : Find Maximum and Minimum

temperatures = [28, 32, 35, 29, 31, 27, 30]
highest=temperatures[0]
lowest=temperatures[0]
for temp in temperatures:
    if temp>highest:
        highest=temp
    if temp<lowest:
        lowest=temp
print(f"highest temperature={highest}c")
print(f"lowest temperature={lowest}c")

Task 2 : count Hot Days

temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue  
    
    hot_days += 1 

print(f"Hot Days (>30°C): {hot_days}")


Task 3 : Alert System

temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_days = 0
day_number = 0

for temp in temperatures:
    day_number += 1  
    
    
    if temp >= 40:
        print(f"Hot Days before alert: {hot_days}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day_number}")
        break  
   
    if temp > 30:
        hot_days += 1





