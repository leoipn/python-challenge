import os
import csv
import datetime

################################
# MAIN CODE
################################
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

col_index       = []
col_first_name  = []
col_last_name   = []
col_dob         = []
col_ssn         = []
col_state       = []

# Set the file path
csvpath = os.path.join('Resources', 'employee_data.csv')

# Open the file as csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Iterate over the file to get and transform the values
    for row in csvreader:
        splitted_name = row[1].split(" ")
        first_name    = splitted_name[0]
        last_name     = splitted_name[1]
        dob_formatted = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        masked_ssn    = "***-**-" + row[3][-4:]
        state_code    = us_state_abbrev[row[4]]

        col_index.append(row[0])
        col_first_name.append(first_name)
        col_last_name.append(last_name)
        col_dob.append(dob_formatted)
        col_ssn.append(masked_ssn)
        col_state.append(state_code)

    formatted_info = zip(col_index,col_first_name,col_last_name, col_dob, col_ssn, col_state)

################################
# Write File
################################
# Set variable for output file
output_file = os.path.join("Resources","output","employee_data_formatted.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(formatted_info)
