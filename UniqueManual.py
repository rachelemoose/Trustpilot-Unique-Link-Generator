from trustpilot_authenticated_encryption import encryption
import urllib.parse
import urllib.request
import base64
import hashlib

email = "ramo@trustpilot.com"
email_encrypted = base64.b64encode(b"ramo@trustpilot.com")
emailb = email_encrypted.decode("utf-8")
print (emailb)

name = "Rachel Moose"
name_encrypted = urllib.parse.quote("Rachel Moose")
print (name_encrypted)

secret_key = "Enter Secret Key Here"
reference_ID = "REM042890"

SHA1_string = (secret_key + email + reference_ID)
print (SHA1_string)

SHA1_encrypted = hashlib.sha1(str.encode(SHA1_string)).hexdigest()
print (SHA1_encrypted)

uniquelink = ("https://www.trustpilot.com/evaluate/companydomain.com?a=" + reference_ID + "&b=" + emailb + "&c=" + name_encrypted + "&e=" + SHA1_encrypted)
print (uniquelink)


