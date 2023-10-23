#main py
import os
import csv

# Define the path for the CSV
csv_path = os.path.join("PyPoll\election_data.csv")

# Name the variables 
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file/Open
with open(csv_path, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip  header 
    next(csvreader)

    for row in csvreader:
        # Pull the candidates names
        candidate = row[2]
        total_votes += 1

        #make the candidates dictionary
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Find the winner and calculate the percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Text file
with open ("anlaysis.txt","w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    if votes > max_votes:
        max_votes = votes
        winner = candidate
    textfile.write("-----------------------------\n")
    textfile.write(f"Winner: {winner}")
    
