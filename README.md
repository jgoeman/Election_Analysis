# Election Analysis Challenge

## Project Overview
A Colorado Board of Elections employee has requested assistance in completing the election audit of a recent local congressional election. The following tasks were asked to completed to assist in completing the audit. The election commision has now also requested more information listed in steps 6-9 below.

1. Calculate the toal number of votes cast
2. Get a complete list of candiates who received votes
3. Calculate the total number of votes each candiate received
4. calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county
7. Calculate the percentage of votes from each county out of the total count
8. State the county with the highest turnout on the text file

## Resources
- Data Source: election_results.csv
- Python 3.7.6, 
- Visual Studio Code 1.61.0

## Election Audit Results
The project provided the following results for the election analysis:
- There were a total of 369,711 votes.
- Three counties were included in the election, and had the follwing voter turnout:
  1. Jefferson County: 38,855 votes cast. A total of 10.5% of the total votes cast.
  2. Denver County: 306,055 votes cast. A total of 82.8% of the total votes cast.
  3. Arapahoe County. 24,801 votes cast. A total of 6.7% of the total votes cast.
  
- Denver County had the larget amount of Votes cast with 306,055 votes which is 82.8% of the total votes.
  
- There were a total of 3 candiates in this electoral competition with the follwing results:
  1. Charles Casper Stockham: 85,213 total votes received which comes out to 23% of the total vote.
  2. Diana DeGette: 272,892 total votes received which comes out to 73.8% of the total vote.
  3. Raymon Anthony Doane: 11,606 total votes received which comes out to 3.1% of the total vote.
  
- The winner of the election is Candidate 2. Diana Degette who received 272,892 votes which is 73.8% of the total votes.

## Election Audit Summary  
The script used in this project is simple, but has the ability to be quite powerful in the use of auditing more the just the current election, both quickly and efficiently. To understand this the follwing will provide information on what actions thee script is performing.  
The script will read through a CSV file and  perform the following functions:
- Find all unique candidates and counties
- Find the total votes cast
- Find the total votes cast by each county, give the percent of the total votes, and and gather the county with the most votes.
- Find the total votes received by each candidate,give percent of the total for each, and gather who won the information.
- Print out all the the information gathered to a txt file that can be easily understood.  
  
Some modification the script could allow for further use would be an input could be requested and then used to provide information pertaining to what is being sought on a specfic candidate or county.The informatin gathered could also be wrote back to a csv file as well. The script used in the project is included below.
  
```
# -*- coding: UTF-8 -*-

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_turnout = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
County_largest_turnout = ""
largest_county_votes = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

     # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_turnout[county_name] = 0      

        # 5: Add a vote to that county's vote count.
        county_turnout[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_turnout:
        # 6b: Retrieve the county vote count.
        county_votes = county_turnout.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_votes:,})\n")

        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if county_votes > largest_county_votes:
            largest_county_votes = county_votes 
            County_largest_turnout = county_name


    # 7: Print the county with the largest turnout to the terminal.
        County_votes_summary = (f"-----------------------\n"
        f"Largest County Turnout: {County_largest_turnout} \n"
        f"-----------------------\n")
    print(County_votes_summary)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(County_votes_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    
    
