import os
import csv

election_data = os.path.join("election_data.csv")

# list to capture the names of candidates, number of votes per candidate, percentage of total votes per candidate, and total number of votes
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to vote-counter
        total_votes += 1 


        #If the candidate is not on list, add name and vote to list
        #If already on list, we add vote

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Display results
print("Election Results")
print("-" * 25)
print(f"Total Votes: {str(total_votes)}")
print("-" * 25)
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("-" * 25)
print(f"Winner: {winning_candidate}")
print("-" * 25)

# Export to text
output = open("polloutput.txt", "w")
line1 = "Election Results"
line2 = ("-" * 25)
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("-" * 25)
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = ("-" * 25)
line6 = str(f"Winner: {winning_candidate}")
line7 = ("-" * 25)
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

