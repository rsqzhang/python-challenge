import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# Set initial variable to hold the total number of votes cast
totalVotes = 0

# Set initial dictionary to hold the list of candidates and the total number of votes each candidate won
candidateVotes = {}

# Set initial variable to hold the winner of the election
winner = "n/a"

# Set initial variable to hold the total number of votes the winner won
winnerVotes = 0

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Add one to the total number of votes cast
        totalVotes += 1

        # Check if the name of the candidate is in the dictionary, if so...
        if row[2] in candidateVotes.keys():

            # Add one to the total number of votes the candidate won
            candidateVotes[row[2]] += 1
        
        # If the name of the candidate is not in the dictionary...
        else:

            # Add the candidate to the dictionary and set the total number of votes the candidate won to zero
            candidateVotes[row[2]] = 1

# Print out the election results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

# Loop through the candidate dictionary to calculate the winner of the election
for key in candidateVotes.keys():
    print(key + ": " + str(round((candidateVotes[key] / totalVotes) * 100, 3)) + "% (" + str(candidateVotes[key]) + ")")
    
    # Check if the total number of votes the candidate won is greater than the total number of votes the winner won, if so...
    if candidateVotes[key] > winnerVotes:

        # Set the winner of the election to the candidate
        winner = key

        # Reset the total number of votes the winner won
        winnerVotes = candidateVotes[key]

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Export a text file with the results
analysisText = open("analysis.txt", 'w')

analysisText.write("Election Results\n")
analysisText.write("-------------------------\n")
analysisText.write("Total Votes: " + str(totalVotes) + "\n")
analysisText.write("-------------------------\n")
for key in candidateVotes.keys():
    analysisText.write(key + ": " + str(round((candidateVotes[key] / totalVotes) * 100, 3)) + "% (" + str(candidateVotes[key]) + ")\n")
analysisText.write("-------------------------\n")
analysisText.write("Winner: " + winner + "\n")
analysisText.write("-------------------------")