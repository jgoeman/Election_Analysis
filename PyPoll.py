# Import Modules
import csv
import os

#Assign a variable for the file to load and the path.
#this is the direct path: file_to_load = 'resources/election_results.csv'
file_to_load = os.path.join("..","Resources", "election_results.csv")             

#Create a filename variable to a direct or indirect path to the file to save for analysis.
file_to_save = os.path.join("..",'analysis', "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as txt_file:
    #Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")
   
#Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    #Perform analysis
    print(election_data)

    #The data we need to retrieve.
    #To do:read and analyze the data here.
    file_reader = csv.reader(election_data)
    #Read and print the Header Row
    headers = next(file_reader)
    print(headers)

#Print each row in the CSV file.
    for row in file_reader:
        print(row)
#1. The total number of votes cast
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election base on popular vote.

# close the file.
