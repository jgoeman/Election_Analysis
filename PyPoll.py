# Add dependencies
import csv
import os

#Assign a variable for the file to load and the path.
#this is the direct path: file_to_load = 'resources/election_results.csv'
file_to_load = os.path.join("..","Resources", "election_results.csv")             

#Create a filename variable to a direct or indirect path to the file to save for analysis.
file_to_save = os.path.join("..",'analysis', "election_analysis.txt")

# Intialize a total vote counter.
total_votes = 0
#Candidate_options and Candidate votes
candidate_options = []
#Declare empty dictionary for tallying candidate votes by candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as txt_file:
    #Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")
   
#Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    file_reader = csv.reader(election_data)
    #Read the Header Row
    headers = next(file_reader)
   
   #Print each row in the CSV file.
    for row in file_reader:
    #2 Add to the total vote count.#1. The total number of votes cast
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # Add it to the list of candidates. #2. A complete list of candidates who received votes.
            candidate_options.append(candidate_name)
        #Begin tracking that candidates's votes by name starting at 0. Candidate votes is an empty dict started at the top. The next line sets up the key with the number of votes.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    #Iniate a variable to find the percentage of votes for each candidate
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
         # 4. Print the candidate name and percentage of votes to one decimal place.
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    #5. The winner of the election base on popular vote.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)       



            

#Print the candidate vote dictionary.





 
 
 #Perform analysis       


#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won


# close the file.
