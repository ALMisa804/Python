# Create a Python script that analyzes the votes and calculates:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Import dependencies
import os
import csv

# Define variables
candidates = {}

# Path to collect data
election_csv = os.path.join('.','election_data.csv')
with open(election_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1

        total = candidates.values()
        total_votes = sum(total)

            
        list_candidates = candidates.keys()
            
        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
            

        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        winner
        
# Print analysis to the terminal
print("Election results")

print("--------------------------------")

print(f" Total votes: {int(total_votes)}")

print("---------------------------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate} , {vote} , {votes_per[i]} ') 
    i+=1
print("------------------------------")

print(f" Winner: {winner} ")

print("------------------------------")

# Export a text file with the results
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results")
    outfile.write("-------------------------")
    outfile.write(f"Total Votes:  {int(total_votes)}")
    outfile.write("-------------------------")
    i = 0
    for candidate, vote in candidates.items():
        outfile.write(f' {candidate} , {vote} , {votes_per[i] } ')
        i+=1
    outfile.write("-------------------------")
    outfile.write(f" Winner:  {winner} ")
    outfile.write("-------------------------")    