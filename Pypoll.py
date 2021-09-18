# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.
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

# Create a filename variable to a direct or indirect path to file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Close the file
election_data.close()

# Using the open() function with the "w" mode will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the election\n----------\nArapahoe\n Denver\n Jefferson")


