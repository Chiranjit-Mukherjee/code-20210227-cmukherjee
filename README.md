# code-20210227-cmukherjee
This program calculate BMI (Body Mass Index) and categorise records according to BMI Category and Health Risk. This program can show the total no of overweight patient and can also store the full table to a file.

# Requirements
This program is developped using python3.8. The required modules are stored in requremensts.txt file and can be installed using "pip3 install -r requirements.txt"

# Usage
To use this program you have to pass a .json like following

"python3 bmi_index.py -i data.json"

You can also store the results to .csv or .xls files with optional augument like following

"python3 bmi_index.py -i data.json -o csv / xls"

For clarification of the format of the .json file of patient's records a data.json file has been added as sample.

# Testing
For testing a script "test_scrpt.py" has been added, which will generate a "sample.json" file and compare the output result with desired result.