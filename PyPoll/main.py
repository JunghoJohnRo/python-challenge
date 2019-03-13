import os
import csv

# Creating a path to pull data from folder (Once again used ".expanduser" to read the file)
electionCSV = os.path.expanduser('~/Desktop/Homework 3/python-challenge/election_data.csv')

# Reading the CSV file
with open(electionCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Define the Variables and Starting values
    row = 0
    totalVotes = 0
    khanVote = 0
    correyVote = 0
    liVote = 0
    otooleyVote = 0

    # Loop through the data
    for row in csvreader:

        # Total amount of votes
        totalVotes += 1

        # Finding the total votes for each Candidate
        if row[2] == "Khan":
            khanVote += 1
        elif row[2] == "Correy":
            correyVote += 1
        elif row[2] == "Li":
            liVote += 1
        elif row[2] == "O'Tooley":
            otooleyVote += 1
   
    # Calculate Percentage of Votes for each Candidate
    khanPercent = (khanVote / totalVotes)
    correyPercent = (correyVote / totalVotes)
    liPercent = (liVote / totalVotes)
    otooleyPercent = (otooleyVote / totalVotes)

    # Creating Dictionary and finding Winner of election (Googled for max function and key=__.get to find value)
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    candidatevotes = [khanVote, correyVote, liVote, otooleyVote]
    candidatelist = dict(zip(candidates, candidatevotes))
    winner = max(candidatelist, key=candidatelist.get)

# Print Final Results in Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(totalVotes)}")
print("-------------------------")
# Googled how to format so the percentages show 3 decimal points
print(f"Khan: {'{:.3%}'.format(khanPercent)} ({str(khanVote)})")
print(f"Correy: {'{:.3%}'.format(correyPercent)} ({str(correyVote)})")
print(f"Li: {'{:.3%}'.format(liPercent)} ({str(liVote)})")
print(f"O'Tooley: {'{:.3%}'.format(otooleyPercent)} ({str(otooleyVote)})")
print("-------------------------")
print(f"Winner: {str(winner)}")
print("-------------------------")

# Specify where to export Text File to
export_file = os.path.expanduser('~/Desktop/Homework 3/python-challenge/PyPoll/Final.txt')

# Open the file and write what to print in Text File (Once agained use "\n" so it prints in the next line)
with open(export_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {str(totalVotes)}\n")
    file.write("-------------------------\n")
    file.write(f"Khan: {'{:.3%}'.format(khanPercent)} ({str(khanVote)})\n")
    file.write(f"Correy: {'{:.3%}'.format(correyPercent)} ({str(correyVote)})\n")
    file.write(f"Li: {'{:.3%}'.format(liPercent)} ({str(liVote)})\n")
    file.write(f"O'Tooley: {'{:.3%}'.format(otooleyPercent)} ({str(otooleyVote)})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {str(winner)}\n")
    file.write("-------------------------\n")