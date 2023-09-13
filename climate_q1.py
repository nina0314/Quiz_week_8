import  matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect(r'climate.db')
cursor = connection.cursor()


years = []
co2 = []
temp = []

cursor.execute("SELECT Temperature FROM ClimateData")
temp = cursor.fetchall()
cursor.execute("SELECT CO2 FROM ClimateData")
co2  = cursor.fetchall()
cursor.execute("SELECT Year FROM ClimateData")
years = cursor.fetchall()



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data")

plt.ylabel("[CO2]") 

plt.xlabel("Year (decade)")


plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)")

plt.show() 
plt.savefig("co2_temp_1.png") 


