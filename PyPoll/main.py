import os
import csv

cereal_csv = os.path.join("Resources", "election_data.csv")
totalVote=0
listCandidate=[]
listvotes=[]

# Open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    for row in csvreader:
        totalVote=totalVote+1

     #   print(row)

print("Election Results")
print("------------")
print("Total votes: "+str(totalVote))
print("------------")