# Trustpilot-Unique-Link-Generator
Create encrypted unique links based on customer data pulled from an Excel file or customer data entered manually

# How to Use
Option 1: 
Manually enter customer data within the "UniqueManual.py" file 
Data to enter: Email addres, Name, secret key, uniquelink url domain
Run script

Option 2:
Save customer data in a csv file called "ImportUniqueData.csv" (or change the file reference in the script - line 13)
Create an outfile to save the data in called "UniqueLinkResults.csv" (or change the file reference in the script - line 14)
Input file should host customer email in column A, name in column B, and reference ID in column C
Run script to encrypt customer data and create unique links, which will be printed in output file
Use unique links in customer emails or Embedded Review Form 
More information here: 
https://support.trustpilot.com/hc/en-us/articles/204953148-The-Unique-Link
https://support.trustpilot.com/hc/en-us/articles/206514477-The-Embedded-Review-Form
