import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(csv_path, encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)

    #Set variables
    total_votes = 0
    candidates = {}
    winner = ""
    max_votes = 0
    candidates_results =[]

    for line in csv_reader:
            ballot_id, county, candidate = line

        #Total number of votes each candidate won
            total_votes += 1

            if candidate in candidates:
                candidates[candidate] += 1

            else:
                candidates[candidate] = 1

for candidate, votes in candidates.items():
     percentage= (votes/total_votes) *100
     candidates_results.append((candidate,votes, percentage))

for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print ("Election Results")
print("------------------------")
print (f"Total Votes: {total_votes}")
print("------------------------")
for candidate, votes, percentage in candidates_results:
     print(f"{candidate}: {percentage:.3f}% ({votes})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

output_folder = "Analysis"
output_file = "Election_Results.txt"
output_path = os.path.join(output_folder, output_file)

with open("Election_Results.txt", "w") as file:
    file.write(f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n")
    [file.write(f"{candidate}: {percentage:.3f}% ({votes})\n") for candidate, votes, percentage in candidates_results]
    file.write("------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("------------------------\n")