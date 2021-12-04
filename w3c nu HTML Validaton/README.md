# W3C HTML Validation Script (w3c-batch.py)
## What is this?
* I created a script (using Python3) that pairs w3c HTML validator errors with their respective webpages and outputs everything to a JSON file. By pairing, I mean, if “stray end tag h3” is an error that appears on 5 pages, all pages should be listed as values for the error (where the error is the key). The script is intended to dramatically speed up the research process for pairing up an error with which webpages contain it. This effort is for the ultimate goal of getting all of the HTML errors in a given codebase documented (so they can be resolved in a systematic way) thus getting closer to w3c HTML compliance.

## How does it work?
* The script works by running the W3C nu HTML checker (v.Nu) on each webpage url listed in important-sites.txt. Python takes the json output from v.Nu and creates a dictionary that pairs the error with an array containing each webpage that has the error.

## Usage/Installation
### Installation steps (assumes you have Python3 and homebrew downloaded)
1. $ pip3 install Unidecode
1. $ brew install vnu

### Usage steps
* important-sites.txt is a .txt file that contains the url of each webpage you want to validate seperated by a newline -- see my example in this repo for an idea of how to structure it
* Make sure you have important-sites.txt in the same directory as where you're running this command
1. $python3 w3c-batch.py

## Expected output
The final results will be displayed both in the terminal and written to “results.json”. The results have each key as the error message and for each error message, there is an array of uris that have the error.
