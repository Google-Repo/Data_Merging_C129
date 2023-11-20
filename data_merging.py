#Importing all modules here:
import pandas as pd
import csv

#Define the input CSV Files
data_of_dwarf_stars = "dwarf_stars.csv"
data_of_bright_stars = "bright_stars.csv"

#Empty list to store data from each CSV File:
d1 = []
d2 = []

#Read data from the first CSV File and store it in the list d1
with open(data_of_dwarf_stars,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
#Read data from the second CSV file and store it in the list d2
with open(data_of_bright_stars,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)
        
#Extracting header and data separately for each csv file:
h1 = d1[0]
h2 = d2[0]
p_d1 = d1[1:]
p_d2 = d2[1:]

#Combine headers and data from both CSV files:
h = h1 + h2
p_d = []

#Append data from the second first CSV file to the Combined data list p_d
for i in p_d1:
    p_d.append(i)
    
# Append data from the second CSV file to the combined data list p_d
for j in p_d2:
    p_d.append(j)

# Write the combined data to a new CSV file called 'total_stars.csv'
with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

# Read the merged data from the new CSV file using Pandas
df = pd.read_csv('total_stars.csv')

# Display the last 8 rows of the merged data
df.tail(8)
        