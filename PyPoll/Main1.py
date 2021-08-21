# Import Libraries
import os ,csv

# Declare file path
pypoll = os.path.join("..", "Resources", "budget_data.csv")

pypoll = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyPoll\Resources\election_data.csv'

output = "PyPoll Summary.txt"

# Declare Variables 
totalvotes = 0
candidates = []
candidatevotes = {}
winnercount = 0
winner = ""

# Open and read CSV
with open(pypoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip header
    pybank_header = next(csv_reader) 
 
    # Loop thru the rows in the file
    for row in csv_reader:

        # Calculate the total vote count
        totalvotes += 1

        candidate = row[2]
        
        # Find unique candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidatevotes[candidate] = 1
        
        candidatevotes[candidate] = candidatevotes[candidate] + 1
# A list of unique candidates should be generated and a dictionary with candidate names and corresponding votes when the loop is finished 

# Print the total vote
print(f"Election Results")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Votes: {totalvotes}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Create output and find winner
with open(output, 'w') as txt_file:
    # Create header
    election_header = (f"Election Results\n"
        f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    txt_file.write(election_header)
    txt_file.write(f"Total Votes: {totalvotes}\n")
    txt_file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    for candidate in candidatevotes:
        votes = candidatevotes[candidate]
        votepercentage = float(votes)/float(totalvotes) * 100
        if (votes > winnercount):
            winnercount = votes
            winner = candidate
        voter_output = f"{candidate}: {votepercentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
    
    winning_summary = (f"Winner: {winner}")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print(winning_summary)
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    txt_file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    txt_file.write(f"{winning_summary}\n")
    txt_file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    