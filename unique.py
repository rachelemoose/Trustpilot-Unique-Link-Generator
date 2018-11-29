from trustpilot_authenticated_encryption import encryption
import urllib.parse
import urllib.request
import csv
import base64
import hashlib

# Unique Secret Key Object (copy and paste)
secret_key = "Insert Secret Key Here"


# Open Import File with Customer Data
with open('ImportUniqueData.csv', 'r') as f:
	outfile = 'UniqueLinkResults.csv' #Establish outfile that will hold the final unique links
	ofile = open(outfile,'w', newline='') #Open outfile, give writing permissions
	writer = csv.writer(ofile,delimiter='\t')
	for row in f: 
		fieldnames = ("Email","Name","Reference ID")
		r = csv.DictReader(f, fieldnames)
		for row in r:
			emailb = base64.b64encode(row["Email"].encode('utf-8')) # base64 encode customer email address 
			email_encrypted = emailb.decode("utf-8") # remove bytes from base64 encoded email address
			print (email_encrypted) # print base64 email address in ready-to-go format
			name_encrypted = urllib.parse.quote(row["Name"]) # encodeURI value in name column
			print (name_encrypted) # print URIencoded name
			SHA1_string = (secret_key + (row["Email"]) + (row["Reference ID"])) # create string to then be SHA1 encoded - secret key + email address (value in csv) + reference ID (value in csv)
			print (SHA1_string) # print string
			SHA1_encrypted = hashlib.sha1(str.encode(SHA1_string)).hexdigest() # SHA1 encrypt previously created string 
			print (SHA1_encrypted) # print SHA encyrption 
			uniquelink = ("https://www.trustpilot.com/evaluate/companydomain.com?a=" + (row["Reference ID"]) + "&b=" + email_encrypted + "&c=" + name_encrypted + "&e=" + SHA1_encrypted) #combine elements for final unique link
			print (uniquelink)
			ofile.write(uniquelink) # write final unique link in outfile 
			writer.writerow('')
			print("Done!")


		
	







		
	
		