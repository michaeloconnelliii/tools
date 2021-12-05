# Lighthouse Audit Script (lighthouse-batch.py)
## What is this?
* Similar to the W3C Nu HTML validation batch script, I created a script (using Python3) that pairs Lighthouse Audit Errors with their respective webpages and outputs everything to a JSON file. The python script uses .json output data from running multiple lighthouse audits. 
* In order to generate the lighthouse audit .json output data in an efficient manner, I’ve included instructions for installing and using the npm tool ‘lighthouse-batch’ which allows for batch lighthouse testing. More about lighthouse-batch can be found: https://www.npmjs.com/package/lighthouse-batch and https://github.com/mikestead/lighthouse-batch  
* The script’s goal and intention is similar to the W3C Nu HTML script - for the ultimate goal of getting all of the performance, accessibility and best-practices errors in a given codebase documented (so they can be resolved in a systematic way) thus getting closer to Lighthouse compliance.

## What is Lighthouse?
* Lighthouse is an open-source, automated tool for improving the quality of web pages. You can run it against any web page, public or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO and more. Source: https://developers.google.com/web/tools/lighthouse

## Why Lighthouse?
* Each category mentioned above can be dramatically improved by resolving issues that Lighthouse brings to your attention from an audit. 

## Usage/Installation
### Installation steps (assumes you have Python3 downloaded)
#### Python dependencies
1. $ pip3 install Unidecode

#### Lighthouse CLI
1. $ npm install -g lighthouse

#### Lighthouse-batch
1. $ npm install -g lighthouse-batch

### Usage steps
#### Part 1 - generating lighthouse error output for our python script to read from using Lighthouse-Batch
##### Notes before starting
* Make sure you have important-sites.txt in the same directory as where you’re running the command below.
* I’m only doing audits for accessibility in this example. You can use whatever category you want (performance, best-practices, etc)

##### Running lighthouse-batch
1. $lighthouse-batch --params '--chrome-flags="--headless" --only-categories=accessibility --quiet' -f important-sites.txt
* This will loop through all the sites in important-sites.txt, run a lighthouse audit for the defined category on each site listed and will create a new directory report/lighthouse which will contain all the .json output files you’ll run the script on.

#### Part 2 - Running python script to pair web pages with errors
##### There are 2 ways to do this:
1. Place the script in the same directory as the .json output files and simply run: $python3 .lighthouse-batch.py
1. Or if you run the script from anywhere by supplying where the .json output file directory is in your command (this can be a relative or absolute path)
* Example:
$ python3 .lighthouse-batch.py report/lighthouse/

## Expected output
The final results will be displayed both in the terminal and written to “results.json” (see example output). The results have each key as the Lighthouse Audit Error ID and for each error message, there is an object consisting of an array of uris that have the error, the formal title of the error, and a description of the error.
