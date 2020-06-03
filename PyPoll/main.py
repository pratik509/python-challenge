#The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

 # * The total number of votes cast

  #* A complete list of candidates who received votes

  #* The percentage of votes each candidate won

  #* The total number of votes each candidate won

  #* The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:

 # ```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
import os

import csv

#Setting CSV path

csvpath = os.path.join( 'Resources', 'election_data.csv')

#Creating List to store Data and setting total number of votes = 0
list_of_Candidates = []
total_vote_count = []
total_number_votes = 0

 #Opening CSV fie and skip the header row

with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile)

    #skip the header
    row = next(csvreader,None)

    #Running for Loops in the data set
    for row in csvreader:
        total_number_votes = total_number_votes+1
   
        candidate = (row[2])

#Creating if statements
        if candidate in list_of_Candidates:
            list_of_candidate_index = list_of_Candidates.index(candidate)
            total_vote_count[list_of_candidate_index] = total_vote_count[list_of_candidate_index] + 1
        #else create new spot in list for candidate
        else:
            list_of_Candidates.append(candidate)
            total_vote_count.append(1)

percent = []
maximum_votes = total_vote_count[0]
index = 0

for y in range(len(list_of_Candidates)):
        vote_precent= "{:.3f}".format ((total_vote_count[y]/ total_number_votes*100))
        percent.append(vote_precent)

        if total_vote_count[y] > maximum_votes:
            maximum_votes = total_vote_count[y]
            print(maximum_votes)
        
Winner = list_of_Candidates[index]  

#Priting The results to the terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_number_votes}")
print("--------------------------")
for y in range(len(list_of_Candidates)):
    print(f"{list_of_Candidates[y]}: {percent[y]}% ({total_vote_count[y]})")
print("---------------------------")
print(f"Winner: {Winner}")
print("---------------------------")


#Results to be saved in the below destination folder
output_file = os.path.join('Analysis', 'pypollresults.txt')
        


#open write file
filewriter = open(output_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {total_number_votes}\n")
filewriter.write("--------------------------\n")
for y in range(len(list_of_Candidates)):
    filewriter.write(f"{list_of_Candidates[y]}: {percent[y]}% ({total_vote_count[y]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {Winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()