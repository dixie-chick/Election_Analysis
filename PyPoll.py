# Open the data file.
#Add dependencies.
import csv
import os

#Assign a variable for to load file from path
file_to_load = os.path.join("C:\\Users\\ddickson\\DataBootCamp\\Election_Analysis\\Resources\\election_results.csv")

#Assign a variable to save file to path
file_to_save = os.path.join("C:\\Users\\ddickson\\DataBootCamp\\Election_Analysis\\Resources\\election_analysis.txt")

#1. Initialize the variables
# vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Candidate votes
candidate_votes = {}

#Create Winning Candidate and Winning Count Variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read the file
with open(file_to_load) as election_data:
    #print(election_data)
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers =next(file_reader)
    #print(headers)

#   #Print each row in the CSV file.
    for row in file_reader:
    #2. Add to the total vote count
        total_votes += 1
   
        #3 Print the total votes
        #print(total_votes)

        # Write down the names of all the candidates/ Print the candidate name for each row
        candidate_name = row[2]

#Get unique candidate names
        if candidate_name not in candidate_options:
            # Add the candidate name to the list
            candidate_options.append(candidate_name)
#print(candidate_options)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
            #Add a vote for each row the candidate and get total votes
        candidate_votes[candidate_name] += 1

#Save results to text file
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Calculate percentage votes for each candidate
    #vote_percentage = (votes/total_votes)*100
    
    #1. Create for loop to iterate through candidate list
    for candidate_name in candidate_votes:
        #2. get vote count for candidate
        votes = candidate_votes[candidate_name]
        #3 calculate vote percentage
        vote_percentage = float(votes)/float(total_votes) * 100
        #Limit to 2 decimals
        #limited_vote = round(vote_percentage, 2)
        #4. Print candidate with vote percentage
        #print(f"{candidate_name}: received {round(vote_percentage, 2)}% of the vote.")
        candidate_results = (f"{candidate_name} : {vote_percentage: .1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #1. Use if to find the winning candidate
        #Determine if the votes are grater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        #print out the winning candidate, vote count and percentage
        #print(f"{winning_candidate} has {winning_count} at {winning_percentage}%")

    #Create winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)