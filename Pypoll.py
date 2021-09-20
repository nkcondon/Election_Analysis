

# Add our dependencies
import csv
import os
# Import the datetime class from the datetime module.
import datetime as dt

# Use the now()attribute on the datetime class to ge the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Assign a variable for the file to load and the path.
file_to_load = os.path.join(".", "Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis
    print(election_data)
# Close the file


# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1 Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


reader = csv.reader(election_data)
    # Read and the header row.
headers = next(file_reader)

    # Print each row in the csv file.
for row in file_reader:

        # Add to the total vote count.
        total_votes += 1
    
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # 3. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

     # After opening the file print the final vote count to the terminal.
    election_results = ( 
         f"\nElection Results \n"
         f"-----------------------\n"
         f"Total Votes: {total_votes: ,}\n")
    print(election_results, end="")
    
    #After printing the final vote count to the terminal save the final vote to a text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    

        #  Print out the winning candidate, vote count and percentage to 
    #   terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary)

    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)



    # Close the file
    election_data.close()
