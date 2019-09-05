# Trustpilot-Unique-Link-Generator
Create encrypted unique links based on customer data pulled from an Excel file or from customer data entered manually into the script. Use these links to invite customers to review Trustpilot from your own email system or make these links embeddable and put them in an iFrame to collect reviews on your website. 

# Documentation
Trustpilot's Unique Link Product: <https://support.trustpilot.com/hc/en-us/articles/204953148-The-Unique-Link>
Trustpilot's Onsite Review Form Product: <https://support.trustpilot.com/hc/en-us/articles/206514477-The-Embedded-Review-Form>
Note: Trustpilot's Onsite Review Form Product must be used in conjection with Trustpilot's Unique Link Product to collect verified reviews. 

# How to Use
Script 1: "UniqueManual.py"

Manually enter customer data where prompted in the "UniqueManual.py" file 
Data to enter: 
* Email address 
* Name 
* Trustpilot Secret Key
* Domain

Once this information has been entered you can run script. Test the final link to make sure it produces a verified review. 

Script 2: "Unique.py"

Save customer data (email address, name, reference ID) in a csv file called "ImportUniqueData.csv" (or change the file reference in the script - line 13). Create an outfile to save the final links in called "UniqueLinkResults.csv" (or change the file reference in the script - line 14). Input file should host customer email in column A, name in column B, and reference ID in column C. Run script to encrypt customer data and create unique links, which will be printed in output file. Be sure to enter in your domain and Trustpilot secret key on the appropriate lines within the script. 

