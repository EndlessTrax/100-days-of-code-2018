'''
It is a well-documented fact that the number of pirates in the world is correlated with a rise in global temperatures.
Write a script pirates.py that visually examines this relationship:
• Read in the file pirates.csv from the Chapter 14 practice files folder.
• Create a line graph of the average world temperature in degrees Celsius as a function 
    of the number of pirates in the world - i.e., graph Pirates along the x-axis and Temperature along the y-axis.
• Add a graph title and label your graph’s axes.
• Save the resulting graph out as a PNG image file.
• Bonus: Label each point on the graph with the appropriate Year; you should do this “programmatically” 
    by looping through the actual data points rather than specifying the individual position of each annotation.
'''

import csv
from matplotlib import pyplot as plt


# New lists for each column of the csv
years = []
temp = []
pirates = []

# Open the csv and read the data
with open('pirates.csv', 'r') as file:
    reader = csv.reader(file)

    # Skip the headers on the first line
    next(reader)

    # Loop through the row and append each value into the appropriate list
    for row in reader:
        years.append(row[0])
        temp.append(row[1])
        pirates.append(row[2])


# Plot pirates on the x-axis, and temp on the y-axis
plt.plot(pirates, temp)

# Add a title and labels to the graph
plt.title("Pirates Prevent Global Warming")
plt.xlabel("Number of Pirates")
plt.ylabel("Average World Temperature")

# Annotate each point with coresponding year
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temp[i]))

# Save the graph as a .png
plt.savefig("pirates-graph.png")

# Display the graph in a pop-out window
plt.show()