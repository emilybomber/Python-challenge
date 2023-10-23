#main.py
import os
import csv

#Varibles 
total_votes = 0
candidates = []
total_candidate_votes = 0
#The percentage of votes each candidate won
#The winner of the election based on popular vote

#Set path for file
csvpath = os.path.join("..","election_data.csv")

#Open the Csv
with open(csvpath,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader: