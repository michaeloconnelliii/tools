import sys
import subprocess
import json
from unidecode import unidecode

# main location for all of our errors
errors = {}

ignoreMessages = ["The first occurrence of ID"]

# read from test.txt
webpages = open('important-sites.txt', 'r')

for webpage in webpages:
    # run bash command to recieve json
    bashCommand = 'vnu --stdout --format json ' + webpage
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    # clean up output
    output = output.decode('utf-8')
    output = output.strip()

    # convert bash output string to json
    jsonOutput = json.loads(output)

    # parse json
    for obj in jsonOutput["messages"]:
        # write the error our dictionary with the message as the key and a list of urls as the value
        for key in obj:
            if(key == "message"):
                skipMessage = False
                errorMessage = obj[key]
                # skip certain messages as they aren't very helpful
                for ignore in ignoreMessages:
                    # if substring exists, skip the error
                    if(ignore in errorMessage):
                        skipMessage = True
                if(not skipMessage):
                    # decode utf-8 fancy quotes and escape characters
                    errorMessage = errorMessage.encode('utf-8', errors="ignore").decode('utf-8')
                    errorMessage = unidecode(errorMessage)
                    if errorMessage in errors:
                        # Prevent duplicate url entries for the same error
                        if obj["url"] not in errors[errorMessage]:
                            errors[errorMessage].append(obj["url"])
                    else:
                        errors[errorMessage] = [obj["url"]]

# Convert our dictionary to a json obj
finalJson = json.dumps(errors, indent = 4)
print(finalJson)

# write to our final json file
with open('results.json', 'w') as f:
    # printing gave me better cosemtic results than writing
    sys.stdout = f
    print(finalJson)