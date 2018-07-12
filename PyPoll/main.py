import os
import csv
import pandas as pd


election_data = os.path.join("Resources", "election_data.csv")
#pdFile= pd.read.csv(election_data,"encoding="ISO-8859-1")
pdFile= pd.read_csv(election_data)  #read the data with pandas
total=pdFile["Voter ID"].count()    # get total votes

listCandidate= pdFile["Candidate"].unique()   #get candidates with votes
len=listCandidate.size  #get size of candidates
print(len)
listvotes=pdFile["Candidate"].value_counts() # also use this to calculate
winner=""
winnervote=0


print("Election Results")
print("------------")
print("Total votes: "+str(total))
print("------------")
i = 0
for i in range(len) :
    percent= listvotes[i]/total *100
    percent=percent.round()
    print(listCandidate[i]+" : "+str(listvotes[i])+" votes  ("+str(percent)+"%)")
    i=i+1
print("------------")
print("Winner is : "+ winner)
print("------------")