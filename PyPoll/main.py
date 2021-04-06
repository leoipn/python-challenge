import os
import csv

total_votes = 0
next_candidate = ""
list_of_unique_candidates = []
dict_candidates = {}
cont = 0
dict_results_of_poll = dict()

# Function that prints and calculates the percentages
def get_poll_results(candidates):
    results_of_poll = []
    previous_candidate_votes = 0
    candidate_keys = candidates.keys()
    dict_poll_results = dict()

    for candidate_key in candidate_keys:
        candidate_info = dict()        
        total_votes_per_candidate = candidates[candidate_key]
        quotient = candidates[candidate_key]/total_votes
        percentage = quotient * 100
        
        if total_votes_per_candidate> previous_candidate_votes:
            dict_poll_results["Winner"] = candidate_key
            previous_candidate_votes = total_votes_per_candidate

        candidate_info["name"] = candidate_key
        candidate_info["percentage"] = percentage
        candidate_info["votes"] = total_votes_per_candidate

        results_of_poll.append(candidate_info)    
    dict_poll_results["results"] = results_of_poll
    #print (dict_poll_results)
    return dict_poll_results

## Main Code
#csvpath = os.path.join('Resources', 'election_data.csv')
csvpath = os.path.join('Resources', 'test.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Read each row of the csv file
    for row in csvreader:
        # Total votes in the file
        total_votes += 1
        
        # Get the candidate
        candidate = row[2]
        
        # List of unique candidates
        if candidate not in list_of_unique_candidates:
            dict_candidates[candidate] = 1
            list_of_unique_candidates.append(candidate)
        else:
            dict_candidates[candidate] +=1

dict_results_of_poll = get_poll_results(dict_candidates)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in dict_results_of_poll["results"]:
    print(f"{result['name']}: {result['percentage']:.2f}% ({result['votes']})")
print("-------------------------")
print(f"---> Winner: {dict_results_of_poll['Winner']}")

#Specify the file to write to
output_path = os.path.join("analysis", "poll_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w')

file.write("Election Results")
file.write("-------------------------")
file.write(f"Total Votes: {total_votes}")
file.write("-------------------------")
file.write(f"{list_of_unique_candidates}")
file.write("-------------------------")

file.close()