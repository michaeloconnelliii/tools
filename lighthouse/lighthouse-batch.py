import os
import sys
import subprocess
import json
from unidecode import unidecode

# The result of this program is to have a json object that contains he Lighthouse Audit error ID as our dictionary keys
# Our value object for each key should contain:
# 1. an array of webpages that contain the error
# 2. the formal title of the error
# 3. a description of the error including where to read about via google's documentation
allErrors = {}

# List of .json files to ignore so you don't have to remove them from your target directory to avoid interpreter errors
jsonFilesToIgnore = ['summary.json']

# Get the path of the directory that contains Lighthouse Batch .json output files if path is provided via stdin
# If not, use the current directory
arguments = sys.argv
directory = '.' if len(arguments) == 1 else arguments[1]

# Loop through our chosen directory and find all of the Lighthouse Batch .json output files
for filename in os.listdir(directory):
    if filename.endswith('.json') and filename not in jsonFilesToIgnore:
        # Now that we have our output files, create path to them, open them up, convert to json and loop through them to get their audit keys
        outputFilePath = directory + '/' + filename
        outputFile = open(outputFilePath, 'r')
        jsonOutput = json.load(outputFile)
        # Use audit keys to determine the Lighthouse Audit score - a score of 0 means the error is present that the key is mapped to 
        for auditKey in jsonOutput['audits']:
            # Add the error to our dictionary if it doesn't exist. If it does, simply add the webpage.
            errorObj = jsonOutput['audits'][auditKey]
            if errorObj['score'] == 0:
                webpageUrl = jsonOutput['finalUrl']
                if auditKey not in allErrors:
                    allErrors[auditKey] = {'webpages': [webpageUrl], 'title': errorObj['title'], 'description': errorObj['description']}
                else:
                    allErrors[auditKey]['webpages'].append(webpageUrl)

# Convert our dictionary to a json obj so we can output in a nicely formatted and standard way
finalJson = json.dumps(allErrors, indent = 4)

# Nice to have the final output show up in terminal, too
print(finalJson)

# write to our final json file
with open('results.json', 'w') as f:
    # printing gave me better cosemtic results than writing
    sys.stdout = f
    print(finalJson)